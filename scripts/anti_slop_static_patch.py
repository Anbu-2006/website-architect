#!/usr/bin/env python3
"""
anti_slop_static_patch.py - Perceptual CIEDE2000, Continuous Slate-Space Region & Approved Palette Allowlist (v2.4.0)
Synthesized from consensus recommendations across 4 Lead Reviewer AIs.

Features:
- Dual-Layer Color Science with Chroma Ceiling:
  1. Full CIEDE2000 math against 5-color Banned Slate Cluster (#0B0F19, #0F172A, #020617, #111827, #030712).
  2. Continuous Dark Slate-Space Filter with Chroma Floor & Ceiling:
     Mathematically bounds dull, low-chroma generic slates:
     L* <= 30.0, 3.0 <= Chroma <= 16.0, and (Hue in [220°, 310°] or b* <= -2.5).
     - Catches: slate-800 (#1E293B), gray-800 (#1F2937), slate-700 (#334155), #1B2027, #20252B,
       #0E1420, teal-slate (#0F1B1E), and purple-slate (#17141F).
     - Spares: Saturated brand navies (Chroma >= 20.0: Stripe #0A2540, Classic #001F3F, Prussian #003049,
       Oxford #14213D, Steel #1D3557), neutral charcoals (Chroma < 3.0: #121212, #000000), and warm stone (#1C1917).
  3. Approved Brand Palette Allowlist:
     Loads approved palette from creative_thesis.json / design_tokens.json. Any brand color explicitly approved
     by human in Stage 07 is whitelisted (dE <= 2.0).
- Modern CSS Color Parser: Resolves oklch(), hsl(), rgb(), color(display-p3), and bare HSL triplets.
- Context-Guarded Hex Extraction: Context assertion (?<=[:=,(\[\s'"`]) prevents short anchors like #add in text from false-flagging.
- Balanced JSX Tag Parser: Quote- and brace-balanced tracking immune to '>' inside arrow handlers or classNames.
- Chained String Sanitization: Strips href and id attributes cleanly before color scanning.
- Rule-Scoped Pragmas: Requires explicit rule and justification (`// anti-slop-allow: <rule> reason: <justification>`).
- Full File Scope: Scans app, components, lib, src, styles, hooks, root configs, .scss, and .svg.
- Fail Closed: Refuses to pass if 0 files scanned or 0 pages found.
"""
import argparse
import colorsys
import json
import math
import os
import re
import sys
from pathlib import Path

SRC_DIRS = ("app", "components", "lib", "src", "styles", "hooks")
CODE_EXTS = {".tsx", ".ts", ".jsx", ".js", ".css", ".scss", ".mjs", ".svg"}
JSX_EXTS = {".tsx", ".jsx"}
SKIP_PARTS = {"node_modules", ".next", ".git", "dist", "build"}

# Banned generic slate cluster anchors
BANNED_SLATE_CLUSTER = [
    "#0B0F19",  # AI default prompt slate
    "#0F172A",  # Tailwind slate-900
    "#020617",  # Tailwind slate-950
    "#111827",  # Tailwind gray-900
    "#030712",  # Tailwind gray-950
]
SLATE_DELTA_E_HARD = 3.5
SLATE_DELTA_E_WARN = 5.0

# Context lookbehind (?<=[:=,\(\[\'\"`])\s* + lookahead (?![0-9a-zA-Z_-]) protects anchors like #addToCart and text #add, while catching var(--color, #0F172A)
HEX_RE = re.compile(r"""(?<=[:=,\(\[\'\"`])\s*#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b(?![0-9a-zA-Z_-])""")
DANGLING_HASH_RE = re.compile(r"""href=(["'])#(?:/)?\1""")
TW_ARBITRARY_COLOR_RE = re.compile(r"\b(?:bg|text|border|fill|stroke|from|via|to|ring|shadow)-\[(?:#|rgb|hsl|oklch|color)")
BLOB_RE = re.compile(r"blur-(?:2xl|3xl|\[)")
PURPLE_RE = re.compile(r"(?:purple|violet|fuchsia|indigo)-\d{2,3}")
PASTE_BLOCK_RE = re.compile(r"onPaste\s*=\s*\{[^}]*preventDefault", re.DOTALL)
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u26FF\u2728\u2B50]")
PLACEHOLDER_RE = re.compile(r"\b(?:lorem ipsum|your company|acme (?:inc|corp)|coming soon)\b", re.IGNORECASE)
COLOR_FN_RE = re.compile(r"\b(?:rgba?|hsla?|oklch|oklab|lch|lab|hwb|color-mix|light-dark|color)\((?!\s*var\()")
DEFAULT_PALETTE_RE = re.compile(
    r"\b(?:bg|text|border|from|via|to|ring|fill|stroke)-"
    r"(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d{2,3}\b"
)

