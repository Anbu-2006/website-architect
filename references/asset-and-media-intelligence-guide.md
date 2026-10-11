# Master Asset & Media Intelligence Guide: Image & Video Engineering

> **Authoritative Media Specification for `/website-architect`**  
> Covers: 8-Dimension De-AI Photographic Prompting, Video Creation (Higgsfield & Canvas), Video Scraping & Web Optimization, Google Maps & Pinterest High-Resolution Harvesting, and Frontend Video Integration.

---

## 1. Master Media Modality Strategy

Before sourcing or generating media, determine the exact media layer for each section of the site:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MASTER MEDIA MODALITY MATRIX                    │
├─────────────────────┬──────────────────────────────────────────────────┤
│ 1. 35MM EDITORIAL   │ Best for: Physical venues, culinary dishes, real │
│    PHOTOGRAPHY      │ estate, craft products, team portraits.          │
│                     │ Source: Harvested =s1600 / 736x or native prompt.│
├─────────────────────┼──────────────────────────────────────────────────┤
│ 2. AMBIENT VIDEO    │ Best for: Hero backgrounds, dynamic ambiance,    │
│    LOOPS (< 5MB)    │ scrollytelling reveals, cinematic craftsmanship. │
│                     │ Source: Higgsfield generate_video / harvested MP4│
├─────────────────────┼──────────────────────────────────────────────────┤
│ 3. 3D / WEBGL       │ Best for: Flagship tech, interactive products,   │
│    CANVAS (60 FPS)  │ avant-garde portfolios, spatial config tools.    │
│                     │ Source: ThreeUI (@designcodeio/threeui) / R3F.   │
├─────────────────────┼──────────────────────────────────────────────────┤
│ 4. REACTIVE VECTOR  │ Best for: UI marks, certification badges, logos, │
│    & MICRO-ICONS    │ data telemetry icons (Lucide, Heroicons, SVGL).  │
│                     │ Source: 21st-magic / SVGL / Lucide.              │
└─────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. The 8-Dimension De-AI Photographic Prompting Framework

To generate imagery that looks like authentic editorial photography rather than synthetic "AI plastic," use the native `generate_image` tool with this 8-dimension prompt structure:

```
[Persona/Subject] + [Material & Texture] + [Moment & Action] + [Lens & Optics] + [Lighting & Atmosphere] + [Framing & Horizon] + [Color Signature] + [Strict Negatives]
```

### The 8 Dimensions Explained:
1. **Persona / Core Subject**: Specify exact physical subjects with authentic human imperfections or architectural details. Never use vague labels like "beautiful villa". Specify: "Hand-quarried limestone pergola overlooking a terraced infinity pool".
2. **Material & Surface Texture**: Demand tangible material reality: "visible porous travertine stone, authentic cedar wood grain with knots, tactile raw linen weave, condensation beads on glassware, crisp rising steam".
3. **Moment & Natural Action**: Capture a documentary moment: "early morning light filtering through olive branches at 45 degrees, empty quiet dining table with folded linen napkins, artisan hands slicing sourdough".
4. **Lens & Optical Setup**: Emulate real glass: "35mm prime lens, f/2.8 shallow depth of field, natural optical falloff, creamy background bokeh, zero barrel distortion, crisp rectilinear perspective".
5. **Lighting & Atmosphere**: Declare directional natural light: "soft morning window light from the left casting gentle shadows, warm 3200K ambient fill, natural shadow gradation, visible sun dust".
6. **Framing & Horizon**: Enforce straight architectural framing: "documentary candid framing, eye-level perspective, straight horizontal horizon with parallel vertical columns, generous negative space on the right for typography".
7. **Color Signature & Film Stock**: Specify analog film stock: "Kodak Portra 400 aesthetic, warm muted earthy tones, deep organic blacks, desaturated foliage greens".
8. **Strict Negative Prompt (MANDATORY)**:
   ```
   NEGATIVE PROMPT: plastic skin, porcelain smoothing, cartoon rendering, 3D CGI shine, Unreal Engine render, over-sharpened HDR, neon glow, bloom, tilted horizon, artificial studio strobes, blurry foreground, distorted hands, stock photo cliché
   ```

