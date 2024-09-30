import sys

with open(sys.argv[1], "r") as f:
    file = f.read()

file = file.upper()
file = file.replace(" ", "")
file = file.replace("\t", "")
file = file.replace("\n", "")

ioc = 0


def convert_to_data_format(sample_text, grp_size):
    temp_frequency_list = []
    duplicate_checker = []

    for char_index in range(len(sample_text) - grp_size + 1):
        cur_group = sample_text[char_index: char_index + grp_size]
        if cur_group not in duplicate_checker:
            temp_frequency_list.append((cur_group, sample_text.count(cur_group)))
            duplicate_checker.append(cur_group)

    return temp_frequency_list


def return_ioc(sample_text):
    index_of_coincidence = 0

    cipher_alpha_frequencies = convert_to_data_format(sample_text, 1)
    total_letters = sum(frequency[1] for frequency in cipher_alpha_frequencies)

    for letter in cipher_alpha_frequencies:
        index_of_coincidence += letter[1] / total_letters * (letter[1] - 1) / (total_letters - 1)

    return index_of_coincidence


def return_slice_ioc():
    index_of_coincidence = 0

    group_texts = [''] * group_size

    for group_character in range(group_size):
        iterator = 0
        while iterator + group_character <= len(file) - 1:
            group_texts[group_character] += file[iterator + group_character]
            iterator += group_size

    for group_text in group_texts:
        index_of_coincidence += return_ioc(group_text)

    return index_of_coincidence / group_size


if len(sys.argv) < 2 or len(sys.argv) > 5:
    print("Usage: ./index_of_coincidence.py [File Name] [Options]\n")
    print(sys.argv)
    exit()

elif "-s" in sys.argv:
    group_size = int(sys.argv[sys.argv.index("-s") + 1])
    ioc = return_slice_ioc()

    print("Index of Coincidence:", 26 * ioc)

elif "-l" in sys.argv:
    for group_size in range(1, int(sys.argv[sys.argv.index("-l") + 1]) + 1):
        ioc = return_slice_ioc()
        if 26*ioc > 1.6:
            print(f"\nKey length {group_size} is probably mono-alphabetic with Index of Coincidence: {26*ioc}")

else:
    ioc += return_ioc(file)
    print("Index of Coincidence for full text:", 26*ioc)
