# src/qrcode_voyage.py
import qrcode

def generate_travel_qr(info_text, output_path="qr_voyage.png"):
    """
    Génère un QR code contenant directement les infos essentielles.
    """
    img = qrcode.make(info_text)
    img.save(output_path)
    print(f"✅ QR code voyage généré → {output_path}")

if __name__ == "__main__":
    # Exemple : infos encodées directement
    infos = """
    🔹 XENIA - Fiche médicale voyage
    Nom: Jean Dupont
    Allergies: Latex, Kiwi, Arachide
    Médicaments interdits: Aspirine
    Contact urgence: +33 6 XX XX XX XX 
    """

    generate_travel_qr(infos)