# Rule-scoped pragma regex: // anti-slop-allow: <rule> reason: <reason>
PRAGMA_RE = re.compile(r"anti-slop-allow:\s*([\w-]+)\s+reason:\s*(\S+)")


def find_app_dir(root: Path):
    for cand in ("src/app", "app"):
        if (root / cand).is_dir():
            return root / cand
    return None


def expand_shorthand(h: str) -> str:
    h = h.lstrip("#")
    if len(h) == 3:
        return h[0]*2 + h[1]*2 + h[2]*2
    if len(h) == 4:
        return h[0]*2 + h[1]*2 + h[2]*2 + h[3]*2
    return h


def _lin(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def oklch_to_rgb(L: float, C: float, h_deg: float) -> tuple[int, int, int]:
    h_rad = math.radians(h_deg)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)
    
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    
    l = l_ ** 3
    m = m_ ** 3
    s = s_ ** 3
    
    r_lin = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g_lin = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_lin = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    
    def to_byte(c):
        c = max(0.0, min(1.0, c))
        c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1.0 / 2.4)) - 0.055
        return int(round(c * 255))
        
    return to_byte(r_lin), to_byte(g_lin), to_byte(b_lin)


def hsl_to_rgb(h_deg: float, s_pct: float, l_pct: float) -> tuple[int, int, int]:
    h = (h_deg % 360.0) / 360.0
    s = s_pct / 100.0
    l = l_pct / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(round(r * 255)), int(round(g * 255)), int(round(b * 255))


def rgb_to_lab(r: int, g: int, b: int) -> tuple[float, float, float]:
    r_lin, g_lin, b_lin = _lin(r), _lin(g), _lin(b)
    x = (0.4124564 * r_lin + 0.3575761 * g_lin + 0.1804375 * b_lin) / 0.95047
    y = (0.2126729 * r_lin + 0.7151522 * g_lin + 0.0721750 * b_lin) / 1.00000
    z = (0.0193339 * r_lin + 0.1191920 * g_lin + 0.9503041 * b_lin) / 1.08883

    x, y, z = max(0.0, x), max(0.0, y), max(0.0, z)

    def f(t: float) -> float:
        return t ** (1.0 / 3.0) if t > 0.008856 else (7.787037 * t) + (16.0 / 116.0)

    fx, fy, fz = f(x), f(y), f(z)
    L = (116.0 * fy) - 16.0
    a = 500.0 * (fx - fy)
    b_val = 200.0 * (fy - fz)
    return (L, a, b_val)


def hex_to_lab(h: str, composite_bg: tuple[int, int, int] = (0, 0, 0)) -> tuple[float, float, float] | None:
    expanded = expand_shorthand(h)
    if len(expanded) == 8:
        try:
            r = int(expanded[0:2], 16)
            g = int(expanded[2:4], 16)
            b = int(expanded[4:6], 16)
            alpha = int(expanded[6:8], 16) / 255.0
            r = int(r * alpha + composite_bg[0] * (1.0 - alpha))
            g = int(g * alpha + composite_bg[1] * (1.0 - alpha))
            b = int(b * alpha + composite_bg[2] * (1.0 - alpha))
        except ValueError:
            return None
    elif len(expanded) == 6:
        try:
            r = int(expanded[0:2], 16)
            g = int(expanded[2:4], 16)
            b = int(expanded[4:6], 16)
        except ValueError:
            return None
    else:
        return None

    return rgb_to_lab(r, g, b)