### Archetype-Specific Production Image Prompts:

#### A. Luxury Farmstay / Eco-Resort:
> *"Editorial documentary photograph of a private stone villa pavilion at Krishi Farms at sunrise. Porous terracotta floor tiles, aged teak sun loungers with natural linen cushions, quiet calm infinity pool reflecting morning mist and surrounding silver oak trees. Shot on 35mm film stock, 50mm f/2.8 lens, natural golden hour sidelight from the left casting long soft shadows. Straight horizontal horizon, parallel architectural columns, clean negative space on the left for headline copy. Kodak Portra color grading, warm earthy palette. Negative: no CGI shine, no plastic rendering, no HDR, no tilted angles."*

#### B. Highway Dining & Artisan Restaurant:
> *"Close-up editorial food photograph of authentic fragrant mutton dum biryani served in an aged brass hand-hammered handi, garnished with fried golden onions and fresh mint leaves. Condensation on a copper water tumbler beside a small bowl of pomegranate raita. Natural directional window lighting from 45 degrees, shallow depth of field with 50mm macro lens at f/2.8, visible steam rising naturally. Dark textured slate tabletop, rich warm spices palette. Negative: no oversaturated plastic colors, no studio strobe glare, no fake steam, no CGI."*

#### C. B2B SaaS & Developer Platform:
> *"High-craft architectural photograph of an executive modern engineering workspace. Dark brushed aluminum laptop displaying clean syntax-highlighted code tabs, subtle ambient warm desk lamp at 2700K illuminating matte walnut desk grain. Crisp geometric shadows, eye-level perspective, clean minimal negative space. Negative: no floating neon holographic wireframes, no generic glowing cybernetic globes, no stock photo business handshakes."*

---

## 3. Video Creation, Scraping & Looping Protocol

### 3.1 When to Use Video
* **Hero Ambient Loop**: 5–8 second muted loop showing atmosphere (steam rising, pool ripples, wind in trees, moving road).
* **Product Feature Teaser**: Micro-walkthrough of a UI interaction, dynamic calculator slider, or booking flow.
* **Kinetic Background Texture**: Subtle fluid or particle dynamics behind high-impact typography.

### 3.2 100% Free / Zero-Credit Ambient Video Engine (Free Alternative to Paid Generators)
> [!IMPORTANT]
> **STRICT ZERO-CREDIT POLICY**:
> External video generation APIs (such as Higgsfield) cost paid credits. Under the **100% Free Mandate**, external paid calls are strictly banned. Instead, ambient video hero loops and cinematic visual motion are produced with 100% free, zero-cost mechanisms:
>
> 1. **Tier 1: Direct Network Interception & DOM Stream Extraction ($0.00)**:
>    Playwright Chromium sniffs active network streaming responses (`.mp4`, `.webm`, `.m3u8`) and inspects `<video>`/`<source>` DOM elements, downloading high-definition video loops locally without relying on HTML markup alone.
> 2. **Tier 2: YouTube & Vimeo B-Roll Harvester via `yt-dlp` ($0.00)**:
>    Autonomous extraction of promotional video clips or ambient b-roll from linked YouTube channels, embeds, or targeted `ytsearch1:"<business> b-roll drone"` queries, packaged as high-efficiency 720p MP4 loops (< 8MB).
> 3. **Tier 3: Public HD Royalty-Free Ambient Loops (Pexels / Pixabay) ($0.00)**:
>    Autonomous scraping of public domain/CC0 ambient video loops filtered for archetype category (luxury estate, artisan culinary, tech abstract, etc.) under 5MB.
> 4. **Tier 4: Free Antigravity Native Image + GPU Ken-Burns Cinema Animation ($0.00)**:
>    Generate an authentic, ultra-high-resolution photograph using the built-in native `generate_image` tool (100% free, zero credit cost) and wrap it in a 60fps GPU-accelerated CSS Ken-Burns infinite animation (`transform: scale(1.1) translate3d(-1%, -1%, 0)` with 20s ease-in-out alternate). Gives 95% of the visual impact of video at 1/10th the bandwidth and $0.00 cost!
> 5. **Tier 5: Procedural WebGL / Three.js Shaders ($0.00)**:
>    Interactive, mathematical canvas shaders for fluid or particle motion that run infinitely with zero video downloads.
>
> *(Optional / Paid Only)*: If and only if the user explicitly authorizes external paid credits, Higgsfield `generate_video` can be invoked via `call_mcp_tool(ServerName="higgsfield", ToolName="generate_video", Arguments={...})`.

