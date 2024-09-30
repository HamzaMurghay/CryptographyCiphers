import os


# Randomness methods setup --------------------------------------------------------------------------------------

lfsr_bit_len = 5
seed = "01101"

taps_state = list(map(int, seed))


def LFSR():
    new_tap = taps_state[4] ^ taps_state[2]
    for idx in range(len(taps_state)-1, 0, -1):
        taps_state[idx] = taps_state[idx-1]
    taps_state[0] = new_tap

    return int("".join(map(str, taps_state)), 2)


def OS_based_randomness(plaintext_length):
    rand = str(os.urandom(plaintext_length))[2:].replace("\\", "")
    return rand


# Encryption/Decryption setup -----------------------------------------------------------------------------------


def encrypt(plaintext: str, r_method):

    ciphertext = ""
    pt_len = len(plaintext)

    if plaintext == "exit":
        exit()
        
    elif r_method == '1':
        key = []

        for i in range(pt_len):
            key.append(LFSR())
            ciphertext += chr(key[i] ^ ord(plaintext[i]))

        return ciphertext, key  # key is returned as well and needs to be delivered to the recipient over a secure channel
    else:
        key = OS_based_randomness(pt_len)

        for i in range(pt_len):
            ciphertext += chr(ord(key[i]) ^ ord(plaintext[i])) + ' '

        return ciphertext.strip(), key  # key is returned as well and needs to be delivered to the recipient over a secure channel


while True:
    randomness_method = input("Would you like to generate key stream with LFSR or OS-based randomness? (Choose 1 or 2) ")

    if randomness_method == "exit":
        break
    elif randomness_method == '1' or randomness_method == '2':
        print(encrypt(input("Enter plaintext to encrypt: "), randomness_method))
    else:
        print("Enter a valid mode!")
