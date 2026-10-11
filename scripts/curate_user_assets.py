#!/usr/bin/env python3
"""
curate_user_assets.py - Forensic Visual Media Inspection & Keyframe Curation Engine
Part of the Universal Website Architect Engine.

Handles Stage 0 User Asset Intake:
1. Scans user-provided assets (photos, videos, logos) in project directory.
2. Forensically inspects media dimensions, aspect ratios, and orientations using Pillow & ffmpeg.
3. Automatically extracts first-frame, mid-frame, and last-frame posters from videos.
4. Merges user assets with Google Maps scraped assets in 'Hybrid' mode.
5. Maps each asset intelligently to candidate website sections (Hero, Story, Accommodations, Dining, Concierge).
6. Generates prompt & keyframe specifications for Higgsfield video generation or zero-credit fallbacks.
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".svg"}
VIDEO_EXTS = {".mp4", ".webm", ".mov", ".m4v", ".mkv"}

def get_image_metadata(img_path: Path):
    """Extracts width, height, aspect ratio, and classification using Pillow."""
    if not HAS_PIL:
        return {"width": 1920, "height": 1080, "aspect_ratio": 1.78, "orientation": "landscape"}
    try:
        with Image.open(img_path) as img:
            w, h = img.size
            ratio = round(w / h, 2)
            if ratio >= 1.5:
                orientation = "landscape_wide"
            elif ratio >= 1.2:
                orientation = "landscape_standard"
            elif 0.85 <= ratio <= 1.15:
                orientation = "square"
            elif ratio <= 0.65:
                orientation = "portrait_tall"
            else:
                orientation = "portrait_standard"
            return {
                "width": w,
                "height": h,
                "aspect_ratio": ratio,
                "orientation": orientation,
                "format": img.format
            }
    except Exception as e:
        return {"error": str(e), "width": 1920, "height": 1080, "aspect_ratio": 1.78, "orientation": "landscape"}

def get_video_metadata_and_keyframes(video_path: Path, output_dir: Path):
    """
    Uses ffmpeg to probe video dimensions and extract first, mid, and last frame posters.
    """
    meta = {
        "width": 1920,
        "height": 1080,
        "aspect_ratio": 1.78,
        "duration_sec": 10.0,
        "first_frame": None,
        "mid_frame": None,
        "last_frame": None
    }
    
    stem = video_path.stem
    first_frame_path = output_dir / f"{stem}_first_frame.jpg"
    mid_frame_path = output_dir / f"{stem}_mid_frame.jpg"
    last_frame_path = output_dir / f"{stem}_last_frame.jpg"

    # Check if ffmpeg exists
    ffmpeg_bin = shutil.which("ffmpeg")
    if not ffmpeg_bin:
        print(f"[!] Warning: ffmpeg not detected. Skipping keyframe extraction for {video_path.name}")
        return meta

    try:
        # Extract first frame (at 0.1s)
        cmd_first = [
            ffmpeg_bin, "-y", "-ss", "00:00:00.100", "-i", str(video_path),
            "-vframes", "1", "-q:v", "2", str(first_frame_path)
        ]
        subprocess.run(cmd_first, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        if first_frame_path.exists():
            meta["first_frame"] = f"/assets/{first_frame_path.name}"
            # Extract width/height from the extracted frame using Pillow
            if HAS_PIL:
                with Image.open(first_frame_path) as im:
                    meta["width"], meta["height"] = im.size
                    meta["aspect_ratio"] = round(im.size[0] / im.size[1], 2)

        # Extract mid frame (at 3.0s or beginning)
        cmd_mid = [
            ffmpeg_bin, "-y", "-ss", "00:00:03.000", "-i", str(video_path),
            "-vframes", "1", "-q:v", "2", str(mid_frame_path)
        ]
        subprocess.run(cmd_mid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        if mid_frame_path.exists():
            meta["mid_frame"] = f"/assets/{mid_frame_path.name}"

        # Extract last frame (near end)
        cmd_last = [
            ffmpeg_bin, "-y", "-sseof", "-0.5", "-i", str(video_path),
            "-vframes", "1", "-q:v", "2", str(last_frame_path)
        ]
        subprocess.run(cmd_last, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        if last_frame_path.exists():
            meta["last_frame"] = f"/assets/{last_frame_path.name}"

    except Exception as e:
        print(f"[!] Warning during video keyframe extraction: {e}")

    return meta

def classify_asset_section(filename: str, meta: dict) -> str:
    """Heuristically suggests optimal section placement based on name & aspect ratio."""
    f = filename.lower()
    ratio = meta.get("aspect_ratio", 1.78)

    if any(k in f for k in ["hero", "cover", "banner", "main", "drone", "ambient"]):
        return "Section01Hero"
    if any(k in f for k in ["room", "suite", "cottage", "villa", "stay", "accommodation", "bedroom"]):
        return "Section04Accommodations"
    if any(k in f for k in ["food", "dining", "menu", "dish", "chef", "culinary", "breakfast", "coffee"]):
        return "Section05Gastronomy"
    if any(k in f for k in ["grounds", "estate", "nature", "pool", "garden", "walkway", "lawn"]):
        return "Section02Story"
    if any(k in f for k in ["review", "guest", "celebration", "event", "wedding"]):
        return "Section06Testimonials"
    if any(k in f for k in ["logo", "brand", "crest", "symbol", "icon"]):
        return "HeaderNavbar"

    # Ratio heuristics
    if ratio >= 1.6 and meta.get("width", 0) >= 1600:
        return "Section01Hero"
    elif ratio >= 1.2:
        return "Section02Story"
    elif 0.9 <= ratio <= 1.1:
        return "Section03Bento"
    elif ratio <= 0.8:
        return "Section04Accommodations"

    return "GeneralGallery"

def curate_assets(
    mode: str = "hybrid",
    user_assets_dir: str = "user_assets",
    maps_manifest_path: str = "public/assets/assets_manifest.json",
    public_assets_dir: str = "public/assets",
    business_name: str = "The Odyssey Retreat"
):
    """
    Scans and forensically curates user assets, merges with maps assets,
    and outputs a comprehensive unified manifest.
    """
    public_dir = Path(public_assets_dir).resolve()
    public_dir.mkdir(parents=True, exist_ok=True)

    user_dir = Path(user_assets_dir).resolve()
    user_files = []
    if user_dir.exists():
        for ext in IMAGE_EXTS | VIDEO_EXTS:
            user_files.extend(list(user_dir.glob(f"*{ext}")))
            user_files.extend(list(user_dir.glob(f"*{ext.upper()}")))

    # Also check project root for loose user media if user_assets dir was empty
    if not user_files:
        root_dir = Path(".").resolve()
        for ext in [".mp4", ".mov", ".png", ".jpg", ".jpeg"]:
            found = [f for f in root_dir.glob(f"*{ext}") if "node_modules" not in f.parts and ".next" not in f.parts]
            user_files.extend(found)

    print(f"[*] Asset Intake Mode: {mode.upper()}")
    print(f"[*] Found {len(user_files)} user-supplied asset files.")

    curated_photos = []
    curated_videos = []
    video_recommendations = []

    # 1. Process User Assets
    if mode in ["user_only", "hybrid"] and user_files:
        print("\n--- Forensically Inspecting User-Provided Assets ---")
        for uf in user_files:
            dest_file = public_dir / uf.name
            if not dest_file.exists() or dest_file.stat().st_size != uf.stat().st_size:
                shutil.copy2(uf, dest_file)

            ext = uf.suffix.lower()
            if ext in VIDEO_EXTS:
                print(f"  [Video] Inspecting: {uf.name}")
                vmeta = get_video_metadata_and_keyframes(uf, public_dir)
                placement = classify_asset_section(uf.name, vmeta)
                v_entry = {
                    "source": "user_provided",
                    "filename": uf.name,
                    "video": f"/assets/{uf.name}",
                    "poster": vmeta["first_frame"] or f"/assets/{uf.stem}_poster.jpg",
                    "first_frame": vmeta["first_frame"],
                    "mid_frame": vmeta["mid_frame"],
                    "last_frame": vmeta["last_frame"],
                    "width": vmeta["width"],
                    "height": vmeta["height"],
                    "aspect_ratio": vmeta["aspect_ratio"],
                    "candidate_section": placement,
                    "camera_angle_notes": "16:9 Landscape - Optimal for 100vh Hero Ambient Loop" if vmeta["aspect_ratio"] >= 1.5 else "Vertical / Non-standard - Recommended for Mobile Reel or Split Grid"
                }
                curated_videos.append(v_entry)

                # Generate video enhancement / alternative angle advice
                if vmeta["aspect_ratio"] < 1.5:
                    video_recommendations.append({
                        "video": uf.name,
                        "observation": f"Aspect ratio {vmeta['aspect_ratio']} is non-standard for full-screen hero headers.",
                        "higgsfield_recipe": {
                            "tool": "higgsfield.generate_video",
                            "first_frame": vmeta["first_frame"],
                            "aspect_ratio": "16:9",
                            "prompt": f"Slow cinematic wide-angle drone orbit over {business_name}, lush greenery, peaceful golden hour sunlight, 4k ultra-detailed, smooth continuous motion",
                            "role": "ambient_loop"
                        }
                    })
            else:
                imeta = get_image_metadata(uf)
                placement = classify_asset_section(uf.name, imeta)
                p_entry = {
                    "source": "user_provided",
                    "filename": uf.name,
                    "path": f"/assets/{uf.name}",
                    "width": imeta.get("width", 1920),
                    "height": imeta.get("height", 1080),
                    "aspect_ratio": imeta.get("aspect_ratio", 1.78),
                    "orientation": imeta.get("orientation", "landscape_wide"),
                    "candidate_section": placement
                }
                curated_photos.append(p_entry)
                print(f"  [Image] {uf.name} ({imeta.get('width')}x{imeta.get('height')}, {imeta.get('orientation')}) -> Recommended: {placement}")

    # 2. Process Maps / Scraped Assets
    maps_data = {}
    maps_photos = []
    maps_videos = []
    if mode in ["maps_only", "hybrid"] and os.path.exists(maps_manifest_path):
        try:
            with open(maps_manifest_path, "r", encoding="utf-8") as mf:
                maps_data = json.load(mf)
            maps_photos = maps_data.get("photos", [])
            maps_videos = maps_data.get("videos", [])
            print(f"[*] Loaded {len(maps_photos)} Google Maps photos and {len(maps_videos)} scraped videos from manifest.")
        except Exception as e:
            print(f"[!] Warning reading maps manifest: {e}")

    # Merge based on Mode
    if mode == "user_only":
        final_photos = curated_photos
        final_videos = curated_videos
    elif mode == "maps_only":
        final_photos = maps_photos
        final_videos = maps_videos
    else:  # Hybrid: User assets take high-priority Hero/Story slots, Maps fill remaining catalog/amenities
        # Prioritize user photos for Hero and Key Sections
        hero_user = [p for p in curated_photos if p["candidate_section"] == "Section01Hero"]
        other_user = [p for p in curated_photos if p["candidate_section"] != "Section01Hero"]
        
        final_photos = hero_user + other_user + [p for p in maps_photos if p.get("path") not in [up["path"] for up in curated_photos]]
        final_videos = curated_videos + [v for v in maps_videos if v.get("video") not in [uv["video"] for uv in curated_videos]]

    # Ensure at least 1 video entry exists for luxury benchmark standards
    if not final_videos:
        print("[!] No video file found. Generating zero-credit 60fps GPU Ken-Burns fallback specification.")
        first_img = final_photos[0]["path"] if final_photos else "/assets/maps_photo_1.jpg"
        final_videos.append({
            "source": "ken_burns_fallback",
            "video": None,
            "poster": first_img,
            "fallback_style": "animate-ken-burns",
            "candidate_section": "Section01Hero",
            "framing": "16:9 60fps GPU Composited Pan"
        })

    # Assemble Unified Curation Plan
    curation_result = {
        "business_name": business_name,
        "intake_mode": mode,
        "total_curated_photos": len(final_photos),
        "total_curated_videos": len(final_videos),
        "hero_media": {
            "type": "video" if final_videos and final_videos[0].get("video") else "ken_burns_image",
            "src": final_videos[0].get("video") if final_videos else (final_photos[0]["path"] if final_photos else "/assets/maps_photo_1.jpg"),
            "poster": final_videos[0].get("poster") if final_videos else (final_photos[0]["path"] if final_photos else "/assets/maps_photo_1.jpg")
        },
        "photos": final_photos,
        "videos": final_videos,
        "video_generation_recommendations": video_recommendations
    }

    out_manifest_path = public_dir / "unified_curation_manifest.json"
    with open(out_manifest_path, "w", encoding="utf-8") as out_f:
        json.dump(curation_result, out_f, indent=2)

    # Also mirror to assets_manifest.json for downstream compatibility
    standard_manifest_path = public_dir / "assets_manifest.json"
    with open(standard_manifest_path, "w", encoding="utf-8") as sm_f:
        json.dump(curation_result, sm_f, indent=2)

    print("\n" + "=" * 70)
    print("        VISUAL MEDIA & ASSET CURATION COMPLETE")
    print("=" * 70)
    print(f"Mode:             {mode.upper()}")
    print(f"Total Photos:     {len(final_photos)}")
    print(f"Total Videos:     {len(final_videos)}")
    print(f"Hero Media:       {curation_result['hero_media']['type']} -> {curation_result['hero_media']['src']}")
    print(f"Saved Manifest:   {out_manifest_path}")
    if video_recommendations:
        print(f"\n[!] Video Generation Recommendations ({len(video_recommendations)}):")
        for vr in video_recommendations:
            print(f"  • {vr['video']}: {vr['observation']}")
            print(f"    Recipe: {vr['higgsfield_recipe']['prompt']}")
    print("=" * 70 + "\n")

    return curation_result

def main():
    parser = argparse.ArgumentParser(description="Forensic Visual Media & Asset Curation Engine")
    parser.add_argument("--mode", choices=["hybrid", "user_only", "maps_only"], default="hybrid", help="Asset intake mode")
    parser.add_argument("--user-dir", default="user_assets", help="Directory where user placed assets")
    parser.add_argument("--maps-manifest", default="public/assets/assets_manifest.json", help="Scraped Google Maps manifest")
    parser.add_argument("--public-dir", default="public/assets", help="Target public/assets directory")
    parser.add_argument("--business-name", default="The Odyssey Retreat", help="Business name")

    args = parser.parse_args()
    curate_assets(
        mode=args.mode,
        user_assets_dir=args.user_dir,
        maps_manifest_path=args.maps_manifest,
        public_assets_dir=args.public_dir,
        business_name=args.business_name
    )

if __name__ == "__main__":
    main()
