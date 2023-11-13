small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

double_keys_enabled = input("Do you wish to have separate keys for lower and uppercase letters?(y/n): ").lower()

while double_keys_enabled not in ['y', 'yes', 'n', 'no', 'exit']:
    double_keys_enabled = input("Invalid answer! Please try again: ").lower()

if double_keys_enabled == "exit":
    exit()

lowercase_key = uppercase_key = 0

if double_keys_enabled == 'y' or double_keys_enabled == 'yes':

    double_keys_enabled = True

    lowercase_key = input("Enter lowercase key for encryption: ")
    while not (lowercase_key.isdigit()) or (int(lowercase_key) % 26 == 0):
        if lowercase_key == "exit":
            exit()
        lowercase_key = input("Enter a valid key! (It should not be 0 or a multiple of 26) ")

    lowercase_key = int(lowercase_key) % 26

    uppercase_key = input("Enter uppercase key for encryption: ")
    while not (uppercase_key.isdigit()) or (int(uppercase_key) % 26 == 0):
        if uppercase_key == "exit":
            exit()
        uppercase_key = input("Enter a valid key! (It should not be 0 or a multiple of 26) ")

    uppercase_key = int(uppercase_key) % 26

else:
    double_keys_enabled = False

    lowercase_key = uppercase_key = input("Enter key for encryption: ")
    while not (lowercase_key.isdigit()) or (int(lowercase_key) % 26 == 0):
        if lowercase_key == "exit":
            exit()
        lowercase_key = input("Enter a valid key! (It should not be 0 or a multiple of 26) ")

    lowercase_key = uppercase_key = int(lowercase_key) % 26

mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()


def take_key_input(specifier_string: str = ''):
    decrypt_key = input(f"Enter {specifier_string}key for decryption: ")

    while not (decrypt_key.isdigit()) or (int(decrypt_key) % 26 == 0):

        if decrypt_key.lower() == "exit":
            exit()
        else:
            decrypt_key = input("Enter a valid key!(It should not be 0 or multiples of 26) ")

    return decrypt_key


def encrypt_or_decrypt(string_to_crypt, encryption: bool):
    crypted_string = ''

    if encryption:
        for letter in string_to_crypt:
            if letter in small_letters:
                crypted_string += small_letters[(small_letters.index(letter) + lowercase_key) % 26]
            elif letter in capital_letters:
                crypted_string += capital_letters[(capital_letters.index(letter) + uppercase_key) % 26]
            else:
                crypted_string += letter
    else:
        for letter in string_to_crypt:
            if letter in small_letters:
                crypted_string += small_letters[(small_letters.index(letter) - int(lower_d_key)) % 26]
            elif letter:
                crypted_string += capital_letters[(capital_letters.index(letter) - int(upper_d_key)) % 26]
            else:
                crypted_string += letter
    return crypted_string


while True:
    if mode == "exit":
        break

    elif mode == 'e':
        to_encrypt = input("Enter Sentence/Word to Encrypt: ")
        if to_encrypt.lower() == "exit":
            break

        print(f"\nENCRYPTED STRING: {encrypt_or_decrypt(to_encrypt, True)} \n")
        mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    elif mode == 'd':

        if double_keys_enabled:
            lower_d_key = take_key_input('lowercase ')
            upper_d_key = take_key_input('uppercase ')
        else:
            lower_d_key = upper_d_key = take_key_input()

        to_decrypt = input("Enter Sentence/Word to Decrypt: ")
        if to_decrypt == "exit":
            break

        print(f"\nDECRYPTED STRING: {encrypt_or_decrypt(to_decrypt, False)} \n")
        mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    else:
        print("Please enter a valid mode!\n")
        mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
