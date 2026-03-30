from docxtpl import DocxTemplate
import os

TEMPLATE_MAP = {
    "bda": "templates/bda.docx",
    "marketing": "templates/marketing.docx",
    "hr": "templates/hr.docx"
}

def generate_offer(data):
    template_path = TEMPLATE_MAP[data["template_key"]]
    
    doc = DocxTemplate(template_path)
    
    output_path = f"outputs/{data['name'].replace(' ', '_')}.docx"
    
    doc.render(data)
    doc.save(output_path)
    
    return output_path