### 3.3 Scraping & Downloading Video Loops from Benchmarks
To harvest existing video assets using Playwright Chromium:
1. **DOM Video Detection**: Query `document.querySelectorAll('video, video source')` to extract direct `.mp4` and `.webm` URLs.
2. **Download & Size Optimization**: Download video files and verify payload size:
   - **Hero Background Videos**: Must be **< 3MB** (maximum 5MB) with resolution $1920\times 1080$ or $1280\times 720$.
   - **Compression Rule**: Use H.264 / AAC encoding with high compression (`crf=26`) to eliminate buffering on mobile 4G networks.
3. **Poster Extraction**: Capture the first frame of the video as a still `.jpg` poster for instant FCP and LCP optimization.

### 3.4 Production Frontend Video Embedding (Vercel Standards)
Always embed looping videos using this exact accessible, responsive markup:

```html
<div class="relative w-full h-[70vh] min-h-[500px] overflow-hidden bg-black">
  <!-- Poster Image Fallback (Prevents CLS & LCP delay) -->
  <picture>
    <source srcset="/assets/hero_video_safari.mp4" type="video/mp4" media="(prefers-reduced-motion: no-preference)" />
    <img 
      src="/assets/hero_poster.jpg" 
      alt="Atmospheric morning view of the retreat grounds" 
      class="absolute inset-0 w-full h-full object-cover" 
      fetchpriority="high"
      width="1920" 
      height="1080" 
    />
  </picture>

  <!-- High-Performance Looping Video -->
  <video 
    autoplay 
    muted 
    loop 
    playsinline 
    poster="/assets/hero_poster.jpg" 
    class="absolute inset-0 w-full h-full object-cover transition-opacity duration-700"
    aria-hidden="true"
  >
    <source src="/assets/hero_loop.mp4" type="video/mp4" />
    <source src="/assets/hero_loop.webm" type="video/webm" />
  </video>

  <!-- Gradient Overlay for Readable Text -->
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

  <!-- Accessible Motion Pause Button -->
  <button 
    id="video-toggle-btn"
    aria-label="Pause background video"
    class="absolute bottom-6 right-6 z-20 p-2.5 rounded-full bg-black/40 backdrop-blur-md text-white border border-white/20 hover:bg-black/60 transition"
  >
    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
      <rect x="6" y="4" width="4" height="16"></rect>
      <rect x="14" y="4" width="4" height="16"></rect>
    </svg>
  </button>
</div>
```

### 3.5 Forensic User Asset Curation & Keyframe Extraction (`curate_user_assets.py`)
When the user selects **Hybrid** or **User-Provided Assets** in Stage 0:
1. The AI runs `curate_user_assets.py --mode hybrid --user-dir user_assets`:
   - Scans user files (`.mp4`, `.mov`, `.jpg`, `.png`, `.webp`).
   - Uses Pillow to probe dimensions and aspect ratios (16:9 landscape, 1:1 square, 4:5/9:16 portrait).
   - Uses `ffmpeg` to probe video fps, duration, and extracts:
     - `*_first_frame.jpg` (used as video poster and LCP anchor).
     - `*_mid_frame.jpg` (preview snapshot).
     - `*_last_frame.jpg` (loop continuity check).
2. Generates `public/assets/unified_curation_manifest.json` mapping each file to its optimal section (`Section01Hero`, `Section02Story`, `Section04Accommodations`, `Section05Gastronomy`).

