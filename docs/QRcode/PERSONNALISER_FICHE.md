# Tutoriel : Personnaliser les fiches XENIA 

Ce guide explique comment modifier le contenu des fiches, générer les QR codes, et produire les PDF et DOCX.

---

## 1️⃣ Modifier le contenu des fiches

- Les fiches sont des fichiers **Markdown (`.md`)** situés dans `/docs/` ou `/src/md/`.  
- Ouvre le fichier correspondant à la fiche à personnaliser, par exemple :  

/docs/fiche_utilisateur.md

- Les sections sont organisées avec des titres Markdown (`#`, `##`, `###`).  
- Pour modifier le texte, ajouter des listes, tableaux ou liens.

---

## 2️⃣ Ajouter ou modifier un QR code

- Les QR codes sont générés via **Python** avec le script `generate_qrcode_xenia.py`.  
- Dans le script, modifiez la variable `data` pour le lien ou texte à encoder :  
```python
data = "https://xenia.local/fiche_utilisateur.pdf"

- Lancer le script pour générer le QR code :

python generate_docs_xenia.py

Le fichier mon_qrcode.png sera créé. On pourra l’insérer dans ton PDF ou DOCX.

---

