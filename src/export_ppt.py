from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import json
import os
import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def apply_theme(slide, theme_name):
    themes = {
        "light": {"bg": "#ffffff", "text": "#1d1d1f", "accent": "#0066cc"},
        "dark": {"bg": "#1d1d1f", "text": "#ffffff", "accent": "#2997ff"},
        "parchment": {"bg": "#f5f5f7", "text": "#1d1d1f", "accent": "#0066cc"}
    }
    theme = themes.get(theme_name, themes["light"])
    background = slide.background
    fill = background.fill
    fill.solid()
    r, g, b = hex_to_rgb(theme["bg"])
    fill.fore_color.rgb = RGBColor(r, g, b)
    return theme

def add_title(slide, text, theme):
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.33), Inches(1.2))
    tf = title_box.text_frame
    tf.text = text
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.font.name = 'Paperlogy'
    p.font.bold = True
    p.font.size = Pt(44)
    r, g, b = hex_to_rgb(theme["text"])
    p.font.color.rgb = RGBColor(r, g, b)

def export_high_fidelity_ppt(json_data_path, output_pptx="presentation.pptx"):
    """
    JSON의 컴포넌트 타입(KPI, Table, Flow 등)을 인식하여 고화질 PPT로 변환합니다.
    """
    if not os.path.exists(json_data_path): return
    with open(json_data_path, 'r', encoding='utf-8') as f:
        slides_data = json.load(f)

    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for item in slides_data:
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        theme = apply_theme(slide, item.get('theme', 'light'))
        add_title(slide, item.get('title', ''), theme)
        
        stype = item.get('type')
        
        # 1. KPI Block 렌더링
        if stype == 'kpi':
            kpis = item.get('kpis', [])
            num_kpis = len(kpis)
            for i, kpi in enumerate(kpis):
                left = Inches(1 + (i * (11.33/num_kpis)))
                box = slide.shapes.add_shape(1, left, Inches(2.5), Inches(3.5), Inches(2.5))
                box.fill.solid()
                box.fill.fore_color.rgb = RGBColor(245, 245, 247) if item.get('theme') != 'dark' else RGBColor(39, 39, 41)
                
                # 가치 텍스트
                tf = box.text_frame
                tf.text = kpi.get('value', '')
                p = tf.paragraphs[0]
                p.alignment = PP_ALIGN.CENTER
                p.font.size = Pt(60)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 102, 204)
                
                # 라벨 텍스트
                p2 = tf.add_paragraph()
                p2.text = kpi.get('label', '')
                p2.alignment = PP_ALIGN.CENTER
                p2.font.size = Pt(18)
                p2.font.color.rgb = RGBColor(29, 29, 31) if item.get('theme') != 'dark' else RGBColor(255, 255, 255)

        # 2. Table 렌더링
        elif stype == 'table':
            rows_data = item.get('rows', [])
            headers = item.get('headers', [])
            rows, cols = len(rows_data) + 1, len(headers)
            table = slide.shapes.add_table(rows, cols, Inches(1), Inches(2.5), Inches(11.33), Inches(4)).table
            for c, h in enumerate(headers):
                table.cell(0, c).text = h
            for r, row in enumerate(rows_data):
                for c, val in enumerate(row):
                    table.cell(r+1, c).text = val

        # 3. Flow 렌더링
        elif stype == 'flow':
            steps = item.get('steps', [])
            for i, step in enumerate(steps):
                left = Inches(1 + (i * 3.5))
                box = slide.shapes.add_shape(1, left, Inches(3.5), Inches(2.5), Inches(1.5))
                box.text = step
                if i < len(steps) - 1:
                    slide.shapes.add_textbox(left + Inches(2.6), Inches(4), Inches(0.8), Inches(0.5)).text = "→"

        # 4. Comparison 렌더링
        elif stype == 'comparison':
            comps = item.get('comparisons', [])
            for i, comp in enumerate(comps):
                left = Inches(1 + (i * 6))
                box = slide.shapes.add_shape(1, left, Inches(2.5), Inches(5), Inches(4))
                box.text = f"{comp.get('label')}\n\n{comp.get('text')}"

        # 5. Default/Hero 렌더링 (이미지 포함)
        else:
            body = slide.shapes.add_textbox(Inches(1.5), Inches(2.5), Inches(10.33), Inches(4))
            body.text_frame.text = item.get('content', '')
            if item.get('image') and os.path.exists(item.get('image')):
                slide.shapes.add_picture(item.get('image'), Inches(5.16), Inches(2.0), height=Inches(3))

    try:
        prs.save(output_pptx)
        print(f"High-Fidelity PPT Export Successful: {output_pptx}")
    except Exception as e:
        print(f"Export Failed: {e}")

if __name__ == "__main__":
    export_high_fidelity_ppt("slides_data.json")
