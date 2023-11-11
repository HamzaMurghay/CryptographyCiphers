import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

double_keys_enabled = input(
    "Do you wish to have separate keys for lower and uppercase letters during encryption?(y/n): ").lower()

if double_keys_enabled == 'y' or double_keys_enabled == 'yes':
    lowercase_key = random.randint(1, 25)
    uppercase_key = random.randint(1, 25)
elif double_keys_enabled == 'n' or double_keys_enabled == "no":
    key = random.randint(1, 25)

while double_keys_enabled not in ['y', 'yes', 'n', 'no']:

    double_keys_enabled = input("Invalid answer! Please try again: ")

    if double_keys_enabled == 'y' or double_keys_enabled == 'yes':
        lowercase_key = random.randint(1, 25)
        uppercase_key = random.randint(1, 25)
    elif double_keys_enabled == 'n' or double_keys_enabled == "no":
        key = random.randint(1, 25)

to_encrypt = ''
to_decrypt = ''

encrypted_output = ''
decrypted_output = ''

mode = input("\nWhich mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

while True:

    if mode == "exit": break

    if mode == 'e':
        to_encrypt = input("Enter Sentence/Word to Encrypt: ")

        if to_encrypt.lower() == "exit": break

        for letter in to_encrypt:
            if letter == ' ':
                encrypted_output += letter

            elif letter in small_letters and (double_keys_enabled == "n" or double_keys_enabled == "no"):
                encrypted_output += small_letters[(small_letters.index(letter) + key) % 26]

            elif letter in small_letters and (double_keys_enabled == 'y' or double_keys_enabled == "yes"):
                encrypted_output += small_letters[(small_letters.index(letter) + lowercase_key) % 26]

            elif letter in capital_letters and (double_keys_enabled == "n" or double_keys_enabled == "no"):
                encrypted_output += capital_letters[(capital_letters.index(letter) + key) % 26]

            elif letter in capital_letters and (double_keys_enabled == 'y' or double_keys_enabled == "yes"):
                encrypted_output += capital_letters[(capital_letters.index(letter) + uppercase_key) % 26]

            else:
                continue

        print("ENCRYPTED STRING:", encrypted_output, "\n\n")
        encrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    elif mode == 'd':
        d_key = input("Enter key: ")

        if (not d_key.isdigit()) or int(d_key) > 25 or int(d_key) <= 0:
            if d_key == "exit":
                break
            else:
                print("Enter a valid key!\n\n")
                continue

        to_decrypt = input("Enter Sentence/Word to Decrypt: ")

        if to_decrypt == "exit": break

        for letter in to_decrypt:
            if letter == ' ':
                decrypted_output += letter
            elif letter in small_letters:
                decrypted_output += small_letters[(small_letters.index(letter) - int(d_key)) % 26]
            elif letter in capital_letters:
                decrypted_output += capital_letters[(capital_letters.index(letter) - int(d_key)) % 26]
            else:
                continue

        print("DECRYPTED STRING:", decrypted_output, "\n\n")
        decrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    else:
        print("Please enter a valid mode!\n")
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
        continue
