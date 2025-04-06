# ⏱️ Chrono Terminal - Python Stopwatch

Un petit script Python tout simple pour faire office de **chronomètre dans le terminal**, avec fonctions de pause, reset, export, et arrêt propre via le clavier.

---

## ⚙️ Fonctionnalités

- ✅ Affichage du temps écoulé en direct (hh:mm:ss)
- ⏸️ Pause / Reprise avec la touche `²`
- 🔄 Réinitialisation (reset) avec `-` (uniquement quand en pause)
- 💾 Export du chrono dans un fichier `.txt` via `E`
- 📁 Les fichiers exportés sont automatiquement enregistrés dans le dossier `Historique/`
- ❌ Fermeture propre via `&` (quand en pause)
- 📌 Sauvegarde automatique du temps dans `chrono.txt`

---

## 🖥️ Utilisation avec OBS Studio

Le script écrit en continu dans un fichier `chrono.txt`, qui peut être **affiché en direct dans OBS** grâce à l'objet texte !

### 🔧 Étapes pour afficher le chrono dans OBS :

1. Dans OBS, ajoute une **source** : `Texte (GDI+)`.
2. Coche l’option **"Lire à partir d’un fichier"**.
3. Sélectionne le fichier `chrono.txt` (créé par le script).
4. Le chrono s’affiche en live dans la scène ! 

⚠️ L’affichage se mettra à jour automatiquement toutes les ~0.2 secondes.

---

## 🎮 Commandes Clavier

| Touche | Action                      | Condition              |
|--------|-----------------------------|------------------------|
| `²`    | Pause / Reprendre           | À tout moment          |
| `-`    | Réinitialiser le chrono     | Uniquement en pause    |
| `E`    | Exporter vers un `.txt`     | À tout moment          |
| `&`    | Quitter proprement          | Uniquement en pause    |

---

## 🚀 Lancer le script
``python chrono.py``

### 📁 Dossiers & fichiers
chrono.txt → fichier de sauvegarde automatique (utilisé par OBS si souhaité)

Historique/ → contiendra les exports du chrono au format :
``Chrono du 06-04-2025 17-52-41.txt``

## 🧪 Prérequis

- Python 3.x
- Module `keyboard` (pour la détection des touches)

### Installation du module :
bash
```pip install keyboard```

🧠 Auteurs & crédit
🛠️ Script développé avec amour par [DBZ-Z]

💬 Besoin de fonctions supplémentaires ? Ouvre une issue ou envoie une PR !

# ⚡ Disclaimer
Ce script fonctionne dans un terminal local. Il peut nécessiter des droits admin pour détecter les touches (notamment sous Windows). N’est pas compatible avec les notebooks ou environnements en ligne.
