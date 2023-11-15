import math

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(plaintext):
    if plaintext.lower() == "exit":
        exit()

    encrypted_string = ''

    for letter in plaintext:
        if letter in small_letters:
            encrypted_string += small_letters[(key1 * (small_letters.index(letter)) + key2) % 26]
        elif letter in capital_letters:
            encrypted_string += capital_letters[(key1 * (capital_letters.index(letter)) + key2) % 26]
        else:
            encrypted_string += letter
    return encrypted_string


def decrypt(ciphertext):
    if ciphertext.lower() == "exit":
        exit()

    decrypted_string = ''

    for letter in ciphertext:
        if letter in small_letters:
            decrypted_string += small_letters[(int(d_key1) * (small_letters.index(letter)-int(d_key2))) % 26]
        elif letter in capital_letters:
            decrypted_string += capital_letters[(int(d_key1) * (capital_letters.index(letter)-int(d_key2))) % 26]
        else:
            decrypted_string += letter
    return decrypted_string


def find_multiplicative_inverse(key_a):
    if math.gcd(key_a, 26) != 1:
        return -1
    else:
        for num in range(key_a):
            result = (num*26+1)/key_a
            if result.is_integer():
                return str(int(result))


def take_key_input(request_text: str, encryption: bool):
    crypt_key = input(f"{request_text}")

    while not crypt_key.isdigit() or int(crypt_key) % 2 == 0 or int(crypt_key) % 13 == 0:

        if crypt_key.lower() == "exit":
            exit()
        elif not crypt_key.isdigit() or int(crypt_key) == 0:
            crypt_key = input("Invalid key! Please re-enter the key: ")
        else:
            while find_multiplicative_inverse(int(crypt_key)) == -1:
                print('This is an imperfect key!(i.e multiple letters will encrypt/decrypt to the same letter)')
                print('NOTE: Avoid entering 0, multiples of 2 or multiples of 13 in order to avoid this\n')
                crypt_key = input("Please re-enter key: ")
    if encryption:
        return int(crypt_key)
    else:
        return find_multiplicative_inverse(int(crypt_key))


def validate_key(print_string):
    key = input("\n"+print_string)

    while not key.isdigit():
        if key.lower() == "exit":
            exit()
        key = input("Invalid key! Please re-enter the key: ")
    return int(key) % 26


key1 = take_key_input("Enter A coefficient(key) for encryption: ", True)

key2 = validate_key("Enter B coefficient(key) for encryption: ")

while True:
    mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    if mode == "exit":
        break
    elif mode == 'e':
        print(f"\nEncrypted Output: {encrypt(input('Enter sentence/word to encrypt: '))}")
    elif mode == 'd':
        d_key1 = take_key_input('Enter A coefficient(key) used during encryption : ', False)
        d_key2 = validate_key("Enter B coefficient(key) used during encryption: ")

        print(f"\nDecrypted Output: {decrypt(input('Enter sentence/word to decrypt: '))}")
    else:
        print("Enter a valid mode!")

# set of A keys with no M.I for mod 26: {2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24}
