# Méthode ROT13
def encrypt_rot13(message):
    """
    Chiffre le message en utilisant la méthode ROT13.
    """
    result = ''
    for char in message:
        if char.isalpha():
            offset = 13 if char.islower() else -13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + offset) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

# Code de Cesar
def encrypt_cesar(message, shift):
    """
    Chiffre le message en utilisant le Code de César avec un décalage donné.
    """
    result = ''
    for char in message:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

# Code de Vigenere
def encrypt_vigenere(message, key):
    """
    Chiffre le message en utilisant le Code de Vigenère avec une clé donnée.
    """
    result = ''
    key = key.upper()
    
    for i, char in enumerate(message):
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            key_char = key[i % len(key)].upper()
            
            if key_char.isalpha():
                result += chr((ord(char) - offset + ord(key_char) - ord('A')) % 26 + offset)
            else:
                print("La clé doit contenir uniquement des lettres alphabétiques.")
                return ''  # Quitter la fonction si la clé n'est pas valide
        else:
            result += char
    return result

# Carré de Polybe
def encrypt_polybius(message):
    """
    Chiffre le message en utilisant le Carré de Polybe.
    """
    polybius_square = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
                      'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '25',
                      'K': '31', 'L': '32', 'M': '33', 'N': '34', 'O': '35',
                      'P': '41', 'Q': '42', 'R': '43', 'S': '44', 'T': '45',
                      'U': '51', 'V': '52', 'W': '53', 'X': '54', 'Y': '55',
                      'Z': '00', ' ': ' '}
    result = ''
    for char in message.upper():
        if char in polybius_square:
            result += polybius_square[char] + ' '
    return result.strip()

# Exemple d'utilisation avec choix de l'algorithme
message = input("Entrez un message: ")
choice = input("Choisissez un algorithme (ROT13, Cesar, Vigenere, Polybe): ").lower()

# Appel de la fonction appropriée en fonction du choix de l'utilisateur
if choice == 'rot13':
    encrypted_message = encrypt_rot13(message)
    print("Message chiffré en ROT13:", encrypted_message)
elif choice == 'cesar':
    shift = int(input("Entrez le décalage pour le Code de César: "))
    encrypted_message = encrypt_cesar(message, shift)
    print("Message chiffré en Code de César:", encrypted_message)
elif choice == 'vigenere':
    key = input("Entrez la clé pour le Code de Vigenère: ")
    encrypted_message = encrypt_vigenere(message, key)
    print("Message chiffré en Code de Vigenère:", encrypted_message)
elif choice == 'polybe':
    encrypted_message = encrypt_polybius(message)
    print("Message chiffré avec le Carré de Polybe:", encrypted_message)
else:
    print("Choix d'algorithme non reconnu. Veuillez choisir parmi ROT13, Cesar, Vigenere, Polybe.")
