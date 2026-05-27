#!/usr/bin/env python3
# Design System HTML Generator — A4 Landscape, 2 Pages per Brand
# v7: playwright 제거, HTML+웹폰트 방식으로 전환
#
# 사용법 (스킬에서 호출 시):
# sys.path.insert(0, skill_scripts_path)
#   from generate_ds_pdf import generate_pdfs
#   asyncio.run(generate_pdfs(fonts_dir=..., out_dir=..., brands=[(config, 'name.pdf')]))

import os

# ── 전역 상수 (경로 아님) ──────────────────────────────────────────────────
# 타입 스케일 행 고정 높이 (Display → Caption 순서, 어떤 폰트든 동일 구조 보장)
ROW_HEIGHTS_MM = [11, 9, 8, 7.5, 7, 6.5, 6]

PAGE2_MARKER = '<!-- ═══════ PAGE 2 : IN USE ═══════ -->'

# ── 유틸 함수 ──────────────────────────────────────────────────────────────

def find_font(font_name_hint, fonts_dir, weight='regular'):
    """fonts_dir 하위에서 폰트 파일을 재귀 탐색해 절대경로 반환.

    우선순위:
      1. Variable TTF  (*Variable*, *wght* 포함)
      2. Regular TTF
      3. Regular OTF
      4. Medium/기타 TTF → OTF 순

    weight='bold' 시 Bold/700/Heavy 키워드 먼저 탐색.
    찾지 못하면 None 반환 (호출자가 fallback 처리).
    """
    import glob as _glob

    if not fonts_dir or not os.path.isdir(fonts_dir):
        return None

    name_lower = (font_name_hint or '').lower().replace(' ', '')

    # 후보 파일 수집 (재귀, .ttf + .otf)
    ttf_files = _glob.glob(os.path.join(fonts_dir, '**', '*.ttf'), recursive=True)
    otf_files = _glob.glob(os.path.join(fonts_dir, '**', '*.otf'), recursive=True)
    all_files = ttf_files + otf_files

    # 폰트명 힌트로 필터 (힌트 없으면 전체 사용)
    if name_lower:
        filtered = [f for f in all_files if name_lower in os.path.basename(f).lower().replace(' ', '').replace('-', '').replace('_', '')]
        if not filtered:
            filtered = all_files  # 힌트 매칭 실패 → 전체 fallback
    else:
        filtered = all_files

    if not filtered:
        return None

    def score(path):
        bn = os.path.basename(path).lower()
        is_ttf = path.lower().endswith('.ttf')
        is_otf = path.lower().endswith('.otf')

        if weight == 'bold':
            # 명시적 Bold / 700 파일 최우선 (Variable보다 예측 가능)
            if any(k in bn for k in ('bold', '700')) and 'extra' not in bn and 'semi' not in bn:
                if is_ttf: return 10
                if is_otf: return 9
            # ExtraBold / SemiBold
            if any(k in bn for k in ('extrabold', 'semibold')):
                if is_ttf: return 8
                if is_otf: return 7
            # Variable TTF → bold 축 지원 가능, 명시 Bold 없을 때 대체
            if ('variable' in bn or 'wght' in bn) and is_ttf:
                return 6
            # Heavy / Black → 너무 두꺼우므로 낮은 점수
            if any(k in bn for k in ('heavy', 'black')):
                if is_ttf: return 5
                if is_otf: return 4
            # Bold 없으면 Regular로 대체
            if 'regular' in bn and is_ttf:
                return 3
            return 1
        else:
            # Regular 계열 우선
            if 'variable' in bn or 'wght' in bn:
                if is_ttf:
                    return 10
            if 'regular' in bn and is_ttf:
                return 9
            if 'regular' in bn and is_otf:
                return 8
            if 'medium' in bn and is_ttf:
                return 7
            if is_ttf:
                return 5
            if is_otf:
                return 4
            return 1

    best = max(filtered, key=score)
    return best


def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def luminance(hex_color):
    r, g, b = [x/255 for x in hex_to_rgb(hex_color)]
    return 0.299*r + 0.587*g + 0.114*b

