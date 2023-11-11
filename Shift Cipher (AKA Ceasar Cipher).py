import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

double_keys_enabled = input("Do you wish to have separate keys for lower and uppercase letters?(y/n): ").lower()

while double_keys_enabled not in ['y', 'yes', 'n', 'no']:

    if double_keys_enabled == 'exit':
        exit()
    double_keys_enabled = input("Invalid answer! Please try again: ").lower()

if double_keys_enabled == 'y' or double_keys_enabled == 'yes':
    lowercase_key = random.randint(1, 25)
    uppercase_key = random.randint(1, 25)

elif double_keys_enabled == 'n' or double_keys_enabled == "no":
    key = random.randint(1, 25)

to_encrypt = to_decrypt = ''

encrypted_output = decrypted_output = ''

mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

if mode == "exit":
    exit()


def take_key_input(decryp_key):
    if (not decryp_key.isdigit()) or int(decryp_key) > 25 or int(decryp_key) <= 0:
        if decryp_key == "exit":
            return 0
        else:
            print("Enter a valid key!\n\n")
            return 1


while True:

    if mode == "exit":
        break

    if mode == 'e':
        to_encrypt = input("Enter Sentence/Word to Encrypt: ")

        if to_encrypt.lower() == "exit":
            break

        for letter in to_encrypt:
            if letter == ' ':
                encrypted_output += letter

            elif letter in small_letters and (double_keys_enabled == 'y' or double_keys_enabled == "yes"):
                encrypted_output += small_letters[(small_letters.index(letter) + lowercase_key) % 26]

            elif letter in small_letters:
                encrypted_output += small_letters[(small_letters.index(letter) + key) % 26]

            elif letter in capital_letters and (double_keys_enabled == 'y' or double_keys_enabled == "yes"):
                encrypted_output += capital_letters[(capital_letters.index(letter) + uppercase_key) % 26]

            elif letter in capital_letters:
                encrypted_output += capital_letters[(capital_letters.index(letter) + key) % 26]

            else:
                continue

        print("\nENCRYPTED STRING:", encrypted_output, "\n\n")
        encrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    elif mode == 'd':

        if double_keys_enabled == 'no' or double_keys_enabled == 'n':
            d_key = input("Enter key: ")
            if take_key_input(d_key):
                continue
            elif take_key_input(d_key) == 0:
                break

        else:
            lower_d_key = input("Enter lowercase key: ")

            if take_key_input(lower_d_key):
                continue
            elif take_key_input(lower_d_key) == 0:
                break

            upper_d_key = input("Enter uppercase key: ")

            if take_key_input(upper_d_key):
                continue
            elif take_key_input(upper_d_key) == 0:
                break

        to_decrypt = input("Enter Sentence/Word to Decrypt: ")

        if to_decrypt == "exit":
            break

        for letter in to_decrypt:
            if letter == ' ':
                decrypted_output += letter

            elif letter in small_letters and (double_keys_enabled == 'y' or double_keys_enabled == 'yes'):
                decrypted_output += small_letters[(small_letters.index(letter) - int(lower_d_key)) % 26]

            elif letter in small_letters:
                decrypted_output += small_letters[(small_letters.index(letter) - int(d_key)) % 26]

            elif letter in capital_letters and (double_keys_enabled == 'y' or double_keys_enabled == 'yes'):
                decrypted_output += capital_letters[(capital_letters.index(letter) - int(upper_d_key)) % 26]

            elif letter in capital_letters:
                decrypted_output += capital_letters[(capital_letters.index(letter) - int(d_key)) % 26]

            else:
                continue

        print("\nDECRYPTED STRING:", decrypted_output, "\n\n")
        decrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
    else:
        print("Please enter a valid mode!\n")
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
