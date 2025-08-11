# 🟦 XENIA  
**Carte numérique personnelle pour la gestion des allergies alimentaires, médicamenteuses et cosmétiques**  

## 🎯 Objectif du projet
XENIA permet à toute personne allergique ou atteinte d’une condition médicale spécifique de disposer d’une fiche claire, lisible et partageable (via QR code ou impression), regroupant :  
- Allergies environnementales
- Allergies alimentaires
- Allergies médicamenteuses (substance active, excipient)  
- Allergies cosmétiques  
- Allergies croisées connues et/ou fortement possibles
- Maladies et traitements médicaux  
- Informations médicales utiles (groupe sanguin, contacts d’urgence…)  

Le tout **hors ligne** pour respecter la vie privée.

---

## ✅ Public visé
- Enfants (via les parents)  
- Personnes allergiques nomades ou en voyage  
- Personnes étrangères ou muettes ayant besoin de montrer leurs restrictions  
- Aidants, professionnels, établissements accueillant du public  

---

## 💡 Fonctionnalités prévues (v1)
- Modèle de fiche personnalisable aux formats **Word (.docx)**, **PDF** et **Markdown**
- QR code généré localement pour partager la fiche
- Base documentaire sur :
  - Allergènes les plus fréquents
  - Allergies croisées connues (sources officielles)
- Fonctionnement local uniquement :  
  Pas de serveur, pas de base de données centralisée  
  Stockage uniquement sur l’appareil de l’utilisateur

---

## 📥 Téléchargement des modèles
📂 **Dossier Templates** : [templates/](./templates)  

- [📄 Modèle Word – XENIA_fiche_utilisateur.docx](./templates/XENIA_fiche_utilisateur.docx)  
- [📄 Modèle PDF – XENIA_fiche_utilisateur.pdf](./templates/XENIA_fiche_utilisateur.pdf)  
- [📝 Modèle Markdown – fiche_utilisateur.md](./fiche_utilisateur.md)  

---

## 📘 Guide d’utilisation rapide
1. **Téléchargez** le modèle Word ou Markdown  
2. **Remplissez** vos informations  
3. **Enregistrez** en PDF (si vous avez utilisé Word ou Markdown)  
4. **Imprimez** ou gardez sur votre téléphone  
5. **Générez** un QR code localement →  [`docs/QRcode.md`](/docs/QRcode.md) 
---

## 📚 Sources officielles utilisées
Voir [/sources/sources_officielles.md](/sources/sources_officielles.md)  
> Nous nous basons uniquement sur des ressources officielles et fiables (agences de santé, publications scientifiques en accès libre).  

---

## ⚠️ Clause de non-responsabilité
Voir [DISCLAIMER.md](./DISCLAIMER.md)  
> Ce document ne remplace pas un avis médical. Il est conçu comme un aide-mémoire personnel.

---

## 📦 Structure du dépôt

XENIA/


├── README.md ← Présentation du projet

├── ROADMAP.md ← Suivi de l’avancement

├── DISCLAIMER.md ← Clause de non-responsabilité médicale

├── sources/ ← Sources & Références Bibliographiques 

│   └── sources_officielles.md ← Sources Bibliographiques       

│   └── annexes.md ← Références Bibliographiques         
 
├── docs/ ← Guide pour les allergies croisées & générer un QR code localement 

│   ├── allergies_croisees.md

│   └── QRcode.md

├── templates/  ← Modèle de fiche personnalisable  

│   ├── XENIA_fiche_utilisateur.md ← Markdown modèle fiche utilisateur      

│   ├── XENIA_fiche_utilisateur.docx ← Word modèle    

│   └── XENIA_fiche_utilisateur.pdf  ← PDF modèle   


---

## 🔄 Idées d’évolution possibles
- Traductions multi-langues
- Générateur de fiche via page HTML locale
- Application web offline
- Option d’impression PDF stylisée
- Système d’icônes pour simplifier la lecture

---

## 🧠 Inspirations & principes
- **Accessibilité** : facile à remplir, à comprendre, à montrer  
- **Sécurité** : pas de collecte de données  
- **Modularité** : possibilité d’étendre à d’autres besoins (asthme, diabète, déficit en G6PD…)  
- **Open Source** : projet communautaire que chacun peut adapter  

---

## 📜 Licence
Projet sous licence **MIT** — libre d’utilisation, modification et partage.

---
