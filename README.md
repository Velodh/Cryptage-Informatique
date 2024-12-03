# Cryptage-Informatique

Pour bien structurer et organiser ton projet sur GitHub, voici comment tu pourrais présenter tout cela avec un README qui explique ton code et un exemple pour l'organisation des fichiers :

Projet de Cryptographie : Implémentation de Méthodes de Chiffrement
Introduction
Ce projet explore les bases de la cryptographie classique à travers l'implémentation de quatre méthodes de chiffrement populaires : ROT13, Code de César, Code de Vigenère et Carré de Polybe. Il a été réalisé dans le cadre de ma spécialité Numérique et Sciences de l'Informatique (NSI) en classe de Première. L'objectif est de mieux comprendre les concepts fondamentaux de la cryptographie tout en appliquant des compétences en programmation Python.

Contenu du Projet
Le programme permet de :

Chiffrer des messages à l'aide de quatre algorithmes.
Offrir une interface en ligne de commande conviviale pour que l'utilisateur puisse choisir son algorithme, entrer son message, et obtenir le résultat chiffré.
Les Méthodes de Chiffrement
ROT13 :

Méthode de substitution qui décale chaque lettre de 13 positions dans l'alphabet.
Particularité : l'encodage est identique au décodage.
Code de César :

Méthode de substitution où l'utilisateur définit le décalage (par exemple : +3 décalera chaque lettre de 3 positions).
Permet une personnalisation de la clé de chiffrement.
Code de Vigenère :

Méthode polyalphabétique où chaque lettre du message est décalée selon une clé fournie par l'utilisateur.
La clé est répétée autant que nécessaire pour correspondre à la longueur du message.
Carré de Polybe :

Méthode qui associe chaque lettre à une paire de chiffres en utilisant une grille 5x5 (par exemple, A=11, B=12, etc.).
Simplicité et efficacité pour des messages courts.
Exemple d'Utilisation
L'utilisateur exécute le programme :
bash
Copier le code
python cryptography.py
L'utilisateur entre son message :
yaml
Copier le code
Entrez un message : Bonjour tout le monde
L'utilisateur choisit une méthode de chiffrement (par exemple ROT13) :
java
Copier le code
Choisissez un algorithme (ROT13, Cesar, Vigenere, Polybe) : rot13
Résultat :
mathematica
Copier le code
Message chiffré en ROT13 : Obawbhe gbhg yr zbaqr
Structure des Fichiers
cryptography.py : Contient le code Python pour les quatre algorithmes de chiffrement.
README.md : Explications du projet, instructions d'installation et d'utilisation.
Exemples :
Ajoute des fichiers d'exemple avec des cas testés, comme example_input.txt et example_output.txt pour illustrer les résultats.
Installation
Clone ce dépôt :
bash
Copier le code
git clone https://github.com/votre-utilisateur/projet-cryptographie.git
cd projet-cryptographie
Assurez-vous d'avoir Python installé :
bash
Copier le code
python --version
Exécutez le programme :
bash
Copier le code
python cryptography.py
Fonctionnement du Code
ROT13
Implémenté avec un décalage fixe de 13. Utilise la fonction ord pour convertir les caractères et appliquer le décalage.
Code de César
Prend un décalage (positif ou négatif) fourni par l'utilisateur. Simple et efficace pour les débutants en cryptographie.
Code de Vigenère
Utilise une clé répétée pour calculer le décalage de chaque caractère.
Carré de Polybe
Utilise une grille fixe 5x5 pour mapper les lettres à des coordonnées numériques.
Améliorations Futures
Ajout de la fonctionnalité de déchiffrement pour chaque méthode.
Support des caractères spéciaux et des chiffres pour les méthodes (autres que ROT13).
Intégration d'une interface graphique simple.
Aperçu du Code
python
Copier le code
# Exemple pour la méthode ROT13
def encrypt_rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            offset = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result
Conclusion
Ce projet m'a permis d'explorer des algorithmes de cryptographie tout en consolidant mes compétences en Python. Il constitue une base solide pour des projets futurs dans le domaine de la sécurité informatique et du développement logiciel.