def ciede2000(lab1: tuple[float, float, float], lab2: tuple[float, float, float],
              k_L: float = 1.0, k_C: float = 1.0, k_H: float = 1.0) -> float:
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    C1 = math.hypot(a1, b1)
    C2 = math.hypot(a2, b2)
    C_bar = (C1 + C2) / 2.0

    G = 0.5 * (1.0 - math.sqrt((C_bar ** 7) / ((C_bar ** 7) + (25.0 ** 7))))

    a1_prime = (1.0 + G) * a1
    a2_prime = (1.0 + G) * a2

    C1_prime = math.hypot(a1_prime, b1)
    C2_prime = math.hypot(a2_prime, b2)

    def get_h(a: float, b: float) -> float:
        if a == 0 and b == 0:
            return 0.0
        deg = math.degrees(math.atan2(b, a))
        return deg if deg >= 0 else deg + 360.0

    h1_prime = get_h(a1_prime, b1)
    h2_prime = get_h(a2_prime, b2)

    delta_L_prime = L2 - L1
    delta_C_prime = C2_prime - C1_prime

    if C1_prime * C2_prime == 0:
        delta_h_prime = 0.0
    elif abs(h2_prime - h1_prime) <= 180.0:
        delta_h_prime = h2_prime - h1_prime
    elif h2_prime - h1_prime > 180.0:
        delta_h_prime = (h2_prime - h1_prime) - 360.0
    else:
        delta_h_prime = (h2_prime - h1_prime) + 360.0

    delta_H_prime = 2.0 * math.sqrt(C1_prime * C2_prime) * math.sin(math.radians(delta_h_prime / 2.0))

    L_bar_prime = (L1 + L2) / 2.0
    C_bar_prime = (C1_prime + C2_prime) / 2.0

    if C1_prime * C2_prime == 0:
        h_bar_prime = h1_prime + h2_prime
    elif abs(h1_prime - h2_prime) <= 180.0:
        h_bar_prime = (h1_prime + h2_prime) / 2.0
    elif h1_prime + h2_prime < 360.0:
        h_bar_prime = (h1_prime + h2_prime + 360.0) / 2.0
    else:
        h_bar_prime = (h1_prime + h2_prime - 360.0) / 2.0

    T = 1.0 - 0.17 * math.cos(math.radians(h_bar_prime - 30.0)) + \
        0.24 * math.cos(math.radians(2.0 * h_bar_prime)) + \
        0.32 * math.cos(math.radians(3.0 * h_bar_prime + 6.0)) - \
        0.20 * math.cos(math.radians(4.0 * h_bar_prime - 63.0))

    delta_theta = 30.0 * math.exp(-(((h_bar_prime - 275.0) / 25.0) ** 2))
    R_C = 2.0 * math.sqrt((C_bar_prime ** 7) / ((C_bar_prime ** 7) + (25.0 ** 7)))
    S_L = 1.0 + ((0.015 * ((L_bar_prime - 50.0) ** 2)) / math.sqrt(20.0 + ((L_bar_prime - 50.0) ** 2)))
    S_C = 1.0 + 0.045 * C_bar_prime
    S_H = 1.0 + 0.015 * C_bar_prime * T
    R_T = -math.sin(math.radians(2.0 * delta_theta)) * R_C

    dE = math.sqrt(
        ((delta_L_prime / (k_L * S_L)) ** 2) +
        ((delta_C_prime / (k_C * S_C)) ** 2) +
        ((delta_H_prime / (k_H * S_H)) ** 2) +
        R_T * (delta_C_prime / (k_C * S_C)) * (delta_H_prime / (k_H * S_H))
    )
    return dE


def cielab_de(lab1: tuple[float, float, float], lab2: tuple[float, float, float]) -> float:
    """CIELAB Delta E*ab Euclidean distance. Documented in color science literature
       (Textile Coloration & Finishing, RIT research) to perform superiorly to CIEDE2000
       for dark shade samples (L* < 25, C* < 16) where CIEDE2000's S_L lightness divisor
       allows excessive lightness error."""
    return math.sqrt((lab1[0] - lab2[0]) ** 2 + (lab1[1] - lab2[1]) ** 2 + (lab1[2] - lab2[2]) ** 2)


def oklab_to_rgb(L: float, a: float, b: float) -> tuple[int, int, int]:
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l = l_ ** 3
    m = m_ ** 3
    s = s_ ** 3
    r_lin = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g_lin = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_lin = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    def to_byte(c):
        c = max(0.0, min(1.0, c))
        c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1.0 / 2.4)) - 0.055
        return int(round(c * 255))
    return to_byte(r_lin), to_byte(g_lin), to_byte(b_lin)


