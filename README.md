# GueCotDDoS

**Créé par Ezio**

Un script Python pour effectuer différentes types d'attaques de flood (HTTP, TCP, UDP) avec la possibilité d'utiliser des proxys et des socks pour masquer l'origine des requêtes.

## ⚠️ Avertissement

**Important :** L'utilisation de ce script pour effectuer des attaques DDoS est **illégale** et **contrary to l'éthique**. Assurez-vous de **respecter toutes les lois et réglementations** en vigueur dans votre pays. Toute utilisation abusive peut entraîner de graves conséquences légales.

---

## 📋 Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
  - [Installation des dépendances système](#installation-des-dépendances-système)
  - [Installation des dépendances Python](#installation-des-dépendances-python)
- [Utilisation](#utilisation)
- [Téléchargement des Proxys](#téléchargement-des-proxys)
- [Contribution](#contribution)
- [Licence](#licence)

---

## 🚀 Fonctionnalités

- **HTTP Flood** : Type d'attaque recommandé.
- **TCP Flood** : Nécessite des privilèges administrateur.
- **UDP Flood** : Nécessite des privilèges administrateur.
- **Support Proxy/Socks** : Utilisation de proxys pour masquer l'origine des requêtes.
- **Téléchargement Automatique des Proxys** : Depuis différentes sources, y compris votre propre liste sur GitHub.
- **Interface Améliorée** : Interface utilisateur colorée et interactive avec des animations de chargement.

---

## 🔧 Prérequis

- **Système d'exploitation** : Linux (Arch-based recommandé)
- **Python** : Version 3.6 ou supérieure

---

## 📦 Installation

### 1. Cloner le Dépôt

```bash
git clone https://github.com/ErrorNoName/G-G-D.git
```

N'hésitez pas à me faire savoir si vous avez besoin d'autres ajustements ou d'informations supplémentaires !
## 🛠️ Utilisation

Après avoir installé les dépendances, vous pouvez exécuter le script :

```bash
python GueCot.py
```

Suivez les instructions à l'écran pour configurer et démarrer l'attaque.

---

## 🌐 Téléchargement des Proxys

Le script permet de télécharger des proxys depuis différentes sources. Vous avez également la possibilité d'ajouter votre propre liste de proxys hébergée sur GitHub.

### Ajouter HugProxy depuis GitHub

Lors de la sélection de la source de proxys, choisissez l'option `2` pour télécharger les proxys depuis votre liste GitHub :

```
Télécharger depuis:
0 - free-proxy-list.net (meilleur)
1 - inforge.net
2 - HugProxy (GitHub)
>> 2
```

Assurez-vous que votre fichier `HugProxy.txt` sur GitHub est au format `IP:Port` par ligne.

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez ouvrir une issue ou soumettre une pull request.

---

## 📜 Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

---

### 3. Notes Supplémentaires

- **Personnalisation du README** : Remplacez `https://github.com/votre-utilisateur/G-G-D.git` par l'URL réelle de votre dépôt GitHub.
- **Licence** : Assurez-vous d'ajouter un fichier `LICENSE` approprié si vous souhaitez spécifier une licence pour votre projet.
- **Sécurité** : Rappelez-vous toujours des implications légales et éthiques de l'utilisation de tels scripts.

---

### 4. Exemple de Fichier `HugProxy.txt`

Assurez-vous que votre fichier `HugProxy.txt` hébergé sur GitHub suit ce format :

```plaintext
192.168.1.1:8080
203.0.113.5:3128
...
```

Chaque ligne doit contenir une adresse IP suivie d'un port, séparés par un deux-points (`:`).

---

### 5. Installation des Dépendances via Pacman

Pour résumer, voici les commandes à exécuter pour installer les dépendances système nécessaires :

```bash
sudo pacman -S python-rich
sudo pacman -S python-pysocks
sudo pacman -S python-scapy
```

---

### 6. Installation des Dépendances Python

Après avoir installé les dépendances système, activez votre environnement virtuel et installez les dépendances Python :

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
