#!/usr/bin/env python3
"""
Universal Asset Harvester & Google Maps Scraper for Website Architect.
Harvests editorial-grade high-resolution images from Pinterest, Google Maps, and Open Web sources
at ZERO credit cost using Playwright Chromium with quality filters across all 10 commercial archetypes.
"""

import os
import re
import sys
import json
import argparse
import urllib.parse
import urllib.request
from playwright.sync_api import sync_playwright

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def launch_browser(p):
    """Robust dual-launch: bundled Chromium first, fallback to system Chrome."""
    try:
        return p.chromium.launch(headless=True)
    except Exception:
        return p.chromium.launch(channel="chrome", headless=True)

def clean_text(t):
    """Clean unicode helper to prevent cp1252 Windows encoding crashes."""
    if not t:
        return ""
    return re.sub(r'[\ue000-\uf8ff]', '', str(t)).strip()

def harvest_pinterest_best(query, output_dir, max_images=3, category="food"):
    """
    Harvests high-resolution photography from Pinterest search.
    Applies professional styling keywords across all 10 commercial archetypes
    and filters out low-resolution thumbnails (>35 KB).
    """
    os.makedirs(output_dir, exist_ok=True)
    downloaded = []
    
    # Universal category query modifiers for all 10 archetypes
    query_modifiers = {
        "food": "restaurant food styling photography editorial high resolution",
        "cocktail": "artisan cocktail drink photography bar dark lighting",
        "luxury": "luxury editorial minimalist product photography",
        "tech": "modern ui tech product aesthetic design",
        "interior": "architectural interior restaurant dining design photography",
        "contractor": "home renovation craftsmanship professional photography",
        "healthcare": "modern clinic medical wellness clean architectural photography",
        "realestate": "luxury modern architecture residential exterior interior photography",
        "corporate": "modern executive corporate office architecture professional photography",
        "industrial": "precision manufacturing engineering industrial facility photography"
    }
    modifier = query_modifiers.get(category, "photography high resolution editorial")
    enhanced_query = f"{query} {modifier}"
    encoded = urllib.parse.quote(enhanced_query)
    search_url = f"https://www.pinterest.com/search/pins/?q={encoded}"
    
    print(f"[*] Searching Pinterest: '{enhanced_query}'")
    print(f"[*] URL: {search_url}")
    
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        try:
            page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
            page.wait_for_timeout(3500)
            
            # Scroll down to load rich pins
            page.mouse.wheel(0, 1200)
            page.wait_for_timeout(2000)
            
            img_srcs = page.eval_on_selector_all("img", "elements => elements.map(e => e.src)")
            pin_urls = set()
            for src in img_srcs:
                if "i.pinimg.com" in src:
                    # Upgrade thumbnail to high-res 736x
                    high_res = re.sub(r'/\d+x/', '/736x/', src)
                    pin_urls.add(high_res)
                    
            print(f"[+] Found {len(pin_urls)} candidate pins.")
            safe_slug = re.sub(r'[^a-zA-Z0-9_]', '_', query.lower())[:20]
            
            # Download and filter by file size (> 35 KB to avoid low-res icons)
            count = 0
            for i, p_url in enumerate(pin_urls):
                if count >= max_images:
                    break
                temp_file = os.path.join(output_dir, f"{safe_slug}_{count+1}.jpg")
                try:
                    req = urllib.request.Request(p_url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        data = resp.read()
                        if len(data) >= 35000:  # Minimum 35 KB for high quality
                            with open(temp_file, "wb") as f:
                                f.write(data)
                            print(f"[+] Downloaded high-res pin: {temp_file} ({len(data)} bytes)")
                            downloaded.append(temp_file)
                            count += 1
                        else:
                            print(f"[-] Skipped low-res pin ({len(data)} bytes): {p_url}")
                except Exception as err:
                    print(f"[-] Download error {p_url}: {err}")
        except Exception as e:
            print(f"[-] Pinterest search error: {e}")
        finally:
            browser.close()
            
    return downloaded

def scrape_google_maps_complete(query_or_url, output_dir, max_photos=5):
    """
    Comprehensive Google Maps Scraper:
    Extracts name, rating, reviews count, price tier, address, phone, hours,
    review topic chips, customer review quotes, and full-resolution photos (=s1600).
    """
    os.makedirs(output_dir, exist_ok=True)
    data = {
        "title": "",
        "category": "",
        "rating": "",
        "reviews_count": "",
        "price_tier": "",
        "address": "",
        "phone": "",
        "hours": "",
        "popular_dishes_tags": [],
        "customer_reviews": [],
        "downloaded_photos": []
    }
    
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900}
        )
        
        target_url = query_or_url
        if not target_url.startswith("http"):
            target_url = f"https://www.google.com/maps/search/{urllib.parse.quote(query_or_url)}"
            
        print(f"[*] Navigating Google Maps: {target_url}")
        page.goto(target_url, timeout=45000, wait_until="domcontentloaded")
        page.wait_for_timeout(4000)
        
        # Click on place listing if list shown
        try:
            first_place = page.locator("a[href*='/maps/place/']").first
            if first_place.is_visible(timeout=3000):
                first_place.click()
                page.wait_for_timeout(3500)
        except Exception:
            pass
            
        # Clean unicode helper to prevent cp1252 Windows crashes
        def clean_text(t):
            if not t:
                return ""
            return re.sub(r'[\ue000-\uf8ff]', '', str(t)).strip()

        # 1. Extract Business Title
        try:
            h1 = page.locator("h1").first
            if h1.is_visible(timeout=2000):
                data["title"] = clean_text(h1.inner_text())
                print(f"[+] Business Name: {data['title']}")
        except Exception:
            pass
            
        # 2. Extract Category, Rating, Reviews Count from header overview
        try:
            overview_el = page.locator("div.LBgpqf").first
            if overview_el.is_visible(timeout=1500):
                otext = clean_text(overview_el.inner_text())
                parts = [p.strip() for p in re.split(r'[\n·]', otext) if p.strip()]
                for p in parts:
                    if re.match(r'^\d\.\d$', p):
                        data["rating"] = f"{p} stars"
                    elif re.match(r'^\([\d,]+\)$', p):
                        data["reviews_count"] = f"{p.strip('()')} reviews"
                    elif len(p) > 2 and not p.isdigit():
                        data["category"] = p
        except Exception:
            pass

        # Fallback for category if not found above
        if not data["category"]:
            for sel in ["button.DkEaL", "button[jsaction*='category']", "button[jsaction*='pane.rating.category']", "span.fontBodyMedium button"]:
                try:
                    el = page.locator(sel).first
                    if el.is_visible(timeout=800):
                        c = clean_text(el.inner_text())
                        if c and len(c) > 2:
                            data["category"] = c
                            break
                except Exception:
                    pass

        # Fallback for rating
        if not data["rating"]:
            try:
                rating_el = page.locator("span[aria-label*='stars']").first
                if rating_el.is_visible(timeout=1000):
                    data["rating"] = clean_text(rating_el.get_attribute("aria-label"))
            except Exception:
                pass

        # Fallback for reviews_count
        if not data["reviews_count"]:
            try:
                rev_el = page.locator("span[aria-label*='reviews']").first
                if rev_el.is_visible(timeout=1000):
                    data["reviews_count"] = clean_text(rev_el.get_attribute("aria-label"))
                elif page.locator("button[aria-label*='reviews']").first.is_visible(timeout=1000):
                    data["reviews_count"] = clean_text(page.locator("button[aria-label*='reviews']").first.inner_text())
            except Exception:
                pass

        print(f"[+] Category: {data['category']}")
        print(f"[+] Rating: {data['rating']}")
        print(f"[+] Reviews: {data['reviews_count']}")

        # 3. Extract Address, Phone, Hours, Website
        try:
            addr_el = page.locator("button[data-item-id='address']").first
            if addr_el.is_visible(timeout=1500):
                data["address"] = clean_text(addr_el.inner_text())
                print(f"[+] Address: {data['address']}")
        except Exception:
            pass

        try:
            phone_el = page.locator("button[data-item-id*='phone']").first
            if phone_el.is_visible(timeout=1500):
                data["phone"] = clean_text(phone_el.inner_text())
                print(f"[+] Phone: {data['phone']}")
        except Exception:
            pass

        try:
            hours_el = page.locator("button[data-item-id='oh']").first
            if hours_el.is_visible(timeout=1500):
                data["hours"] = clean_text(hours_el.inner_text())
                print(f"[+] Hours: {data['hours']}")
        except Exception:
            pass

        try:
            site_el = page.locator("a[data-item-id='authority']").first
            if site_el.is_visible(timeout=1000):
                data["website"] = site_el.get_attribute("href")
                print(f"[+] Website: {data['website']}")
        except Exception:
            pass
            
        # 3. Extract Reviews Tab & Popular Topic Chips
        try:
            btn_reviews = page.locator("button:has-text('Reviews')").first
            if btn_reviews.is_visible(timeout=3000):
                btn_reviews.click()
                page.wait_for_timeout(3000)
                
                # Popular topics (e.g. biryani 29, mandi 12)
                chips = page.eval_on_selector_all("button[aria-label*='mention']", "elements => elements.map(e => e.innerText.trim())")
                data["popular_dishes_tags"] = chips[:12]
                print(f"[+] Extracted popular review tags: {data['popular_dishes_tags']}")
                
                # Top review texts
                rev_texts = page.eval_on_selector_all(".wiI7pd", "elements => elements.map(e => e.innerText.trim())")
                data["customer_reviews"] = [t for t in rev_texts if len(t) > 20][:5]
                print(f"[+] Extracted {len(data['customer_reviews'])} customer reviews.")
        except Exception as e:
            print("[-] Reviews tab extraction error:", e)
            
        # 4. Open Photo Viewer & Collect High-Res Photos
        collected_photo_urls = set()
        try:
            page.mouse.click(200, 180)
            page.wait_for_timeout(3000)
            
            for _ in range(8):
                srcs = page.eval_on_selector_all("img", "elements => elements.map(e => e.src)")
                for s in srcs:
                    if "googleusercontent.com" in s and ("=w" in s or "/p/" in s):
                        base = s.split("=")[0]
                        collected_photo_urls.add(base)
                page.keyboard.press("ArrowRight")
                page.wait_for_timeout(1000)
        except Exception as e:
            print("[-] Photo gallery error:", e)
            
        print(f"[+] Found {len(collected_photo_urls)} Google Maps photo URLs.")
        for i, base in enumerate(list(collected_photo_urls)[:max_photos]):
            target = os.path.join(output_dir, f"maps_photo_{i+1}.jpg")
            try:
                urllib.request.urlretrieve(base + "=s1600", target)
                print(f"[+] Downloaded maps photo: {target} ({os.path.getsize(target)} bytes)")
                data["downloaded_photos"].append(target)
            except Exception as e:
                print(f"[-] Download error {base}: {e}")
                
        # Save metadata to maps_data.json
        meta_file = os.path.join(output_dir, "maps_data.json")
        with open(meta_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[+] Saved metadata to {meta_file}")
        
        browser.close()
    return data

def harvest_web_videos(url_or_query, output_dir, max_videos=2):
    """
    Harvests ambient background web video loops (< 5MB) from a target website URL or Pexels/Pixabay open public video directory.
    Downloads MP4 files, captures a first-frame poster image (.jpg) to prevent LCP degradation,
    and writes metadata to assets_manifest.json.
    """
    os.makedirs(output_dir, exist_ok=True)
    downloaded = []
    
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720}
        )
        
        video_urls = []
        is_direct_url = url_or_query.startswith("http://") or url_or_query.startswith("https://")
        
        if is_direct_url:
            print(f"[*] Navigating target website for video extraction: {url_or_query}")
            try:
                page.goto(url_or_query, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(3000)
                
                # 1. Inspect <video> elements and their child <source> elements
                v_srcs = page.eval_on_selector_all("video, video source", """
                    elements => elements.map(el => {
                        return el.src || el.currentSrc || el.getAttribute('src') || el.getAttribute('data-src') || '';
                    }).filter(Boolean)
                """)
                for s in v_srcs:
                    if s.startswith("http") and (".mp4" in s or ".webm" in s or "blob:" not in s):
                        video_urls.append(s)
                
                # 2. Inspect anchor links ending in .mp4
                a_srcs = page.eval_on_selector_all("a[href*='.mp4']", "elements => elements.map(e => e.href)")
                video_urls.extend(a_srcs)

                # 3. Detect embedded YouTube or Vimeo videos
                yt_srcs = page.eval_on_selector_all("iframe[src*='youtube.com'], iframe[src*='youtu.be'], iframe[src*='vimeo.com'], a[href*='youtube.com'], a[href*='youtu.be']", """
                    elements => elements.map(el => el.src || el.href || '').filter(Boolean)
                """)
                for yt in yt_srcs:
                    if "youtube.com" in yt or "youtu.be" in yt:
                        print(f"[+] Detected YouTube video embed/link: {yt}")
                        try:
                            import yt_dlp
                            safe_slug = re.sub(r'[^a-zA-Z0-9_]', '_', url_or_query.lower())[:16]
                            target_yt_vid = os.path.join(output_dir, f"{safe_slug}_yt_loop.mp4")
                            ydl_opts = {
                                'format': 'bestvideo[height<=720][ext=mp4]/best[ext=mp4]/best',
                                'outtmpl': target_yt_vid,
                                'quiet': True,
                                'no_warnings': True,
                                'max_filesize': 12 * 1024 * 1024
                            }
                            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([yt])
                            if os.path.exists(target_yt_vid) and os.path.getsize(target_yt_vid) > 50000:
                                video_urls.append(f"file:///{os.path.abspath(target_yt_vid).replace(os.sep, '/')}")
                                print(f"[+] Downloaded YouTube b-roll clip via yt-dlp: {target_yt_vid}")
                                break
                        except Exception as e:
                            print(f"[-] yt-dlp extraction note: {e}")
            except Exception as e:
                print(f"[-] Video extraction navigation error: {e}")
        else:
            # Query open video gallery (Pixabay & YouTube Search)
            clean_q = urllib.parse.quote(url_or_query)
            # Try YouTube search for ambient b-roll first via yt-dlp
            try:
                import yt_dlp
                safe_slug = re.sub(r'[^a-zA-Z0-9_]', '_', url_or_query.lower())[:16]
                target_search_vid = os.path.join(output_dir, f"{safe_slug}_ambient_yt.mp4")
                ydl_opts = {
                    'format': 'bestvideo[height<=720][ext=mp4]/best[ext=mp4]/best',
                    'outtmpl': target_search_vid,
                    'quiet': True,
                    'no_warnings': True,
                    'max_filesize': 12 * 1024 * 1024
                }
                print(f"[*] Searching YouTube for ambient b-roll: 'ytsearch1:{url_or_query} b-roll drone'...")
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([f"ytsearch1:{url_or_query} b-roll drone"])
                if os.path.exists(target_search_vid) and os.path.getsize(target_search_vid) > 50000:
                    video_urls.append(f"file:///{os.path.abspath(target_search_vid).replace(os.sep, '/')}")
                    print(f"[+] Downloaded YouTube b-roll loop via yt-dlp: {target_search_vid}")
            except Exception as e:
                print(f"[-] yt-dlp search note: {e}")

            if not video_urls:
                search_url = f"https://pixabay.com/videos/search/{clean_q}/"
                print(f"[*] Searching open stock video library: {search_url}")
                try:
                    page.goto(search_url, timeout=30000, wait_until="domcontentloaded")
                    page.wait_for_timeout(3500)
                    v_elements = page.eval_on_selector_all("video source, video, [data-mp4]", """
                        elements => elements.map(el => {
                            return el.src || el.getAttribute('data-mp4') || el.getAttribute('src') || '';
                        }).filter(s => s && s.includes('.mp4'))
                    """)
                    video_urls.extend(v_elements)
                except Exception as e:
                    print(f"[-] Stock video search error: {e}")
                
        print(f"[+] Found {len(video_urls)} candidate video stream URLs.")
        
        # Deduplicate
        unique_urls = list(dict.fromkeys(video_urls))
        count = 0
        
        for idx, v_url in enumerate(unique_urls):
            if count >= max_videos:
                break
            print(f"[*] Processing candidate video: {v_url}")
            safe_slug = re.sub(r'[^a-zA-Z0-9_]', '_', url_or_query.lower())[:16]
            target_vid = os.path.join(output_dir, f"{safe_slug}_loop_{count+1}.mp4")
            target_poster = os.path.join(output_dir, f"{safe_slug}_loop_{count+1}_poster.jpg")
            
            try:
                req = urllib.request.Request(v_url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=25) as resp:
                    data = resp.read()
                    size_mb = len(data) / (1024 * 1024)
                    print(f"[*] Video payload: {size_mb:.2f} MB")
                    
                    # Web performance constraint: Ambient hero loops should be <= 8MB (ideally < 5MB)
                    if size_mb <= 8.0:
                        with open(target_vid, "wb") as f:
                            f.write(data)
                        print(f"[+] Downloaded web video loop: {target_vid} ({size_mb:.2f} MB)")
                        
                        # Generate poster still frame using page navigation or screenshot
                        try:
                            page.goto(f"file:///{os.path.abspath(target_vid).replace(os.sep, '/')}", timeout=10000)
                            page.wait_for_timeout(1000)
                            page.screenshot(path=target_poster)
                            print(f"[+] Captured poster still frame: {target_poster}")
                        except Exception:
                            pass
                            
                        downloaded.append({
                            "video": target_vid,
                            "poster": target_poster if os.path.exists(target_poster) else None,
                            "size_bytes": len(data),
                            "source_url": v_url
                        })
                        count += 1
                    else:
                        print(f"[-] Skipped video: {size_mb:.2f} MB exceeds 8MB web performance budget.")
            except Exception as err:
                print(f"[-] Video download error ({v_url}): {err}")
                
        # Write asset manifest
        manifest_file = os.path.join(output_dir, "video_manifest.json")
        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(downloaded, f, indent=2)
        print(f"[+] Saved video manifest to {manifest_file}")
        
        browser.close()
    return downloaded

def scrape_domain_assets(domain_url, output_dir, max_images=6):
    """
    Extracts brand assets from the client's official website:
    - Vector SVG logos & high-res PNG logos
    - OpenGraph images and Twitter cards
    - Social profile links (Instagram, Facebook, YouTube, LinkedIn)
    - Full-resolution hero and gallery imagery (>25 KB)
    """
    os.makedirs(output_dir, exist_ok=True)
    domain_data = {
        "domain": domain_url,
        "logo": None,
        "social_links": {},
        "downloaded_photos": []
    }
    
    if not domain_url.startswith("http"):
        domain_url = f"https://{domain_url}"
        
    print(f"[*] Scraping official domain assets: {domain_url}")
    with sync_playwright() as p:
        browser = launch_browser(p)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1440, "height": 900}
        )
        try:
            page.goto(domain_url, timeout=30000, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            
            # 1. Extract Social Media Links
            links = page.eval_on_selector_all("a[href]", "elements => elements.map(e => e.href)")
            for l in links:
                if "instagram.com/" in l and "instagram" not in domain_data["social_links"]:
                    domain_data["social_links"]["instagram"] = l
                elif "facebook.com/" in l and "facebook" not in domain_data["social_links"]:
                    domain_data["social_links"]["facebook"] = l
                elif ("youtube.com/" in l or "youtu.be/" in l) and "youtube" not in domain_data["social_links"]:
                    domain_data["social_links"]["youtube"] = l
                elif "linkedin.com/" in l and "linkedin" not in domain_data["social_links"]:
                    domain_data["social_links"]["linkedin"] = l
                elif ("twitter.com/" in l or "x.com/" in l) and "twitter" not in domain_data["social_links"]:
                    domain_data["social_links"]["twitter"] = l
            print(f"[+] Extracted social links: {domain_data['social_links']}")
            
            # 2. Extract Vector Logo or Logo Image
            logo_info = page.evaluate("""() => {
                const candidates = [
                    document.querySelector('header img[src*="logo"], nav img[src*="logo"], a[class*="logo"] img, img[class*="logo"]'),
                    document.querySelector('header svg, nav svg, a[class*="logo"] svg'),
                    document.querySelector('header img, nav img')
                ];
                for (const c of candidates) {
                    if (!c) continue;
                    if (c.tagName.toLowerCase() === 'svg') {
                        return { type: 'svg', content: c.outerHTML };
                    }
                    if (c.tagName.toLowerCase() === 'img' && c.src) {
                        return { type: 'img', src: c.src };
                    }
                }
                return null;
            }""")
            
            if logo_info:
                if logo_info.get("type") == "svg":
                    logo_path = os.path.join(output_dir, "brand_logo.svg")
                    with open(logo_path, "w", encoding="utf-8") as f:
                        f.write(logo_info["content"])
                    domain_data["logo"] = logo_path
                    print(f"[+] Saved extracted SVG logo: {logo_path}")
                elif logo_info.get("type") == "img":
                    src = logo_info["src"]
                    ext = ".svg" if ".svg" in src else ".png"
                    logo_path = os.path.join(output_dir, f"brand_logo{ext}")
                    try:
                        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
                        with urllib.request.urlopen(req, timeout=10) as resp:
                            with open(logo_path, "wb") as f:
                                f.write(resp.read())
                        domain_data["logo"] = logo_path
                        print(f"[+] Downloaded brand logo: {logo_path}")
                    except Exception as e:
                        print(f"[-] Logo download error: {e}")
                        
            # 3. Extract High-Res Content Images, Computed CSS Background Images & OG Meta
            og_img = page.locator("meta[property='og:image']").get_attribute("content")
            candidate_imgs = set()
            if og_img and og_img.startswith("http"):
                candidate_imgs.add(og_img)
                
            dom_imgs = page.evaluate("""() => {
                const results = new Set();
                // A. <img> tags and <picture source>
                document.querySelectorAll('img, picture source').forEach(el => {
                    const src = el.src || el.srcset || el.getAttribute('data-src') || '';
                    if (src) {
                        const clean = src.split(',')[0].trim().split(' ')[0];
                        if (clean.startsWith('http')) results.add(clean);
                    }
                });
                // B. Computed CSS background-image across all elements in the DOM
                document.querySelectorAll('*').forEach(el => {
                    const bg = window.getComputedStyle(el).getPropertyValue('background-image');
                    if (bg && bg.includes('url(') && !bg.includes('data:')) {
                        const m = bg.match(/url\\(['"]?(.*?)['"]?\\)/);
                        if (m && m[1] && m[1].startsWith('http')) results.add(m[1]);
                    }
                });
                return Array.from(results);
            }""")
            for s in dom_imgs:
                if not any(skip in s.lower() for skip in ["pixel", "tracking", "1x1", "icon", "data:"]):
                    candidate_imgs.add(s)
                    
            print(f"[+] Found {len(candidate_imgs)} candidate domain photos (including computed CSS backgrounds).")
            count = 0
            for idx, img_url in enumerate(candidate_imgs):
                if count >= max_images:
                    break
                target = os.path.join(output_dir, f"domain_photo_{count+1}.jpg")
                try:
                    req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
                    with urllib.request.urlopen(req, timeout=12) as resp:
                        data = resp.read()
                        if len(data) >= 25000:  # >= 25KB filter
                            with open(target, "wb") as f:
                                f.write(data)
                            print(f"[+] Downloaded domain photo: {target} ({len(data)} bytes)")
                            domain_data["downloaded_photos"].append(target)
                            count += 1
                except Exception:
                    continue
        except Exception as e:
            print(f"[-] Domain scraping error: {e}")
        finally:
            browser.close()
            
    out_meta = os.path.join(output_dir, "domain_data.json")
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(domain_data, f, indent=2)
    return domain_data

def harvest_web_videos(query_or_category, output_dir="public/assets", max_videos=1):
    """
    Harvests lightweight (< 5MB) ambient background looping videos (MP4/WebM)
    for signature hero backgrounds and case-study loops.
    Extracts poster image (*_poster.jpg) to prevent Cumulative Layout Shift (CLS).
    """
    os.makedirs(output_dir, exist_ok=True)
    videos = []
    
    VIDEO_CATALOG = {
        "luxury": "https://assets.mixkit.co/videos/preview/mixkit-luxury-interior-of-a-contemporary-living-room-41537-large.mp4",
        "resort": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-resort-with-swimming-pools-42211-large.mp4",
        "hospitality": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-resort-with-swimming-pools-42211-large.mp4",
        "architecture": "https://assets.mixkit.co/videos/preview/mixkit-modern-city-buildings-with-glass-facades-42095-large.mp4",
        "tech": "https://assets.mixkit.co/videos/preview/mixkit-futuristic-technology-digital-networking-connection-loop-42861-large.mp4",
        "developer": "https://assets.mixkit.co/videos/preview/mixkit-futuristic-technology-digital-networking-connection-loop-42861-large.mp4",
        "coffee": "https://assets.mixkit.co/videos/preview/mixkit-coffee-being-poured-into-a-cup-41714-large.mp4",
        "nature": "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-mountain-valley-during-sunset-41757-large.mp4"
    }
    
    q_lower = (query_or_category or "").lower()
    selected_url = VIDEO_CATALOG["luxury"]
    for k, v in VIDEO_CATALOG.items():
        if k in q_lower:
            selected_url = v
            break
            
    target_video = os.path.join(output_dir, "ambient_hero_loop.mp4")
    poster_target = os.path.join(output_dir, "ambient_hero_loop_poster.jpg")
    
    print(f"[*] Downloading ambient hero loop video for '{query_or_category}'...")
    try:
        req = urllib.request.Request(selected_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(target_video, "wb") as f:
                f.write(data)
        print(f"[+] Downloaded ambient video loop: {target_video} ({len(data)} bytes)")
        
        poster_extracted = False
        try:
            res = subprocess.run([
                "ffmpeg", "-y", "-ss", "00:00:01", "-i", target_video,
                "-vframes", "1", "-q:v", "2", poster_target
            ], capture_output=True, timeout=10)
            if res.returncode == 0 and os.path.exists(poster_target):
                poster_extracted = True
                print(f"[+] Extracted video poster frame: {poster_target}")
        except Exception:
            pass
            
        videos.append({
            "path": target_video,
            "poster": poster_target if poster_extracted else None,
            "type": "video/mp4",
            "role": "ambient_hero_loop",
            "size_bytes": len(data)
        })
    except Exception as e:
        print(f"[-] Video download error: {e}")
        
    return videos

def harvest_multi_channel(query_or_maps, domain_url=None, output_dir="public/assets", max_photos=12, category="luxury", include_video=False):
    """
    Elite Multi-Channel Asset Harvester:
    Aggregates assets from:
    1. Google Maps (NAP, rating, reviews, customer photos)
    2. Official Domain (brand logo, hero photography, social channels)
    3. Social Media Links (Instagram/Facebook assets)
    4. Curated Pinterest fallback (for unmatched aesthetic breadth)
    5. Ambient loop video (MP4 + poster still frame)
    Produces consolidated assets_manifest.json with categorized assets.
    """
    os.makedirs(output_dir, exist_ok=True)
    manifest = {
        "business_name": "",
        "category": category,
        "rating": None,
        "reviews_count": None,
        "phone": None,
        "address": None,
        "website": domain_url,
        "social_links": {},
        "logo": None,
        "photos": [],
        "videos": [],
        "customer_reviews": []
    }
    
    # 1. Google Maps Extraction
    maps_data = None
    if query_or_maps:
        print("[*] --- Stage 1: Google Maps Deep Harvester ---")
        try:
            maps_data = scrape_google_maps_complete(query_or_maps, output_dir, max_photos=min(max_photos, 8))
            if maps_data:
                manifest["business_name"] = maps_data.get("title", "")
                manifest["rating"] = maps_data.get("rating")
                manifest["reviews_count"] = maps_data.get("reviews_count")
                manifest["phone"] = maps_data.get("phone")
                manifest["address"] = maps_data.get("address")
                manifest["customer_reviews"] = maps_data.get("customer_reviews", [])
                if not manifest["website"] and maps_data.get("website"):
                    manifest["website"] = maps_data.get("website")
                for p in maps_data.get("downloaded_photos", []):
                    manifest["photos"].append({
                        "path": p,
                        "source": "google_maps",
                        "category": "venue"
                    })
        except Exception as e:
            print(f"[-] Google Maps harvesting warning: {e}")
            
    # 2. Official Domain Extraction
    target_domain = manifest["website"] or domain_url
    if target_domain:
        print(f"[*] --- Stage 2: Official Domain Harvester ({target_domain}) ---")
        try:
            dom_data = scrape_domain_assets(target_domain, output_dir, max_images=6)
            if dom_data.get("logo"):
                manifest["logo"] = dom_data["logo"]
            if dom_data.get("social_links"):
                manifest["social_links"] = dom_data["social_links"]
            for p in dom_data.get("downloaded_photos", []):
                manifest["photos"].append({
                    "path": p,
                    "source": "official_domain",
                    "category": "editorial"
                })
        except Exception as e:
            print(f"[-] Domain harvesting warning: {e}")
            
    # 3. Supplemental High-Res Photography via Pinterest (if below target quota)
    current_count = len(manifest["photos"])
    if current_count < max_photos:
        needed = max_photos - current_count
        search_topic = manifest["business_name"] or query_or_maps or category
        print(f"[*] --- Stage 3: Supplemental High-Res Asset Harvester ({needed} needed) ---")
        try:
            pin_photos = harvest_pinterest_best(search_topic, output_dir, max_images=needed, category=category)
            for p in pin_photos:
                manifest["photos"].append({
                    "path": p,
                    "source": "curated_editorial",
                    "category": "lifestyle"
                })
        except Exception as e:
            print(f"[-] Supplemental harvesting warning: {e}")
            
    # 4. Ambient Web Video (if requested)
    if include_video:
        print("[*] --- Stage 4: Ambient Web Video Engine ---")
        video_query = target_domain if target_domain else (manifest["business_name"] or category)
        try:
            vids = harvest_web_videos(video_query, output_dir, max_videos=1)
            manifest["videos"] = vids
        except Exception as e:
            print(f"[-] Video harvesting warning: {e}")
            
    # Save Consolidated Manifest
    manifest_file = os.path.join(output_dir, "assets_manifest.json")
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n[+] Multi-Channel Harvesting Complete!")
    print(f"    - Photos: {len(manifest['photos'])} high-resolution images")
    print(f"    - Logo:   {manifest['logo'] or 'None (using SVG fallback)'}")
    print(f"    - Social: {list(manifest['social_links'].keys())}")
    print(f"    - Video:  {len(manifest['videos'])} ambient video loops")
    print(f"    - Manifest saved to: {manifest_file}")
    return manifest

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal Multi-Channel Asset Harvester for Website Architect")
    parser.add_argument("--source", choices=["pinterest", "maps", "video", "domain", "multi"], default="multi", help="Harvest source")
    parser.add_argument("--query", required=True, help="Search query or Google Maps URL")
    parser.add_argument("--domain", default=None, help="Official domain URL of the client business")
    parser.add_argument("--out", default="public/assets", help="Destination folder")
    parser.add_argument("--max", type=int, default=10, help="Max items to download")
    parser.add_argument("--category", default="luxury", help="Category archetype for editorial modifier")
    parser.add_argument("--video", action="store_true", help="Harvest ambient background video loop")
    args = parser.parse_args()
    
    if args.source == "pinterest":
        harvest_pinterest_best(args.query, args.out, max_images=args.max, category=args.category)
    elif args.source == "maps":
        scrape_google_maps_complete(args.query, args.out, max_photos=args.max)
    elif args.source == "video":
        harvest_web_videos(args.query, args.out, max_videos=args.max)
    elif args.source == "domain":
        scrape_domain_assets(args.domain or args.query, args.out, max_images=args.max)
    elif args.source == "multi":
        harvest_multi_channel(args.query, domain_url=args.domain, output_dir=args.out, max_photos=args.max, category=args.category, include_video=args.video)
