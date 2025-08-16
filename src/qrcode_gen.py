import qrcode

# Texte ou lien à encoder
data = "https://xenia.local/fiche_utilisateur.pdf"

# Génération du QR code
img = qrcode.make(data)

# Sauvegarde en image
img.save("mon_qrcode.png")

print("✅ QR code généré : mon_qrcode.png")
