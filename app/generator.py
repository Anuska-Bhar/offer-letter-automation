from docxtpl import DocxTemplate
import os

TEMPLATE_MAP = {
    "bda": "templates/bda.docx",
    "marketing": "templates/marketing.docx",
    "hr": "templates/hr.docx"
}

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_offer(data):
    template_path = TEMPLATE_MAP.get(data["template_key"])

    if not template_path:
        raise ValueError("Invalid template_key")

    doc = DocxTemplate(template_path)

    filename = f"{data['name'].replace(' ', '_')}_{data['id']}_{data['template_key']}.docx"
    output_path = os.path.join(OUTPUT_DIR, filename)

    doc.render(data)
    doc.save(output_path)

    return output_path