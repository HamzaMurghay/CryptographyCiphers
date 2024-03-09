small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(plaintext: str):
    if plaintext == "exit":
        exit()

    keystream = ''
    ciphertext = ''
    for letter_position in range(len(plaintext)):
        keystream += key[letter_position % (len(key))]
        current_key_pos = small_letters.index(keystream[letter_position])

        if plaintext[letter_position] in small_letters:
            ciphertext += small_letters[(current_key_pos + small_letters.index(plaintext[letter_position])) % 26]
        elif plaintext[letter_position] in capital_letters:
            ciphertext += capital_letters[(current_key_pos + capital_letters.index(plaintext[letter_position])) % 26]
        else:
            ciphertext += plaintext[letter_position]
    print(f"\nENCRYPTED CIPHERTEXT: {ciphertext}")


def decrypt(ciphertext: str):
    if ciphertext == "exit":
        exit()

    keystream = ''
    plaintext = ''

    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.replace("\n", "")
    ciphertext = ciphertext.replace("\t", "")

    for letter_position in range(len(ciphertext)):
        keystream += d_key[letter_position % len(d_key)]
        current_key_pos = small_letters.index(keystream[letter_position])

        if ciphertext[letter_position] in small_letters:
            plaintext += small_letters[(small_letters.index(ciphertext[letter_position]) - current_key_pos) % 26]
        elif ciphertext[letter_position] in capital_letters:
            plaintext += capital_letters[(capital_letters.index(ciphertext[letter_position]) - current_key_pos) % 26]
        else:
            plaintext += ciphertext[letter_position]
    print(f"\nDECRYPTED PLAINTEXT: {plaintext}")


def enter_key(input_string: str):
    inp_key = input(input_string).lower()

    while not inp_key.replace(" ", '').isalpha():
        print("Invalid! Key must be a series of alphabetical letters")
        inp_key = input("Re-enter the key: ")
    if inp_key == "exit":
        exit()
    return inp_key.replace(" ", '').lower()


key = enter_key("Enter encryption key: ")

while True:
    mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    if mode == "exit":
        break
    elif mode == 'e':
        encrypt(input("Enter plaintext to encrypt: "))
    elif mode == 'd':
        d_key = enter_key("Enter decryption key: ")
        decrypt(input("Enter ciphertext to decrypt: "))
    else:
        print("Enter a valid mode!")
