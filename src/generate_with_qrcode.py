import os
import qrcode
from weasyprint import HTML
from docx import Document

# === CONFIG ===
INPUT_FILE = "docs/fiche_utilisateur.md"
OUTPUT_DIR = "output/"

def md_to_html(md_text):
    """Conversion très simple Markdown → HTML minimal"""
    return f"<html><body>{md_text.replace('\n', '<br>')}</body></html>"

def generate_pdf(md_file, pdf_file):
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    html_content = md_to_html(md_text)
    HTML(string=html_content).write_pdf(pdf_file)

def generate_docx(md_file, docx_file):
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    doc = Document()
    for line in md_text.splitlines():
        doc.add_paragraph(line)
    doc.save(docx_file)

def generate_qrcode(data, qrcode_file):
    img = qrcode.make(data)
    img.save(qrcode_file)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(INPUT_FILE))[0]
    pdf_file = os.path.join(OUTPUT_DIR, f"{base_name}.pdf")
    docx_file = os.path.join(OUTPUT_DIR, f"{base_name}.docx")
    qrcode_file = os.path.join(OUTPUT_DIR, f"{base_name}.png")

    # Générer les documents
    generate_pdf(INPUT_FILE, pdf_file)
    generate_docx(INPUT_FILE, docx_file)

    # Associer QR code (ici on encode juste le nom du fichier PDF)
    generate_qrcode(f"{base_name}.pdf", qrcode_file)

    print(f"✅ Fichiers générés : {pdf_file}, {docx_file}, {qrcode_file}")
