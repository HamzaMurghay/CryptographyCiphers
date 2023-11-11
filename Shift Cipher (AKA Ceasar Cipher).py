import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

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
            elif letter in small_letters:
                encrypted_output += small_letters[(small_letters.index(letter) + key) % 26]
            elif letter in capital_letters:
                encrypted_output += capital_letters[(capital_letters.index(letter) + key) % 26]
            else:
                continue

        print("ENCRYPTED OUTPUT:", encrypted_output, "\n\n")
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

        print("DECRYPTED OUTPUT:", decrypted_output, "\n\n")
        decrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    else:
        print("Please enter a valid mode!\n")
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
        continue
