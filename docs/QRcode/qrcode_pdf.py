# src/qrcode_pdf.py
import qrcode
import os

def generate_qr_for_pdf(pdf_path, output_path="qr_pdf.png"):
    """
    Génère un QR code pointant vers le fichier PDF.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"⚠️ Le fichier {pdf_path} n'existe pas.")

    # Utilise un chemin absolu pour que le QR code soit lisible
    abs_path = os.path.abspath(pdf_path)
    data = f"file://{abs_path}"

    img = qrcode.make(data)
    img.save(output_path)
    print(f"✅ QR code généré pour {pdf_path} → {output_path}")

if __name__ == "__main__":
    # Exemple : génère un QR code vers une fiche PDF
    generate_qr_for_pdf("output/fiche_utilisateur.pdf")
