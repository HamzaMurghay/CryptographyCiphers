import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']

key = random.randint(1, 25)

print(f"""Welcome to the Shift Cipher program!
{'-' * 27}
Here, you can enter any sentence or word in order to encrypt it according to a randomly generated key that is different every time the program is run,
or you can decrypt a given encoded phrase given that you know the key, if you dont know the key you can still try inputting all possible 25 keys to see which one gives a sensible output

(The program encrypts according to the Shift Cipher, also known as Ceasar Cipher)

You are able to use two modes: 

i) Encrypt Mode: Enter any text to see it get encrypted according to the random key selected by the program
ii) Decrypt Mode: Enter a key and encoded text to see it get decrypted according to the key you provided

Enter 'd' to switch to Decrypt Mode or 'e' to switch to Encrypt Mode when asked

You can enter "exit" at any time to exit the program
{'-'* 27}
""")

to_encrypt = ''
to_decrypt = ''

encrypted_output = ''
decrypted_output = ''

mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

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
                decrypted_output += small_letters[(small_letters.index(letter) - key) % 26]
            elif letter in capital_letters:
                decrypted_output += capital_letters[(capital_letters.index(letter) - key) % 26]
            else:
                continue

        print("DECRYPTED OUTPUT:", decrypted_output, "\n\n")
        decrypted_output = ''
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()

    else:
        print("Please enter a valid mode!\n")
        mode = input("Which mode would you like to use?(Encrypt/Decrypt Mode): ").lower()
        continue