### 3.6 Vision Inspection Protocol (AI Media Forensic Audit)
The AI does NOT guess image content. It uses the `view_file` tool to inspect each user-supplied photo or extracted video frame:
1. **Subject Detection**: Identifies whether the image portrays exterior architecture, dining/food, bedroom suites, pool/gardens, or staff/hosts.
2. **Angle & Framing Assessment**:
   - Is it a wide horizontal vista (16:9)? -> Candidate for Hero or Full-Bleed Intermission.
   - Is it a tight vertical shot (4:5 or 9:16)? -> Candidate for Accommodations Card or Mobile Reel.
   - Is the video shaky or poorly angled? -> Flagged for AI generation / replacement.
3. **Lighting & Texture Quality**: Checks exposure, natural contrast, and architectural alignment.

### 3.7 Frame-Directed Video Creation & Generation Protocol
If a hero video loop is missing or the user video has an awkward camera angle:
1. **Higgsfield `generate_video` (When Authorized)**:
   - Provide the extracted `*_first_frame.jpg` (or generated high-res keyframe) as `role: "image"` in `medias`.
   - Specify camera direction: `"Slow cinematic forward drone push over the grounds at sunrise, calm water ripples, natural golden light, 4k ultra-high-definition, ambient seamless loop"`.
   - Set `aspect_ratio: "16:9"`, `duration: 5`.
2. **Zero-Credit 60fps GPU Ken-Burns Pan (Default Free Fallback)**:
   - Take the highest-resolution still photograph (`=s1600` or user photo).
   - Apply CSS class `animate-ken-burns` with 60fps GPU compositor acceleration:
     ```css
     @keyframes ken-burns {
       0% { transform: scale(1) translate3d(0, 0, 0); }
       50% { transform: scale(1.08) translate3d(-1%, -1%, 0); }
       100% { transform: scale(1) translate3d(0, 0, 0); }
     }
     .animate-ken-burns {
       animation: ken-burns 22s ease-in-out infinite alternate;
       will-change: transform;
     }
     ```
   - Delivers stunning, continuous cinematic visual immersion at **$0.00 cost** and zero layout shift!

---

## 4. Google Maps & Pinterest High-Resolution Scraping Protocols

### 4.1 Google Maps Full-Resolution Scraping (`=s1600`)
* **Endpoint Mechanism**: Google Maps place photos are served from `lh5.googleusercontent.com/p/...=w400-h300-k-no`.
* **Resolution Upgrade Rule**: By replacing `=w...-h...` with **`=s1600`** or **`=s2400`**, Google's CDN delivers the full-resolution uncompressed master photograph uploaded by the owner or photographer at zero cost.
* **Harvesting Script Command**:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source maps --query "<Google_Maps_URL>" --out assets/
  ```

### 4.2 Pinterest Editorial Board Scraping (`/736x/`)
* **Endpoint Mechanism**: Pinterest image URLs follow the pattern `https://i.pinimg.com/{size}/{hash}.jpg`.
* **Resolution Upgrade Rule**: By rewriting thumbnail URLs (`/236x/` or `/474x/`) to **`/736x/`** or **`/originals/`**, the script downloads editorial publication-grade photographs.
* **File Size Filter**: Images `< 35KB` are automatically skipped to eliminate blurry icons and empty tracking pixels.
* **Harvesting Script Command**:
  ```bash
  python "C:/Users/anbua/.gemini/config/skills/website-architect/scripts/harvest_assets.py" --source pinterest --query "<query>" --out assets/ --max 4 --category luxury
  ```

---

## 5. Pre-Delivery Asset Verification Checklist

Before finalizing any frontend build:
- [ ] Every image has explicit `width` and `height` (or aspect-ratio) to ensure **$CLS < 0.05$**.
- [ ] Single Signature Hero image has `fetchpriority="high"` and `loading="eager"`.
- [ ] All below-the-fold images have `loading="lazy"`.
- [ ] No cartoon 3D AI renders used for real-world physical businesses.
- [ ] Background videos are `< 5MB`, muted, loopable, and provide a still poster fallback.
- [ ] Video pause button provided and `@media (prefers-reduced-motion: reduce)` respected.
- [ ] All media mapped 1:1 to sections in the Authoritative Asset Manifest Table.