def wcag_luminance(hex_color):
    """WCAG 2.1 상대 휘도 (정확한 공식)"""
    def linearize(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = [linearize(x / 255) for x in hex_to_rgb(hex_color)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(c1, c2):
    l1, l2 = wcag_luminance(c1), wcag_luminance(c2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 1)

def wcag_level(ratio):
    if ratio >= 7.0:   return 'AAA', '#1B6B2F', '#D6F0DC'
    if ratio >= 4.5:   return 'AA',  '#1B6B2F', '#D6F0DC'
    if ratio >= 3.0:   return 'AA*', '#7A5200', '#FFF0C2'
    return '✗', '#B71C1C', '#FDECEA'

def make_semantic_section(b, text_sub, border_c):
    """Semantic Alias 토큰 섹션 — col-type 하단용"""
    primary   = b['primary']
    accent    = b['accent']
    text_s    = b['text_sub']
    _nt = b.get('neutral_tints', [])
    _nt_list = list(_nt.values()) if isinstance(_nt, dict) else _nt
    neutral_100 = _nt_list[0] if _nt_list else '#F5F5F5'
    neutral_500 = _nt_list[3] if len(_nt_list) > 3 else (_nt_list[-1] if _nt_list else '#8C8C8C')

    aliases = [
        (primary,      'interactive',   'Primary',     primary),
        (accent,       'destructive',   'Accent',      accent),
        (text_s,       'placeholder',   'Text.Sub',    text_s),
        (neutral_100,  'disabled-bg',   'Neutral-100', neutral_100),
        (neutral_500,  'disabled-text', 'Neutral-500', neutral_500),
    ]

    rows = ''
    for (dot_color, token_name, ref_name, hex_val) in aliases:
        dot_border = f'border:0.25mm solid {border_c};' if dot_color in ('#F5F5F5', '#FFFFFF', '#FAFAFA') else ''
        rows += f'''
        <div style="display:flex;align-items:center;gap:1.5mm;padding:1.5mm 0;border-bottom:0.25mm solid {border_c};">
          <div style="width:3.5mm;height:3.5mm;border-radius:1px;background:{dot_color};flex-shrink:0;{dot_border}"></div>
          <div style="font-size:7pt;font-weight:700;font-family:monospace;color:{text_sub};flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{token_name}</div>
          <div style="font-size:6pt;color:{text_sub};opacity:.7;white-space:nowrap;margin-right:1mm;">→ {ref_name}</div>
          <div style="font-size:6pt;font-family:monospace;color:{text_sub};opacity:.6;white-space:nowrap;">{hex_val}</div>
        </div>'''

    return f'''
    <div>
      {make_sec_title('Semantic Aliases')}
      {rows}
    </div>'''

def make_contrast_section(b, text_sub, border_c):
    """접근성 대비율 섹션 — col-comp 하단용 컴팩트 버전"""
    page_bg  = b['page_bg']
    primary  = b['primary']
    text_main = b['text_main']
    text_caption = b['text_tokens'][2][1] if len(b['text_tokens']) > 2 else '#999999'

    pairs = [
        (text_main,    page_bg,  'Text.Main / Surface'),
        (b['text_sub'], page_bg, 'Text.Sub / Surface'),
        (text_caption, page_bg,  'Caption / Surface'),
        ('#FFFFFF',    primary,  'White / Primary'),
        (text_main,   primary,   'Dark / Primary'),
    ]

    rows = ''
    for (fg, bg, label) in pairs:
        ratio = contrast_ratio(fg, bg)
        level, lvl_color, lvl_bg = wcag_level(ratio)
        rows += f'''
        <div style="display:flex;align-items:center;gap:1.5mm;margin-bottom:2mm;">
          <div style="width:5.5mm;height:5mm;background:{bg};border:0.3mm solid {border_c};border-radius:1px;flex-shrink:0;display:flex;align-items:center;justify-content:center;">
            <div style="width:2.8mm;height:2.8mm;background:{fg};border-radius:0.5px;"></div>
          </div>
          <div style="flex:1;font-size:6.5pt;color:{text_sub};overflow:hidden;white-space:nowrap;text-overflow:ellipsis;">{label}</div>
          <div style="font-size:7pt;font-weight:700;color:{text_sub};white-space:nowrap;">{ratio}</div>
          <div style="font-size:6pt;font-weight:700;padding:0.8mm 2mm;border-radius:3mm;background:{lvl_bg};color:{lvl_color};white-space:nowrap;">{level}</div>
        </div>'''

    return f'''
    <div style="margin-top:1.5mm;">
      <div style="font-size:7pt;color:{text_sub};font-weight:700;letter-spacing:.1em;margin-bottom:2.5mm;text-transform:uppercase;">Accessibility</div>
      {rows}
      <div style="font-size:5.5pt;color:{text_sub};opacity:.65;margin-top:1.5mm;">AA=4.5:1 · AA*=large text only · AAA=7:1</div>
    </div>'''

def make_personality_section(b, text_sub, border_c):
    """섹션 A — 브랜드 퍼스낼리티 (3단어 + 한 줄 설명) — col-comp 상단"""
    items = b.get('personality', [])
    if not items:
        return ''
    primary = b['primary']
    hf = b.get('heading_font', 'sans-serif')
    rows = ''
    for (word, desc) in items:
        rows += f'''
        <div style="display:flex;align-items:baseline;gap:2.5mm;margin-bottom:2.5mm;">
          <div style="font-size:10pt;font-weight:700;color:{primary};white-space:nowrap;font-family:'{hf}','NKR',sans-serif;">{word}</div>
          <div style="font-size:6.5pt;color:{text_sub};opacity:.85;line-height:1.45;flex:1;">{desc}</div>
        </div>'''
    return f'''
    <div style="margin-bottom:2mm;">
      {rows}
    </div>'''


def make_token_hierarchy_section(b, text_sub, border_c):
    """섹션 B — 토큰 계층 다이어그램 (Primitive→Semantic→Alias 플로우) — col-comp"""
    items = b.get('token_hierarchy', [])
    if not items:
        return ''
    rows = ''
    for (prim_hex, prim_name, alias_name, alias_desc) in items:
        dot_border = f'border:0.25mm solid {border_c};' if luminance(prim_hex) > 0.85 else ''
        rows += f'''
        <div style="display:flex;align-items:center;gap:1.5mm;padding:1.5mm 0;border-bottom:0.25mm solid {border_c};">
          <div style="width:3.5mm;height:3.5mm;border-radius:1px;background:{prim_hex};flex-shrink:0;{dot_border}"></div>
          <div style="font-size:6pt;font-family:monospace;color:{text_sub};opacity:.7;white-space:nowrap;width:16mm;overflow:hidden;text-overflow:ellipsis;">{prim_name}</div>
          <div style="font-size:6pt;color:{text_sub};opacity:.5;">→</div>
          <div style="font-size:7pt;font-weight:700;font-family:monospace;color:{text_sub};white-space:nowrap;width:16mm;overflow:hidden;text-overflow:ellipsis;">{alias_name}</div>
          <div style="font-size:6pt;color:{text_sub};opacity:.5;">→</div>
          <div style="font-size:6pt;color:{text_sub};opacity:.8;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">"{alias_desc}"</div>
        </div>'''
    return f'''
    <div style="margin-bottom:1.5mm;">
      {make_sec_title('Token Hierarchy')}
      {rows}
    </div>'''


def make_component_hints_section(b, text_sub, border_c):
    """섹션 D — 컴포넌트 힌트 (Card/Badge/Input 시각화) — PAGE 2 col-right 하단"""
    hints = b.get('component_hints', {})
    if not hints:
        return ''
    primary = b['primary']
    primary_on = on_color(primary)

    card  = hints.get('card',  {})
    badge = hints.get('badge', {})
    inp   = hints.get('input', {})

    # 카드 bg는 브랜드의 Surface.Card 우선 (없으면 page_bg 폴백).
    # 카드가 컬럼 가득 채워서(inset margin 없음) 외곽 안개 문제 회피.
    card_bg     = card.get('bg', b['page_bg'])
    card_radius = card.get('radius', '6px')
    card_border = card.get('border', border_c)
    card_shadow = card.get('shadow', '')

    badge_bg     = badge.get('bg',     b.get('font_badge_bg', '#ECEEFE'))
    badge_text   = badge.get('text',   primary)
    badge_radius = badge.get('radius', '100px')

    inp_border = inp.get('border', border_c)
    inp_radius = inp.get('radius', '4px')
    inp_focus  = inp.get('focus',  primary)

    return f'''
    <div style="margin-top:2mm;">
      {make_sec_title('Component Hints')}

      <!-- Card — 컬럼 가득 채움. Badge/Input의 좌우와 자동 정렬됨.
           box-shadow 없음 (Mac Preview·Chrome 등 뷰어 렌더링 일관성 위해 border만 사용). -->
      <div style="font-size:6.5pt;color:{text_sub};opacity:.75;margin-bottom:2mm;font-weight:700;letter-spacing:.05em;">CARD</div>
      <div style="margin-bottom:4mm;background:{card_bg};border:0.4mm solid {card_border};border-radius:{card_radius};padding:3mm 3.5mm;">
        <div style="width:50%;height:2.5mm;background:{text_sub};border-radius:1mm;margin-bottom:1.8mm;opacity:.4;"></div>
        <div style="width:80%;height:2mm;background:{text_sub};border-radius:1mm;margin-bottom:1.2mm;opacity:.28;"></div>
        <div style="width:60%;height:2mm;background:{text_sub};border-radius:1mm;opacity:.28;"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:2.5mm;">
          <div style="background:{primary};color:{primary_on};font-size:6pt;font-weight:700;padding:1.2mm 3mm;border-radius:8mm;line-height:1;">Action</div>
          <div style="font-size:6pt;color:{text_sub};font-family:monospace;opacity:.6;">{card_radius} · {card_shadow}</div>
        </div>
      </div>

      <!-- Badge + Input -->
      <div style="display:flex;gap:2.5mm;align-items:flex-start;">
        <div style="flex:1;">
          <div style="font-size:6.5pt;color:{text_sub};opacity:.75;margin-bottom:2mm;font-weight:700;letter-spacing:.05em;">BADGE</div>
          <div style="display:flex;flex-wrap:wrap;gap:1.5mm;">
            <div style="background:{badge_bg};color:{badge_text};font-size:7pt;font-weight:700;padding:1.2mm 3mm;border-radius:{badge_radius};line-height:1;white-space:nowrap;">Label</div>
            <div style="background:{primary};color:{primary_on};font-size:7pt;font-weight:700;padding:1.2mm 3mm;border-radius:{badge_radius};line-height:1;white-space:nowrap;">Active</div>
          </div>
        </div>
        <div style="flex:1;">
          <div style="font-size:6.5pt;color:{text_sub};opacity:.75;margin-bottom:2mm;font-weight:700;letter-spacing:.05em;">INPUT</div>
          <div style="border:0.5mm solid {inp_focus};border-radius:{inp_radius};padding:1.8mm 2.5mm;font-size:7pt;color:{text_sub};line-height:1;display:flex;justify-content:space-between;align-items:center;gap:1.5mm;">
            <span style="opacity:.85;">입력하세요...</span>
            <span style="font-family:monospace;opacity:.6;">{inp_focus}</span>
          </div>
        </div>
      </div>
    </div>'''


def on_color(hex_color):
    return '#000000' if luminance(hex_color) > 0.5 else '#FFFFFF'

def make_tint_strip(colors, label, strip_labels=None):
    # strip_labels: 칸 수에 맞는 라벨 리스트. None이면 10칸 기본값(50~900) 사용
    default_labels = ['50','100','200','300','400','500','600','700','800','900']
    lbls = strip_labels if strip_labels else default_labels[:len(colors)]
    # 500 굵게 처리: 10칸 기본 스케일일 때만 index 5에 적용
    base_500_idx = lbls.index('500') if '500' in lbls else -1
    cells = ''
    for i, c in enumerate(colors):
        inset = f'box-shadow:inset 0 0 0 1.5px #fff;' if i == base_500_idx else ''
        cells += f'<div style="flex:1;height:7mm;background:{c};{inset}"></div>'
    label_cells = ''
    for i, lbl in enumerate(lbls):
        fw = 'font-weight:700;' if i == base_500_idx else ''
        label_cells += f'<div style="flex:1;text-align:center;font-size:6pt;{fw}color:{label};opacity:.8;">{lbl}</div>'
    return f'''
    <div style="margin-bottom:2.5mm;">
      <div style="display:flex;border-radius:2px;overflow:hidden;">{cells}</div>
      <div style="display:flex;margin-top:1.2mm;">{label_cells}</div>
    </div>'''

def make_swatch(color, name, desc, text_color, border="none"):
    tc = on_color(color)
    return f'''
    <div style="margin-bottom:2.5mm;">
      <div style="background:{color};border:{border};border-radius:3px;padding:3mm 4mm 2.5mm;height:12mm;display:flex;flex-direction:column;justify-content:space-between;">
        <div style="font-size:9pt;font-weight:700;color:{tc};letter-spacing:.03em;">{name}</div>
        <div style="font-size:7.5pt;font-family:monospace;color:{tc};opacity:.9;">{color}</div>
      </div>
      <div style="font-size:6.5pt;color:{text_color};margin-top:1.2mm;line-height:1.35;">{desc}</div>
    </div>'''

def make_type_row(label, size_token, weight, lh, sample_text, sample_size_pt, text_color, border_color, row_height_mm, font_override=None):
    font_style = f"font-family:'{font_override}','NKR',sans-serif;" if font_override else ''
    return f'''
    <div style="min-height:{row_height_mm}mm;padding:1.8mm 0;border-bottom:0.15mm solid {border_color};display:flex;align-items:center;overflow:hidden;">
      <div style="display:flex;justify-content:space-between;align-items:baseline;width:100%;">
        <div style="{font_style}font-size:{sample_size_pt}pt;font-weight:{weight};color:{text_color};line-height:1.1;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;flex:1;">{sample_text}</div>
        <div style="font-size:6pt;font-family:monospace;color:{text_color};opacity:.55;white-space:nowrap;margin-left:3mm;flex-shrink:0;">{size_token}px · {weight} · {lh}</div>
      </div>
    </div>'''

def make_radius_row(name, radius_val, primary, label_color):
    br = radius_val if radius_val != '100px' else '20mm'
    return f'''
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2.5mm;">
      <div style="width:20mm;height:7mm;background:{primary};border-radius:{br};"></div>
      <div style="font-size:7pt;color:{label_color};text-align:right;line-height:1.3;">{name}<br><span style="font-family:monospace;opacity:.75;font-size:6pt;">{radius_val}</span></div>
    </div>'''

def make_button(label, bg, text, border_style, radius="20mm", font_family='sans-serif'):
    return (
        f'<div style="background:{bg};border:{border_style};border-radius:{radius};'
        f'padding:0 5mm;height:6.5mm;line-height:6.5mm;'
        f'display:inline-block;text-align:center;vertical-align:middle;'
        f'margin-right:2mm;margin-bottom:1.5mm;'
        f"font-family:'{font_family}','NKR',sans-serif;"
        f'font-size:6pt;font-weight:700;color:{text};white-space:nowrap;">'
        f'{label}</div>'
    )

def make_sec_title(label):
    """서브 섹션 타이틀을 sec-title 클래스로 생성.
    컬럼 헤더(col-title)보다 작고 가볍게 — 뎁스 2 서브 섹션 전용.
    스타일 변경 시 CSS의 .sec-title 한 곳만 수정하면 전체 반영된다."""
    return f'<div class="sec-title">{label}</div>'

def make_surface_section(b, text_sub, border_c):
    """Surface 계층 — 컬러칩 + 이름 + HEX 행 목록으로 통일"""
    if b.get('dual_mode'):
        light = b['surfaces']['light']
        dark  = b['surfaces']['dark']
        stack = [
            ("Light · Page",  light['page']),
            ("Light · Card",  light['card']),
            ("Dark  · Page",  dark['page']),
            ("Dark  · Card",  dark['card']),
        ]
    else:
        stack = b['surfaces']['stack']

    rows = ''
    for (label, color) in stack:
        dot_border = f'0.3mm solid {border_c}'
        rows += f'''
        <div style="display:flex;align-items:center;gap:2.5mm;margin-bottom:2mm;">
          <div style="width:11mm;height:5.5mm;background:{color};border-radius:1px;border:{dot_border};flex-shrink:0;"></div>
          <div style="flex:1;font-size:7pt;color:{text_sub};">{label}</div>
          <div style="font-size:6pt;font-family:monospace;color:{text_sub};opacity:.75;">{color}</div>
        </div>'''

    return f'''
    <div>
      {make_sec_title('Surface')}
      {rows}
    </div>'''

def make_text_tokens(b):
    """Text 컬러 4단계 — 실제 색상으로 텍스트 렌더링"""
    text_sub = b['text_sub']
    border_c = b['border']
    rows = ''
    for (token_name, color, sample) in b['text_tokens']:
        dot_border = f'0.25mm solid {border_c}' if luminance(color) > 0.85 else 'none'
        rows += f'''
        <div style="display:flex;align-items:center;gap:2mm;margin-bottom:2mm;">
          <div style="width:3.5mm;height:3.5mm;background:{color};border-radius:50%;flex-shrink:0;border:{dot_border};"></div>
          <div style="flex:1;font-size:7pt;color:{color};line-height:1.1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{sample}</div>
          <div style="font-size:6pt;font-family:monospace;color:{text_sub};opacity:.65;white-space:nowrap;">{token_name}</div>
        </div>'''
    return f'''
    <div style="margin-top:1.5mm;">
      {make_sec_title('Text Tokens')}
      {rows}
    </div>'''


# ── V2 → V3 마이그레이션 ─────────────────────────────────────────────────────

def migrate_brand_config(b):
    """V2 bds_ 파일에서 파생된 brand_config에 V3 필드가 없으면 자동으로 채운다.
    호출: generate_combined_html() 최상단에서 한 번.
    반환: 동일 dict (in-place 수정 + 반환)
    """
    primary = b['primary']
    accent  = b['accent']
    text_s  = b['text_sub']
    _neutral_raw = b.get('neutral_tints', [])
    neutral = (list(_neutral_raw.values()) if isinstance(_neutral_raw, dict) else _neutral_raw)
    radii   = b.get('radii', [])
    _p_raw  = b.get('primary_tints', [])
    p_tints = (list(_p_raw.values()) if isinstance(_p_raw, dict) else _p_raw)

    # ── personality ──────────────────────────────────────────────────────────
    if not b.get('personality'):
        r, g, bv = hex_to_rgb(primary)
        lum = luminance(primary)
        if r > g and r > bv and lum > 0.1:      # 붉은/주황 계열 → 따뜻한
            words = [('친근한',   '다가가기 쉬운 분위기로 신뢰를 만든다'),
                     ('포용적인', '누구나 환영받는 느낌을 준다'),
                     ('따뜻한',   '색상과 톤이 온기를 전달한다')]
        elif bv > r and bv > g:                  # 파란 계열 → 전문/신뢰
            words = [('명확한',   '정보를 군더더기 없이 전달한다'),
                     ('신뢰있는', '일관된 구조가 안정감을 준다'),
                     ('전문적인', '절제된 색감이 전문성을 드러낸다')]
        elif g > r and g > bv:                   # 초록 계열 → 자연/균형
            words = [('균형있는',   '색과 여백이 조화를 이룬다'),
                     ('자연스러운', '강요하지 않는 부드러운 인상을 준다'),
                     ('지속가능한', '눈에 피로감 없이 오래 바라볼 수 있다')]
        elif lum < 0.12:                          # 어두운 계열 → 고급/모던
            words = [('세련된',   '다크 톤이 고급스러운 분위기를 만든다'),
                     ('현대적인', '최소한의 요소로 최대의 임팩트를 낸다'),
                     ('격식있는', '중후한 인상이 신뢰와 권위를 나타낸다')]
        else:                                     # 기타 → 미니멀
            words = [('명확한',   '불필요한 장식 없이 내용에 집중한다'),
                     ('절제된',   '색과 형태가 목적만을 위해 존재한다'),
                     ('현대적인', '트렌드를 타지 않는 타임리스 디자인이다')]
        b['personality'] = words

    # ── token_hierarchy ──────────────────────────────────────────────────────
    if not b.get('token_hierarchy'):
        n100 = neutral[0] if len(neutral) > 0 else '#F5F5F5'
        n500 = neutral[3] if len(neutral) > 3 else '#8C8C8C'
        p500 = p_tints[5] if len(p_tints) > 5 else primary
        b['token_hierarchy'] = [
            (p500,   'primary-500', 'interactive',   '클릭 가능한 모든 요소'),
            (p500,   'primary-500', 'focus-ring',    '포커스 표시'),
            (accent, 'accent',      'destructive',   '되돌릴 수 없는 액션'),
            (text_s, 'text-sub',    'placeholder',   '입력 전 힌트 텍스트'),
            (n100,   'neutral-100', 'disabled-bg',   '비활성 배경'),
            (n500,   'neutral-500', 'disabled-text', '비활성 텍스트'),
        ]

    # ── component_hints ──────────────────────────────────────────────────────
    if not b.get('component_hints'):
        badge_r = '100px'
        box_r   = '6px'
        for (name, val) in radii:
            nm = name.lower()
            if 'badge' in nm or 'pill' in nm:
                badge_r = val
            elif 'box' in nm or 'card' in nm:
                box_r = val
        badge_bg   = p_tints[0] if p_tints else '#ECEEFE'
        badge_text = p_tints[7] if len(p_tints) > 7 else primary
        shadow_lvl = b.get('shadow_level', 'sm')
        card_shadow = 'sm' if any(x in shadow_lvl.lower() for x in ('sm', 'light', 'soft')) else 'md'
        b['component_hints'] = {
            'card':  {'bg': b['page_bg'], 'radius': box_r,   'border': b['border'], 'shadow': card_shadow},
            'badge': {'bg': badge_bg,     'text': badge_text, 'radius': badge_r},
            'input': {'border': b['border'], 'radius': box_r, 'focus': primary},
        }

    # ── name / tagline / source / spacing_base / shadow_level 기본값 ─
    if not b.get('name'):
        b['name'] = b.get('brand_name', 'Brand')
    if not b.get('tagline'):
        b['tagline'] = b.get('brand_tagline', '')
    if not b.get('source'):
        b['source'] = b.get('brand_name', 'brand config')
    if not b.get('spacing_base'):
        b['spacing_base'] = '8px'
    if not b.get('shadow_level'):
        b['shadow_level'] = 'Shadow sm'

    # ── heading_font / body_font / font_name (computed display) ──────────
    # font_name → 하위 호환용 단일 폰트명 (구 bds_ 파일). heading_font 없으면 폴백.
    _fallback_font = b.get('font_name', 'Pretendard')
    if not b.get('heading_font'):
        b['heading_font'] = _fallback_font
    if not b.get('body_font'):
        b['body_font'] = b['heading_font']
    # font_name을 표시용으로 재계산 (heading ≠ body면 "H / B" 형식)
    if b['heading_font'] != b['body_font']:
        b['font_name'] = f"{b['heading_font']} / {b['body_font']}"
    else:
        b['font_name'] = b['heading_font']

    # ── 색상 설명 기본값 ──────────────────────────────────────────────
    if not b.get('primary_desc'):
        b['primary_desc'] = b.get('brand_name', 'Primary')
    if not b.get('secondary_desc'):
        b['secondary_desc'] = 'Secondary'
    if not b.get('accent_desc'):
        b['accent_desc'] = 'Accent'

    # ── type_scale 기본값 ─────────────────────────────────────────────
    if not b.get('type_scale'):
        b['type_scale'] = [
            ('Display',    40, 700, '1.2', b.get('brand_name', 'Display'),        16),
            ('Heading 1',  32, 700, '1.3', '제목 텍스트',                         13),
            ('Heading 2',  24, 600, '1.3', '소제목 텍스트',                       10),
            ('Heading 3',  20, 600, '1.4', '섹션 제목',                            9),
            ('Body',       16, 400, '1.7', '본문 텍스트입니다. 읽기 편한 크기.',   7.5),
            ('Body SM',    14, 400, '1.7', '작은 본문 텍스트',                     6.5),
            ('Caption',    12, 400, '1.5', '캡션 / 보조 안내',                     5.5),
        ]

    # ── radii 기본값 ──────────────────────────────────────────────────
    if not b.get('radii'):
        b['radii'] = [
            ('badge',   '100px'),
            ('box',     '10px'),
            ('callout', '14px'),
            ('table',   '6px'),
        ]

    # ── buttons 기본값 ────────────────────────────────────────────────
    if not b.get('buttons'):
        primary_on_c = on_color(primary)
        b['buttons'] = [
            ('Primary',  primary,        primary_on_c, 'none'),
            ('Secondary', 'transparent', primary,      f'1.5px solid {primary}'),
            ('Ghost',     'transparent', b.get('text_sub', '#888'), 'none'),
        ]

    # ── surfaces 기본값 ───────────────────────────────────────────────
    if not b.get('surfaces'):
        b['surfaces'] = {
            'light': {'page': b.get('page_bg', '#FFFFFF'), 'card': '#FFFFFF'},
            'dark':  {'page': '#1C1410', 'card': '#2A1F1A'},
            'stack': [],
        }

    # ── text_tokens 기본값 ────────────────────────────────────────────
    if not b.get('text_tokens'):
        b['text_tokens'] = [
            ('Text.Main',    b.get('text_main', '#111111'), '기본 본문'),
            ('Text.Sub',     b.get('text_sub',  '#888888'), '보조 텍스트'),
            ('Text.Inverse', b.get('page_bg',   '#FFFFFF'), '반전 배경 위 텍스트'),
        ]

    # ── font_badge_bg 기본값 ──────────────────────────────────────────
    if not b.get('font_badge_bg'):
        b['font_badge_bg'] = (p_tints[0] if p_tints else '#ECEEFE')

    return b


# ── 페이지 1 (요약·큼직) 전용 헬퍼 ─────────────────────────────────────────

def make_swatch_big(color, name, desc, text_color, border="none"):
    """1페이지 요약용 큰 브랜드 스와치. 가로 펼침 그리드 셀에 들어감."""
    tc = on_color(color)
    return f'''
    <div style="flex:1;display:flex;flex-direction:column;">
      <div style="background:{color};border:{border};border-radius:3mm;padding:5mm 6mm;flex:1;display:flex;flex-direction:column;justify-content:space-between;min-height:26mm;">
        <div style="font-size:15pt;font-weight:700;color:{tc};letter-spacing:.02em;">{name}</div>
        <div style="font-size:11pt;font-family:monospace;color:{tc};opacity:.9;">{color}</div>
      </div>
      <div style="font-size:8.5pt;color:{text_color};margin-top:2mm;line-height:1.35;text-align:center;">{desc}</div>
    </div>'''


def make_tint_strip_big(colors, label_color, strip_labels=None):
    """1페이지 요약용 큰 틴트 스트립. 칸 높이 13mm."""
    default_labels = ['50','100','200','300','400','500','600','700','800','900']
    lbls = strip_labels if strip_labels else default_labels[:len(colors)]
    base_500_idx = lbls.index('500') if '500' in lbls else -1
    cells = ''
    for i, c in enumerate(colors):
        inset = 'box-shadow:inset 0 0 0 2.5px #fff;' if i == base_500_idx else ''
        cells += f'<div style="flex:1;height:13mm;background:{c};{inset}"></div>'
    label_cells = ''
    for i, lbl in enumerate(lbls):
        fw = 'font-weight:700;' if i == base_500_idx else ''
        label_cells += f'<div style="flex:1;text-align:center;font-size:7.5pt;{fw}color:{label_color};opacity:.75;">{lbl}</div>'
    return f'''
    <div style="margin-bottom:4mm;">
      <div style="display:flex;border-radius:1.5mm;overflow:hidden;">{cells}</div>
      <div style="display:flex;margin-top:2mm;">{label_cells}</div>
    </div>'''


def make_typography_preview(font_family, body_family, same_font, text_main, text_sub, primary, badge_bg):
    """1페이지 요약용 폰트 페어 라벨 + 큰 샘플."""
    if same_font:
        pair_label = f'''
        <div style="display:flex;align-items:center;gap:3mm;margin-bottom:5mm;">
          <div style="font-size:8pt;color:{text_sub};opacity:.75;letter-spacing:.1em;text-transform:uppercase;font-weight:700;">Font</div>
          <div style="background:{badge_bg};color:{primary};font-size:12pt;font-weight:700;padding:2mm 5mm;border-radius:2mm;font-family:'{font_family}','NKR',sans-serif;">{font_family}</div>
        </div>'''
    else:
        pair_label = f'''
        <div style="display:flex;flex-direction:column;gap:2.5mm;margin-bottom:5mm;">
          <div style="display:flex;align-items:center;gap:3mm;">
            <div style="font-size:8pt;color:{text_sub};opacity:.75;letter-spacing:.1em;text-transform:uppercase;font-weight:700;width:18mm;">Heading</div>
            <div style="background:{badge_bg};color:{primary};font-size:12pt;font-weight:700;padding:2mm 5mm;border-radius:2mm;font-family:'{font_family}','NKR',sans-serif;">{font_family}</div>
          </div>
          <div style="display:flex;align-items:center;gap:3mm;">
            <div style="font-size:8pt;color:{text_sub};opacity:.75;letter-spacing:.1em;text-transform:uppercase;font-weight:700;width:18mm;">Body</div>
            <div style="background:{badge_bg};color:{primary};font-size:12pt;font-weight:700;padding:2mm 5mm;border-radius:2mm;font-family:'{body_family}','NKR',sans-serif;">{body_family}</div>
          </div>
        </div>'''
    return f'''
    {pair_label}
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:5mm;min-height:0;">
      <div style="font-family:'{font_family}','NKR',sans-serif;font-size:32pt;font-weight:700;color:{text_main};line-height:1.1;letter-spacing:-0.02em;">Display</div>
      <div style="font-family:'{font_family}','NKR',sans-serif;font-size:15pt;font-weight:700;color:{text_main};line-height:1.3;">제목 Heading</div>
      <div style="font-family:'{body_family}','NKR',sans-serif;font-size:10.5pt;font-weight:400;color:{text_main};line-height:1.5;">본문 텍스트 — 일관된 시각 언어로 읽기 좋은 흐름을 만듭니다.</div>
    </div>'''


def make_radius_row_big(name, radius_val, primary, label_color):
    """1페이지 요약용 큰 Named Radius 행."""
    br = radius_val if radius_val != '100px' else '20mm'
    return f'''
    <div style="display:flex;align-items:center;gap:4mm;">
      <div style="width:28mm;height:9mm;background:{primary};border-radius:{br};flex-shrink:0;"></div>
      <div style="flex:1;">
        <div style="font-size:12pt;font-weight:700;color:{label_color};line-height:1.2;">{name}</div>
        <div style="font-size:9pt;font-family:monospace;color:{label_color};opacity:.65;margin-top:0.8mm;">{radius_val}</div>
      </div>
    </div>'''


def make_button_big(label, bg, text, border_style, radius="20mm", font_family='sans-serif'):
    """1페이지 요약용 큰 버튼."""
    return (
        f'<div style="background:{bg};border:{border_style};border-radius:{radius};'
        f'padding:0 9mm;height:11mm;line-height:11mm;'
        f'display:inline-block;text-align:center;vertical-align:middle;'
        f'margin-right:3mm;margin-bottom:2.5mm;'
        f"font-family:'{font_family}','NKR',sans-serif;"
        f'font-size:12pt;font-weight:700;color:{text};white-space:nowrap;">'
        f'{label}</div>'
    )


# ── 핵심 HTML 생성 — fonts_dir 파라미터 필수 ───────────────────────────────

def generate_combined_html(b, fonts_dir):
    """1페이지(토큰) + 2페이지(In Use) 합본 HTML 생성.

    Args:
        b:         brand_config dict
        fonts_dir: 폰트 폴더 절대경로 (세션 경로 포함한 실제 경로)
                   예) '/sessions/abc123.../mnt/claude_work/0000_공용형식/fonts'
    """
    # V2 bds_ 파일 자동 업그레이드 — V3 필드 없으면 자동 파생
    b = migrate_brand_config(b)

    page_bg   = b['page_bg']
    text_main = b['text_main']
    text_sub  = b['text_sub']
    border_c  = b['border']
    primary   = b['primary']
    secondary = b['secondary']
    accent    = b['accent']
    accent_border = '0.3mm solid #CCCCCC' if accent == '#FFFFFF' else 'none'

    _pt_raw = b['primary_tints']
    p_tints = list(_pt_raw.values()) if isinstance(_pt_raw, dict) else _pt_raw
    _nt_raw = b['neutral_tints']
    if isinstance(_nt_raw, dict):
        n_tints = list(_nt_raw.values())
        n_tint_labels = [str(k) for k in _nt_raw.keys()]
    else:
        n_tints = _nt_raw
        n_tint_labels = b.get('neutral_tint_labels')

    heading_font = b.get('heading_font', 'Pretendard')
    body_font    = b.get('body_font',    heading_font)
    same_font    = (heading_font == body_font)
    font_display = b.get('font_name', heading_font)  # 표시용 (migrate에서 계산됨)

    # ── heading 폰트 파일 탐색 ────────────────────────────────────────────
    ff = b.get('font_files', {
        'family':  heading_font,
        'regular': None,
        'bold':    None,
    })
    font_family = ff.get('family') or heading_font or 'sans-serif'

    _r_path = ff.get('regular')
    _b_path = ff.get('bold')
    if not _r_path or not os.path.isfile(_r_path):
        _r_path = find_font(font_family, fonts_dir, weight='regular')
    if not _b_path or not os.path.isfile(_b_path):
        _b_path = find_font(font_family, fonts_dir, weight='bold') or _r_path

    font_path_r = f"file://{_r_path}" if _r_path else ''
    font_path_b = f"file://{_b_path}" if _b_path else font_path_r

    # ── body 폰트 파일 탐색 (heading과 다를 때만) ─────────────────────────
    if same_font:
        body_family   = font_family
        body_path_r   = font_path_r
        body_path_b   = font_path_b
    else:
        bff = b.get('body_font_files', {
            'family':  body_font,
            'regular': None,
            'bold':    None,
        })
        body_family = bff.get('family') or body_font or 'sans-serif'
        _br_path = bff.get('regular')
        _bb_path = bff.get('bold')
        if not _br_path or not os.path.isfile(_br_path):
            _br_path = find_font(body_family, fonts_dir, weight='regular')
        if not _bb_path or not os.path.isfile(_bb_path):
            _bb_path = find_font(body_family, fonts_dir, weight='bold') or _br_path
        body_path_r = f"file://{_br_path}" if _br_path else ''
        body_path_b = f"file://{_bb_path}" if _bb_path else body_path_r

    # NotoSansKR: 한글 fallback 폰트 — 재귀 탐색
    _nk_r = find_font('NotoSansKR', fonts_dir, weight='regular') or \
            find_font('Noto Sans KR', fonts_dir, weight='regular')
    _nk_b = find_font('NotoSansKR', fonts_dir, weight='bold') or \
            find_font('Noto Sans KR', fonts_dir, weight='bold') or _nk_r

    font_path_nk  = f"file://{_nk_r}" if _nk_r else ''
    font_path_nkb = f"file://{_nk_b}" if _nk_b else font_path_nk

    primary_on = on_color(primary)

    # ── 1페이지 콘텐츠 빌드 ──────────────────────────────────────────
    # Heading 행 = Display / Heading 1~4 → heading_font
    # Body 행    = Body / Caption / Body SM 등 그 외 → body_font
    HEADING_LABELS = {'display', 'heading 1', 'heading 2', 'heading 3', 'heading 4',
                      'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}
    type_rows = ''
    for i, (label, size, wt, lh, sample, psize) in enumerate(b['type_scale']):
        h = ROW_HEIGHTS_MM[i] if i < len(ROW_HEIGHTS_MM) else 6
        if same_font:
            font_ovr = None
        elif label.lower() in HEADING_LABELS:
            font_ovr = font_family   # heading 폰트
        else:
            font_ovr = body_family   # body 폰트
        type_rows += make_type_row(label, size, wt, lh, sample, psize, text_main, border_c, h, font_override=font_ovr)

    swatches  = make_swatch(primary,   'Primary',   b['primary_desc'],   text_sub)
    swatches += make_swatch(secondary, 'Secondary', b['secondary_desc'],  text_sub, border='0.3mm solid #444')
    swatches += make_swatch(accent,    'Accent',    b['accent_desc'],     text_sub, border=accent_border)

    radius_rows = ''
    for (name, val) in b['radii']:
        radius_rows += make_radius_row(name, val, primary, text_sub)

    btn_radius = '20mm'  # 기본 pill — Named Radius badge 값으로 덮어씀
    for (rname, rval) in b.get('radii', []):
        if rname.lower() == 'badge':
            btn_radius = rval
            break

    buttons_html = ''
    for (label, bg, tc, bdr) in b['buttons']:
        buttons_html += make_button(label, bg, tc, bdr, btn_radius, font_family)

    surface_html     = make_surface_section(b, text_sub, border_c)
    text_tokens_html = make_text_tokens(b)

    # ── 1페이지 요약용 큼직 조각 ────────────────────────────────────────
    swatches_big  = make_swatch_big(primary,   'Primary',   b['primary_desc'],   text_sub)
    swatches_big += make_swatch_big(secondary, 'Secondary', b['secondary_desc'],  text_sub, border='0.3mm solid #444')
    swatches_big += make_swatch_big(accent,    'Accent',    b['accent_desc'],     text_sub, border=accent_border)

    tint_strips_big  = make_tint_strip_big(p_tints, text_sub)
    tint_strips_big += make_tint_strip_big(n_tints, text_sub, n_tint_labels)

    typo_preview = make_typography_preview(font_family, body_family, same_font,
                                            text_main, text_sub, primary,
                                            b.get('font_badge_bg', '#ECEEFE'))

    radius_rows_big = ''
    for (name, val) in b['radii']:
        radius_rows_big += make_radius_row_big(name, val, primary, text_sub)

    buttons_big_html = ''
    for (label, bg, tc, bdr) in b['buttons']:
        buttons_big_html += make_button_big(label, bg, tc, bdr, btn_radius, font_family)

    # ── 2페이지 변수 ─────────────────────────────────────────────────
    ppt_bg     = '#FFFFFF'
    ppt_text   = '#111111'
    ppt_sub    = '#888888'
    ppt_border = '#E0E0E0'
    word_border = '#D8D8D8'
    table_alt   = '#F5F5F5'
    sns_bg2     = b.get('font_badge_bg', '#ECEEFE')

    # Surface 값 — 실제 브랜드 토큰 사용 (하드코딩 금지)
    light_surface_val = b['page_bg']
    if b.get('dual_mode'):
        dark_surface_val = b['surfaces']['dark']['page']
    else:
        dark_surface_val = '해당 없음'

    sub_lbl = f'font-size:7pt;font-weight:700;color:{text_sub};letter-spacing:.08em;text-transform:uppercase;height:5mm;display:flex;align-items:center;margin-bottom:2mm;flex-shrink:0;'

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
@font-face {{ font-family: '{font_family}'; src: url('{font_path_r}'); font-weight: 400; }}
@font-face {{ font-family: '{font_family}'; src: url('{font_path_b}'); font-weight: 700; }}
{f"@font-face {{ font-family: '{body_family}'; src: url('{body_path_r}'); font-weight: 400; }}" if not same_font else ""}
{f"@font-face {{ font-family: '{body_family}'; src: url('{body_path_b}'); font-weight: 700; }}" if not same_font else ""}
@font-face {{ font-family: 'NKR'; src: url('{font_path_nk}'); font-weight: 400; }}
@font-face {{ font-family: 'NKR'; src: url('{font_path_nkb}'); font-weight: 700; }}

@page {{ size: A4 landscape; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; line-height: 1; }}
body {{ font-family: '{body_family}', 'NKR', sans-serif; background: {page_bg}; color: {text_main}; line-height: 1; }}

.page {{ width: 297mm; height: 210mm; display: flex; flex-direction: column; overflow: hidden; page-break-after: always; page-break-inside: avoid; break-inside: avoid; }}
.page:last-child {{ page-break-after: avoid; }}
.accent-bar {{ height: 5mm; background: {primary}; flex-shrink: 0; }}
.header {{ padding: 0 7mm; height: 24mm; display: flex; justify-content: space-between; align-items: center; border-bottom: 0.3mm solid {border_c}; flex-shrink: 0; }}
.brand-block {{ display: flex; align-items: center; gap: 4mm; }}
.color-mark {{ width: 9mm; height: 9mm; background: {primary}; border-radius: 2mm; flex-shrink: 0; }}
.brand-name {{ font-size: 22pt; font-weight: 700; color: {text_main}; letter-spacing: -0.02em; font-family: '{font_family}', 'NKR', sans-serif; line-height: 1.05; }}
.brand-tagline {{ font-size: 8pt; color: {text_sub}; margin-top: 1.5mm; letter-spacing: .03em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 140mm; }}
.header-meta {{ display: flex; align-items: center; gap: 2.5mm; }}
.badge {{ font-size: 7.5pt; padding: 1.5mm 3.5mm; border-radius: 10mm; border: 0.3mm solid {border_c}; color: {text_sub}; white-space: nowrap; line-height: 1; }}
.badge-primary {{ background: {primary}; color: {primary_on}; border: none; }}
.content {{ flex: 1; display: flex; overflow: hidden; }}
.col {{ padding: 4mm 5mm; border-right: 0.3mm solid {border_c}; overflow: hidden; display: flex; flex-direction: column; height: 100%; box-sizing: border-box; }}
.col:last-child {{ border-right: none; }}
.col-colors {{ width: 28%; }}
.col-type   {{ width: 42%; }}
.col-comp   {{ width: 30%; }}
.col-left   {{ flex: 1; }}
.col-right  {{ width: 91mm; flex-shrink: 0; }}
.col-title {{ font-size: 9pt; font-weight: 700; color: {text_main}; letter-spacing: .08em; margin-bottom: 3.5mm; height: 7mm; flex-shrink: 0; display: flex; align-items: center; border-bottom: 0.4mm solid {border_c}; text-transform: uppercase; line-height: 1; }}
.divider {{ height: 0.15mm; background: {border_c}; margin: 2mm 0; }}
.font-name-badge {{ display: inline-flex; align-items: center; font-size: 9pt; font-weight: 700; color: {primary}; background: {b['font_badge_bg']}; padding: 0 4mm; height: 8mm; border-radius: 2mm; margin-bottom: 3mm; line-height: 1; font-family: '{font_family}', 'NKR', sans-serif; }}
.footer {{ padding: 2.5mm 7mm; border-top: 0.3mm solid {border_c}; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; }}
.footer-text {{ font-size: 7pt; color: {text_sub}; opacity: .65; }}
.sec-title {{ font-size: 7pt; font-weight: 700; color: {text_sub}; letter-spacing: .1em; margin-bottom: 2.5mm; height: 5mm; display: flex; align-items: center; text-transform: uppercase; line-height: 1; opacity: .75; }}
.col-title-big {{ font-size: 12pt; font-weight: 700; color: {text_main}; letter-spacing: .08em; margin-bottom: 3.5mm; display: flex; align-items: center; text-transform: uppercase; line-height: 1; padding-bottom: 2mm; border-bottom: 0.4mm solid {primary}; }}
</style>
</head>
<body>

<!-- ═══════ PAGE 1 : SUMMARY (디자이너용 요약) ═══════ -->
<div class="page">
  <div class="accent-bar"></div>
  <div class="header">
    <div class="brand-block">
      <div class="color-mark"></div>
      <div>
        <div class="brand-name">{b['name']}</div>
        <div class="brand-tagline">{b['tagline']}</div>
      </div>
    </div>
    <div class="header-meta">
      <div class="badge">{font_display}</div>
      <div class="badge">{b['mode']}</div>
      <div class="badge-primary badge">v1.0</div>
      <div class="badge" style="background:{primary};color:{primary_on};border:none;">1 / 3</div>
    </div>
  </div>
  <div class="content" style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:minmax(0,1fr) minmax(0,1fr);gap:5mm;padding:5mm;min-height:0;">

    <!-- 좌상 : Brand Colors 큰 스와치 3개 -->
    <div style="display:flex;flex-direction:column;overflow:hidden;">
      <div class="col-title-big">Brand Colors</div>
      <div style="display:flex;gap:4mm;flex:1;">
        {swatches_big}
      </div>
    </div>

    <!-- 우상 : Typography 미리보기 -->
    <div style="display:flex;flex-direction:column;overflow:hidden;">
      <div class="col-title-big">Typography</div>
      {typo_preview}
    </div>

    <!-- 좌하 : Tint Strips + Surface -->
    <div style="display:flex;flex-direction:column;overflow:hidden;">
      <div class="col-title-big">Tints &amp; Surface</div>
      {tint_strips_big}
      {surface_html}
    </div>

    <!-- 우하 : Named Radius + Buttons -->
    <div style="display:flex;flex-direction:column;overflow:hidden;">
      <div class="col-title-big">Radius &amp; Buttons</div>
      <div style="display:flex;flex-direction:column;gap:2mm;margin-bottom:3mm;">
        {radius_rows_big}
      </div>
      <div style="height:0.15mm;background:{border_c};margin-bottom:3mm;"></div>
      <div>{buttons_big_html}</div>
    </div>

  </div>
  <div class="footer">
    <div class="footer-text">Generated by design-system-by-blue · Extracted from {b['source']}</div>
    <div class="footer-text">{b['name']} Design System · Version 1.0</div>
  </div>
</div>

<!-- ═══════ PAGE 2 : DETAIL (일반 오피스 사용자용 상세) ═══════ -->
<div class="page">
  <div class="accent-bar"></div>
  <div class="header">
    <div class="brand-block">
      <div class="color-mark"></div>
      <div>
        <div class="brand-name">{b['name']}</div>
        <div class="brand-tagline">{b['tagline']}</div>
      </div>
    </div>
    <div class="header-meta">
      <div class="badge">{font_display}</div>
      <div class="badge">{b['mode']}</div>
      <div class="badge-primary badge">v1.0</div>
      <div class="badge" style="background:{primary};color:{primary_on};border:none;">2 / 3</div>
    </div>
  </div>
  <div class="content">
    <div class="col col-type" style="width:38%;">
      <div class="col-title">Typography &amp; Text</div>
      <div class="font-name-badge">{font_display}</div>
      {type_rows}
      <div class="divider"></div>
      {text_tokens_html}
    </div>
    <div class="col col-comp" style="width:31%;">
      <div class="col-title">Semantic &amp; Brand</div>
      {make_semantic_section(b, text_sub, border_c)}
      <div class="divider"></div>
      {make_token_hierarchy_section(b, text_sub, border_c)}
      <div class="divider"></div>
      <div class="sec-title">Brand Personality</div>
      {make_personality_section(b, text_sub, border_c)}
    </div>
    <div class="col col-comp" style="width:31%;">
      <div class="col-title">Spacing, Shadow &amp; Components</div>
      <div class="sec-title">Spacing &amp; Shadow</div>
      <div style="display:flex;gap:2mm;align-items:flex-end;margin-bottom:2mm;">
        <div style="width:2mm;height:3mm;background:{primary};opacity:.5;border-radius:0.5mm;"></div>
        <div style="width:4mm;height:5mm;background:{primary};opacity:.65;border-radius:0.5mm;"></div>
        <div style="width:6mm;height:7mm;background:{primary};opacity:.8;border-radius:0.5mm;"></div>
        <div style="width:8mm;height:10mm;background:{primary};border-radius:0.5mm;"></div>
        <div style="width:10mm;height:13mm;background:{primary};border-radius:0.5mm;opacity:.9;"></div>
      </div>
      <div style="font-size:7pt;font-family:monospace;color:{text_sub};opacity:.75;">base {b['spacing_base']} · {b['shadow_level']}</div>
      <div class="divider"></div>
      {make_component_hints_section(b, text_sub, border_c)}
    </div>
  </div>
  <div class="footer">
    <div class="footer-text">Generated by design-system-by-blue · Extracted from {b['source']}</div>
    <div class="footer-text">{b['name']} Design System · Version 1.0</div>
  </div>
</div>

<!-- ═══════ PAGE 3 : IN USE ═══════ -->
<div class="page">
  <div class="accent-bar"></div>
  <div class="header">
    <div class="brand-block">
      <div class="color-mark"></div>
      <div>
        <div class="brand-name">{b['name']}</div>
        <div class="brand-tagline">{b['tagline']}</div>
      </div>
    </div>
    <div class="header-meta">
      <div class="badge">{font_display}</div>
      <div class="badge">{b['mode']}</div>
      <div class="badge-primary badge">v1.0</div>
      <div class="badge" style="background:{primary};color:{primary_on};border:none;">3 / 3</div>
    </div>
  </div>

  <div class="content">

    <!-- 좌 2/3 : PPT + Word -->
    <div class="col col-left">
      <div class="col-title">In Use</div>
      <div style="flex:1;display:flex;flex-direction:column;gap:3mm;overflow:hidden;">

        <!-- PPT 슬라이드 목업 (16:9) -->
        <div style="flex:0.85;display:flex;flex-direction:column;overflow:hidden;">
          <div style="{sub_lbl}">PPT Slide</div>
          <div style="flex:1;display:flex;align-items:center;overflow:hidden;">
            <div style="width:128mm;height:72mm;flex-shrink:0;background:{ppt_bg};border:0.3mm solid {ppt_border};border-radius:1.5mm;overflow:hidden;display:flex;flex-direction:column;">
              <div style="height:2.5mm;background:{primary};flex-shrink:0;"></div>
              <div style="flex:1;display:flex;overflow:hidden;">

                <!-- 좌측 : 막대 차트 -->
                <div style="flex:1.2;padding:7mm 7mm 7mm 8mm;display:flex;flex-direction:column;overflow:hidden;border-right:0.2mm solid {ppt_border};">
                  <div style="font-size:7pt;font-weight:700;color:{ppt_sub};letter-spacing:.08em;text-transform:uppercase;margin-bottom:4mm;">분기별 성장</div>
                  <div style="flex:1;display:flex;align-items:flex-end;gap:4mm;padding:5mm 0 3mm 0;border-bottom:0.2mm solid {ppt_border};">
                    <!-- Q1 -->
                    <div style="flex:1;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end;">
                      <div style="font-size:8pt;color:{ppt_sub};margin-bottom:2mm;font-weight:700;">12</div>
                      <div style="width:100%;height:38%;background:{primary};opacity:.4;border-radius:1mm 1mm 0 0;"></div>
                    </div>
                    <!-- Q2 -->
                    <div style="flex:1;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end;">
                      <div style="font-size:8pt;color:{ppt_sub};margin-bottom:2mm;font-weight:700;">18</div>
                      <div style="width:100%;height:56%;background:{primary};opacity:.6;border-radius:1mm 1mm 0 0;"></div>
                    </div>
                    <!-- Q3 -->
                    <div style="flex:1;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end;">
                      <div style="font-size:8pt;color:{ppt_sub};margin-bottom:2mm;font-weight:700;">24</div>
                      <div style="width:100%;height:75%;background:{primary};opacity:.78;border-radius:1mm 1mm 0 0;"></div>
                    </div>
                    <!-- Q4 (강조) -->
                    <div style="flex:1;display:flex;flex-direction:column;align-items:center;height:100%;justify-content:flex-end;">
                      <div style="font-size:10pt;color:{primary};margin-bottom:2mm;font-weight:700;">32</div>
                      <div style="width:100%;height:100%;background:{primary};border-radius:1mm 1mm 0 0;"></div>
                    </div>
                  </div>
                  <div style="display:flex;gap:4mm;margin-top:3mm;">
                    <div style="flex:1;text-align:center;font-size:8pt;color:{ppt_sub};">Q1</div>
                    <div style="flex:1;text-align:center;font-size:8pt;color:{ppt_sub};">Q2</div>
                    <div style="flex:1;text-align:center;font-size:8pt;color:{ppt_sub};">Q3</div>
                    <div style="flex:1;text-align:center;font-size:9pt;font-weight:700;color:{ppt_text};">Q4</div>
                  </div>
                </div>

                <!-- 우측 : 설명 -->
                <div style="flex:1;padding:7mm 7mm 6mm 6mm;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden;">
                  <div>
                    <div style="font-size:7pt;font-weight:700;color:{primary};letter-spacing:.1em;text-transform:uppercase;margin-bottom:2.5mm;font-family:'{font_family}','NKR',sans-serif;">Quarterly Report</div>
                    <div style="font-size:14pt;font-weight:700;color:{ppt_text};line-height:1.2;margin-bottom:3mm;font-family:'{font_family}','NKR',sans-serif;">성장 추이</div>
                    <div style="font-size:24pt;font-weight:700;color:{primary};line-height:1;margin-bottom:2.5mm;font-family:'{font_family}','NKR',sans-serif;">+32%</div>
                    <div style="font-size:10pt;color:{ppt_sub};line-height:1.5;">전년 동기 대비<br>가파른 성장 기록</div>
                  </div>
                  <div style="display:flex;align-items:center;gap:2mm;">
                    <div style="width:2.2mm;height:2.2mm;border-radius:50%;background:{primary};"></div>
                    <div style="font-size:8pt;color:{ppt_sub};opacity:.75;">{b['name']} · 2026</div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>

        <!-- Word 문서 목업 -->
        <div style="flex:1.15;display:flex;flex-direction:column;overflow:hidden;">
          <div style="{sub_lbl}">Word Document</div>
          <div style="flex:1;background:#FFFFFF;border:0.3mm solid {word_border};border-radius:1.5mm;overflow:hidden;padding:3.5mm 5mm;display:flex;flex-direction:column;justify-content:flex-start;">
            <div style="font-size:14pt;font-weight:700;color:{primary};border-bottom:0.5mm solid {primary};padding-bottom:1.5mm;margin-bottom:2mm;line-height:1.2;font-family:'{font_family}','NKR',sans-serif;">디자인 시스템 활용 가이드</div>
            <div style="font-size:10pt;color:#222222;line-height:1.45;margin-bottom:2mm;">디자인 시스템은 색상·타이포그래피·컴포넌트를 하나의 규칙으로 묶어 브랜드 일관성과 제작 효율을 동시에 높이는 구조적 체계입니다.</div>
            <div style="margin-bottom:2mm;">
              <div style="display:flex;gap:2.5mm;align-items:center;margin-bottom:1.2mm;">
                <div style="width:1.8mm;height:1.8mm;border-radius:50%;background:{primary};flex-shrink:0;"></div>
                <div style="font-size:10pt;color:#222222;line-height:1.3;">색상 · 타이포그래피 토큰 일괄 관리</div>
              </div>
              <div style="display:flex;gap:2.5mm;align-items:center;margin-bottom:1.2mm;">
                <div style="width:1.8mm;height:1.8mm;border-radius:50%;background:{primary};flex-shrink:0;"></div>
                <div style="font-size:10pt;color:#222222;line-height:1.3;">PPT · Word · SNS 등 다채널 즉시 적용</div>
              </div>
              <div style="display:flex;gap:2.5mm;align-items:center;">
                <div style="width:1.8mm;height:1.8mm;border-radius:50%;background:{primary};flex-shrink:0;"></div>
                <div style="font-size:10pt;color:#222222;line-height:1.3;">브랜드 일관성을 코드처럼 구조화</div>
              </div>
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:10pt;line-height:1.2;">
              <tr>
                <th style="background:{primary};color:{primary_on};padding:1.8mm 2.5mm;text-align:left;font-weight:700;width:28%;">구분</th>
                <th style="background:{primary};color:{primary_on};padding:1.8mm 2.5mm;text-align:left;font-weight:700;width:36%;">라이트 모드</th>
                <th style="background:{primary};color:{primary_on};padding:1.8mm 2.5mm;text-align:left;font-weight:700;width:36%;">다크 모드</th>
              </tr>
              <tr style="background:{table_alt};">
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;">Primary</td>
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;font-family:monospace;">{primary}</td>
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;">동일 적용</td>
              </tr>
              <tr>
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;">Surface</td>
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;font-family:monospace;">{light_surface_val}</td>
                <td style="padding:1.8mm 2.5mm;border-bottom:0.3mm solid {word_border};color:#111111;">{dark_surface_val}</td>
              </tr>
              <tr style="background:{table_alt};">
                <td style="padding:1.8mm 2.5mm;color:#111111;">Typography</td>
                <td style="padding:1.8mm 2.5mm;color:#111111;">{font_display}</td>
                <td style="padding:1.8mm 2.5mm;color:#111111;">동일 적용</td>
              </tr>
            </table>
          </div>
        </div>

      </div>
    </div>

    <!-- 우 1/3 : SNS 카드 -->
    <div class="col col-right">
      <div class="col-title">SNS Card</div>
      <div style="flex:1;display:flex;flex-direction:column;gap:3mm;overflow:hidden;">

        <!-- SNS Card 1 : 이미지형 -->
        <div style="width:80mm;height:80mm;flex-shrink:0;border:0.3mm solid {border_c};border-radius:1.5mm;overflow:hidden;display:flex;flex-direction:column;background:{primary};">
          <div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:4mm;">
            <div style="background:rgba(0,0,0,0.42);border-radius:1.5mm;padding:3mm 3.5mm;">
              <div style="font-size:14pt;font-weight:700;color:#FFFFFF;line-height:1.2;margin-bottom:1.5mm;font-family:'{font_family}','NKR',sans-serif;">{b['name']}</div>
              <div style="font-size:10pt;color:rgba(255,255,255,0.88);line-height:1.4;">Design System · Colors &amp; Type</div>
            </div>
          </div>
          <div style="background:{page_bg};padding:2.5mm 3.5mm;flex-shrink:0;border-top:0.3mm solid {border_c};">
            <div style="height:3.5pt;background:{border_c};border-radius:1mm;width:72%;margin-bottom:1.5mm;"></div>
            <div style="height:3.5pt;background:{border_c};border-radius:1mm;width:52%;opacity:.6;"></div>
          </div>
        </div>

        <!-- SNS Card 2 : 텍스트 카드형 -->
        <div style="width:80mm;height:80mm;flex-shrink:0;border:0.3mm solid {border_c};border-radius:1.5mm;overflow:hidden;display:flex;flex-direction:column;background:{sns_bg2};">
          <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:5mm;overflow:hidden;">
            <div style="font-size:14pt;font-weight:700;color:{primary};line-height:1.25;margin-bottom:3mm;font-family:'{font_family}','NKR',sans-serif;">Consistent.<br>Scalable.<br>Beautiful.</div>
            <div style="font-size:10pt;color:{text_sub};line-height:1.55;margin-bottom:4mm;">모든 페이지, 모든 화면에서<br>동일한 디자인 경험을 제공합니다.</div>
            <div style="display:inline-flex;align-items:center;background:{primary};color:{primary_on};font-size:10pt;font-weight:700;padding:2mm 5mm;border-radius:10mm;align-self:flex-start;line-height:1;">시작하기</div>
          </div>
        </div>

      </div>
    </div>

  </div>

  <div class="footer">
    <div class="footer-text">Generated by design-system-by-blue · Extracted from {b['source']}</div>
    <div class="footer-text">{b['name']} Design System · Version 1.0</div>
  </div>
</div>

</body>
</html>'''


# ── 페이지 분리 ────────────────────────────────────────────────────────────

def split_pages(combined_html):
    """합본 HTML을 1페이지 / 2페이지 독립 HTML로 분리.
    단일 HTML + CSS page-break 방식 대신 각 페이지를 독립 HTML로 렌더링해
    Chromium 페이지네이션 오프셋 버그를 방지한다.
    """
    css_start = combined_html.find('<style>')
    css_end   = combined_html.find('</style>') + len('</style>')
    css       = combined_html[css_start:css_end]

    parts = combined_html.split(PAGE2_MARKER)
    body1 = parts[0].split('<body>')[1].rstrip()
    body2 = PAGE2_MARKER + parts[1].rsplit('</body>', 1)[0]

    shell = '<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8">{css}</head><body>{body}</body></html>'
    return (
        shell.format(css=css, body=body1),
        shell.format(css=css, body=body2),
    )