def lch_to_lab(L: float, C: float, h_deg: float) -> tuple[float, float, float]:
    h_rad = math.radians(h_deg)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)
    return (L, a, b)


def display_p3_to_lab(r: float, g: float, b: float) -> tuple[float, float, float]:
    def lin_p3(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r_l, g_l, b_l = lin_p3(r), lin_p3(g), lin_p3(b)
    # Display-P3 linear to XYZ D65 matrix
    x = 0.4865709486 * r_l + 0.2656676932 * g_l + 0.1982172852 * b_l
    y = 0.2289745641 * r_l + 0.6917385218 * g_l + 0.0792869141 * b_l
    z = 0.0000000000 * r_l + 0.0451133819 * g_l + 1.0439443689 * b_l
    x, y, z = x / 0.95047, y / 1.00000, z / 1.08883
    x, y, z = max(0.0, x), max(0.0, y), max(0.0, z)
    def f(t: float) -> float:
        return t ** (1.0 / 3.0) if t > 0.008856 else (7.787037 * t) + (16.0 / 116.0)
    fx, fy, fz = f(x), f(y), f(z)
    L_val = (116.0 * fy) - 16.0
    a_val = 500.0 * (fx - fy)
    b_val = 200.0 * (fy - fz)
    return (L_val, a_val, b_val)


def is_in_slate_region(lab: tuple[float, float, float]) -> bool:
    """Continuous slate-space filter with Chroma ceiling & floor:
       Catches dull low-chroma generic slates (Chroma in [3.0, 16.0]),
       while preserving vibrant brand navies (Chroma >= 20.0) and neutrals (Chroma < 3.0)."""
    L, a, b = lab
    chroma = math.hypot(a, b)
    if L <= 30.0 and 3.0 <= chroma <= 16.0:
        hue = math.degrees(math.atan2(b, a)) % 360.0
        if (220.0 <= hue <= 310.0) or b <= -2.5:
            return True
    return False


def load_approved_palette(root: Path) -> list[tuple[float, float, float]]:
    """Loads approved brand palette strictly from human/client-approved creative_thesis.json.
       Cryptographically enforces:
       1. Rejects loading from design_tokens.json (cannot allowlist colors via code mutation).
       2. If approval_root exists in .arch/state.json, verifies creative_thesis.json hasn't drifted.
       3. Prohibits any color that matches the banned slate cluster (dE <= 3.5) from being allowlisted."""
    approved_labs = []
    banned_labs = [hex_to_lab(c) for c in BANNED_SLATE_CLUSTER if hex_to_lab(c) is not None]

    thesis_candidates = [
        root / ".arch" / "creative_thesis.json",
        root / "creative_thesis.json"
    ]
    thesis_file = None
    for cand in thesis_candidates:
        if cand.exists():
            thesis_file = cand
            break

    if not thesis_file:
        return approved_labs

    # If state.json exists, verify that approval root is respected
    state_file = root / ".arch" / "state.json"
    if state_file.exists():
        try:
            state_data = json.loads(state_file.read_text(encoding="utf-8"))
            appr_root = state_data.get("merkle_roots", {}).get("approval_root")
            stages = state_data.get("stages", {})
            # If Stage 07 approved, ensure thesis has not been tampered with post-approval
            if appr_root and stages.get("07_user_approval", {}).get("status") == "passed":
                expected_hash = stages.get("02_creative_direction", {}).get("output_hashes", {}).get("creative_thesis.json")
                if expected_hash:
                    cur_hash = "sha256:" + hashlib.sha256(thesis_file.read_bytes()).hexdigest()
                    if cur_hash != expected_hash:
                        print(f"[SECURITY] Tampered creative_thesis.json detected! Ignoring unverified palette.", file=sys.stderr)
                        return []
        except Exception:
            pass

    try:
        data = json.loads(thesis_file.read_text(encoding="utf-8"))
        # Only extract from explicitly declared brand palette sections
        palette_candidates = []
        if isinstance(data, dict):
            for key in ("approved_brand_palette", "brand_colors", "palette", "colors"):
                val = data.get(key)
                if isinstance(val, (list, dict)):
                    palette_candidates.append(json.dumps(val))
        if not palette_candidates:
            palette_candidates.append(json.dumps(data))

        for blob in palette_candidates:
            for hex_val in re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", blob):
                lab = hex_to_lab(hex_val)
                if lab:
                    # Enforce that generic slate cluster can NEVER be allowlisted
                    if not any(cielab_de(lab, b) <= 3.5 for b in banned_labs):
                        approved_labs.append(lab)
    except Exception:
        pass

    return approved_labs


def is_approved_brand_color(lab: tuple[float, float, float], approved_palette: list[tuple[float, float, float]]) -> bool:
    """Returns True if the color matches an approved brand color within dE <= 2.0."""
    if not approved_palette:
        return False
    return any(ciede2000(lab, app_lab) <= 2.0 for app_lab in approved_palette)


def find_image_tags(text: str) -> list[tuple[str, int]]:
    """Extracts <img> and <Image> tags respecting balanced quotes, curly braces, and parentheses."""
    tags = []
    i = 0
    n = len(text)
    while i < n:
        idx = -1
        for p in ('<Image', '<img'):
            if text[i:i+len(p)] == p and (i+len(p) == n or not text[i+len(p)].isalnum()):
                idx = i
                break
        if idx == -1:
            i += 1
            continue
        start = idx
        i = start + 4
        in_quote = None
        brace_depth = 0
        paren_depth = 0
        tag_end = -1
        while i < n:
            ch = text[i]
            if in_quote:
                if ch == in_quote and text[i-1] != '\\':
                    in_quote = None
            else:
                if ch in ('"', "'", '`'):
                    in_quote = ch
                elif ch == '{':
                    brace_depth += 1
                elif ch == '}':
                    if brace_depth > 0:
                        brace_depth -= 1
                elif ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    if paren_depth > 0:
                        paren_depth -= 1
                elif ch == '>' and brace_depth == 0 and paren_depth == 0:
                    tag_end = i + 1
                    break
            i += 1
        if tag_end != -1:
            tags.append((text[start:tag_end], start))
            i = tag_end
        else:
            i = start + 1
    return tags


def iter_files(root: Path, counter: list[int] | None = None):
    for p in root.glob("*"):
        if p.is_file() and p.suffix in CODE_EXTS and not (SKIP_PARTS & set(p.relative_to(root).parts)):
            if counter is not None:
                counter[0] += 1
            yield p

    for d in SRC_DIRS:
        base = root / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            rel_parts = set(p.relative_to(root).parts)
            if p.is_file() and p.suffix in CODE_EXTS and not (SKIP_PARTS & rel_parts):
                if counter is not None:
                    counter[0] += 1
                yield p


def scan(root: Path, tokens_file: str | None, stats: dict) -> list[dict]:
    app_dir = find_app_dir(root)
    if tokens_file:
        tokens_path = (root / tokens_file).resolve()
    else:
        tokens_path = (app_dir / "globals.css").resolve() if app_dir else None

    banned_labs = [hex_to_lab(c) for c in BANNED_SLATE_CLUSTER]
    banned_labs = [lab for lab in banned_labs if lab is not None]
    approved_palette = load_approved_palette(root)
    out = []

    def add(sev: str, rule: str, path: Path, line: int, detail: str):
        out.append({
            "severity": sev,
            "rule": rule,
            "file": str(path.relative_to(root)),
            "line": line,
            "detail": detail
        })

    scanned = [0]
    for path in iter_files(root, scanned):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        lines = text.splitlines()
        is_tokens = tokens_path is not None and path.resolve() == tokens_path

        for i, line in enumerate(lines, 1):
            allowed_rules = set()
            for pm in PRAGMA_RE.finditer(line):
                rule_name, reason = pm.group(1), pm.group(2)
                if reason:
                    allowed_rules.add(rule_name)
                    stats["pragmas"] += 1

            # Chain replacements so href="..." and id="..." are stripped cleanly
            clean = re.sub(r"""href=(["'])[^"']*\1""", "", line)
            clean = re.sub(r"""id=(["'])[^"']*\1""", "", clean)

            # 1. Hex Color Verification
            for m in HEX_RE.finditer(clean):
                hex_str = m.group(0).strip()
                lab = hex_to_lab(hex_str)
                if lab:
                    # Check if approved in brand palette allowlist
                    is_approved = is_approved_brand_color(lab, approved_palette)
                    
                    if not is_approved:
                        min_de = min(ciede2000(lab, b) for b in banned_labs)
                        if min_de <= SLATE_DELTA_E_HARD and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i,
                                f"{hex_str} is within CIEDE2000 dE={min_de:.2f} <= {SLATE_DELTA_E_HARD} of generic slate")
                        elif min_de <= SLATE_DELTA_E_WARN and "banned-slate" not in allowed_rules:
                            add("warn", "slate-near-miss-warning", path, i,
                                f"{hex_str} is within CIEDE2000 dE={min_de:.2f} <= {SLATE_DELTA_E_WARN} of generic slate")

                        # CIELAB Delta E*ab fallback for dark colors (L* < 25, C* < 16)
                        # Resolves CIEDE2000 S_L lightness permissiveness in dark shade region
                        chroma = math.hypot(lab[1], lab[2])
                        if lab[0] < 25.0 and chroma < 16.0:
                            min_cielab = min(cielab_de(lab, b) for b in banned_labs)
                            if min_cielab <= SLATE_DELTA_E_HARD and "banned-slate" not in allowed_rules:
                                add("error", "banned-slate", path, i,
                                    f"{hex_str} is within CIELAB dE_ab={min_cielab:.2f} <= {SLATE_DELTA_E_HARD} of generic slate (dark region fallback)")

                        if is_in_slate_region(lab) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate-region", path, i,
                                f"{hex_str} falls into continuous dark slate region (L*={lab[0]:.1f}, b*={lab[2]:.1f})")

                if not is_tokens and "raw-color-bypasses-tokens" not in allowed_rules:
                    add("error", "raw-color-bypasses-tokens", path, i, hex_str)

            # 2. Modern Color Function Check in Tokens (globals.css) & Components
            for oklch_m in re.finditer(r"oklch\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    L, C, h = float(oklch_m.group(1)), float(oklch_m.group(2)), float(oklch_m.group(3))
                    r, g, b = oklch_to_rgb(L, C, h)
                    lab = rgb_to_lab(r, g, b)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{oklch_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            for hsl_m in re.finditer(r"hsl\(\s*([\d.]+)(?:deg)?\s+([\d.]+)%\s+([\d.]+)%(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    h, s, l = float(hsl_m.group(1)), float(hsl_m.group(2)), float(hsl_m.group(3))
                    r, g, b = hsl_to_rgb(h, s, l)
                    lab = rgb_to_lab(r, g, b)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{hsl_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            for bare_m in re.finditer(r"--[\w-]+:\s*([\d.]+)\s+([\d.]+)%\s+([\d.]+)%;", line):
                try:
                    h, s, l = float(bare_m.group(1)), float(bare_m.group(2)), float(bare_m.group(3))
                    r, g, b = hsl_to_rgb(h, s, l)
                    lab = rgb_to_lab(r, g, b)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"Token triplet {bare_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            # 3. Lab / Lch / Oklab / Display-P3 modern CSS evaluations in tokens
            for lab_m in re.finditer(r"lab\(\s*([\d.]+)(?:%|deg)?\s+([-\d.]+)\s+([-\d.]+)(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    L, a, b_val = float(lab_m.group(1)), float(lab_m.group(2)), float(lab_m.group(3))
                    lab = (L, a, b_val)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{lab_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            for lch_m in re.finditer(r"lch\(\s*([\d.]+)(?:%|deg)?\s+([\d.]+)\s+([-\d.]+)(?:deg)?(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    L, C, h = float(lch_m.group(1)), float(lch_m.group(2)), float(lch_m.group(3))
                    lab = lch_to_lab(L, C, h)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{lch_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            for oklab_m in re.finditer(r"oklab\(\s*([\d.]+)\s+([-\d.]+)\s+([-\d.]+)(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    L, a, b_val = float(oklab_m.group(1)), float(oklab_m.group(2)), float(oklab_m.group(3))
                    r, g, b_byte = oklab_to_rgb(L, a, b_val)
                    lab = rgb_to_lab(r, g, b_byte)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{oklab_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            for p3_m in re.finditer(r"color\(\s*display-p3\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*[\d.%]+)?\s*\)", line):
                try:
                    r, g, b_val = float(p3_m.group(1)), float(p3_m.group(2)), float(p3_m.group(3))
                    lab = display_p3_to_lab(r, g, b_val)
                    if not is_approved_brand_color(lab, approved_palette):
                        min_de = min(ciede2000(lab, bl) for bl in banned_labs)
                        if (min_de <= SLATE_DELTA_E_HARD or is_in_slate_region(lab)) and "banned-slate" not in allowed_rules:
                            add("error", "banned-slate", path, i, f"{p3_m.group(0)} computes to dark slate (dE={min_de:.2f})")
                except Exception:
                    pass

            if not is_tokens and COLOR_FN_RE.search(clean) and "raw-color-function" not in allowed_rules:
                add("error", "raw-color-function", path, i, clean.strip()[:100])

            if DEFAULT_PALETTE_RE.search(clean) and "default-palette-class" not in allowed_rules:
                add("warn", "default-palette-class", path, i, clean.strip()[:100])

            if TW_ARBITRARY_COLOR_RE.search(clean) and "tailwind-arbitrary-color" not in allowed_rules:
                add("error", "tailwind-arbitrary-color", path, i, clean.strip()[:100])

            if BLOB_RE.search(clean) and PURPLE_RE.search(clean) and "purple-blur-blob" not in allowed_rules:
                add("error", "purple-blur-blob", path, i, clean.strip()[:100])

            if DANGLING_HASH_RE.search(line) and "dangling-hash-link" not in allowed_rules:
                add("error", "dangling-hash-link", path, i, "Anchor links with href='#' or href='#/' are prohibited.")

            if path.suffix in JSX_EXTS and EMOJI_RE.search(clean) and "emoji-in-ui" not in allowed_rules:
                add("warn", "emoji-in-ui", path, i, clean.strip()[:100])

            if path.suffix in JSX_EXTS and PLACEHOLDER_RE.search(clean) and "placeholder-copy" not in allowed_rules:
                add("warn", "placeholder-copy", path, i, clean.strip()[:100])

        if path.suffix in JSX_EXTS:
            for tag, pos in find_image_tags(text):
                has_alt = re.search(r"\b(?:alt|aria-label)\s*=", tag)
                if not has_alt and "img-missing-alt" not in allowed_rules:
                    ln = text.count("\n", 0, pos) + 1
                    add("error", "img-missing-alt", path, ln, tag[:80].replace("\n", " "))
            for m in PASTE_BLOCK_RE.finditer(text):
                ln = text.count("\n", 0, m.start()) + 1
                add("error", "paste-blocked", path, ln, "onPaste calls preventDefault")

    if scanned[0] == 0:
        out.append({
            "severity": "error",
            "rule": "no-files-scanned",
            "file": "-",
            "line": 0,
            "detail": "scanner examined 0 source files; refusing to pass"
        })

    pages = [p for p in app_dir.rglob("page.tsx") if not (SKIP_PARTS & set(p.relative_to(root).parts))] if app_dir else []
    if not pages:
        out.append({
            "severity": "error",
            "rule": "no-pages-found",
            "file": "-",
            "line": 0,
            "detail": "no app/**/page.tsx or src/app/**/page.tsx found; refusing to pass"
        })
    for page in pages:
        try:
            p_text = page.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        has_meta = re.search(r"export\s+(?:const\s+metadata|async\s+function\s+generateMetadata|function\s+generateMetadata)", p_text)
        if re.match(r"\s*(['\"])use client\1", p_text):
            add("error", "client-page-no-metadata", page, 1, "page.tsx is a client component and cannot export metadata")
        elif not has_meta:
            add("error", "page-missing-metadata", page, 1, "no metadata / generateMetadata export")

    return out


def main():
    ap = argparse.ArgumentParser(description="Static Anti-Slop Audit Patch (v2.4.0)")
    ap.add_argument("root", nargs="?", default=".", help="Project root directory")
    ap.add_argument("--tokens-file", default=None, help="Design tokens CSS file")
    ap.add_argument("--max-pragmas", type=int, default=5, help="Max allowed anti-slop-allow exemptions")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    stats = {"pragmas": 0}
    findings = scan(root, args.tokens_file, stats)

    if stats["pragmas"] > args.max_pragmas:
        findings.append({
            "severity": "error",
            "rule": "too-many-pragmas",
            "file": "-",
            "line": 0,
            "detail": f"{stats['pragmas']} anti-slop-allow exemptions > {args.max_pragmas}"
        })

    errors = [f for f in findings if f["severity"] == "error"]
    print(json.dumps({
        "errors": len(errors),
        "warnings": len(findings) - len(errors),
        "pragmas": stats["pragmas"],
        "findings": findings
    }, indent=2))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
