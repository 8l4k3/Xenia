
# 📱 QR Code — Mode Voyage (XENIA)

Ce guide explique comment générer et utiliser les QR codes pour partager facilement votre fiche médicale, même à l’étranger ou sans connexion internet.

---

## 🔹 1. QR code vers la fiche PDF

Script : src/qrcode_pdf.py

Fonction : génère un QR code qui ouvre directement votre fiche médicale en PDF.

Exemple d’utilisation :

python src/qrcode_pdf.py

👉 Résultat :
Un fichier qr_pdf.png est créé.
En scannant ce QR code avec un smartphone, la fiche PDF s’ouvre directement.

---

## 🔹 2. QR code “voyage” (infos essentielles encodées)

Script : src/qrcode_voyage.py

Fonction : encode directement dans le QR code les informations vitales (allergies, traitements interdits, contacts d’urgence).

Exemple d’utilisation :

python src/qrcode_voyage.py

👉 Résultat :
Un fichier qr_voyage.png est créé.
En scannant ce QR code, les infos essentielles apparaissent en clair sur le téléphone, même sans accès au PDF.

---

## 📌 Bonnes pratiques

Toujours générer les deux QR codes :

- qr_pdf.png (pour fiche détaillée)

- qr_voyage.png (pour urgence rapide)

Impression conseillée :

Sur une carte plastifiée format carte bancaire.

Ou sous forme de stickers à coller sur un carnet ou dans le portefeuille.

Traduction mode voyage (prochaines versions) :
Les informations encodées dans qr_voyage.png pourront être générées en plusieurs langues (anglais, espagnol, allemand…) pour être comprises partout.

---
