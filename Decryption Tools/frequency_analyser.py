import sys

with open(sys.argv[1], "r") as f:
    file = f.read()

file = file.upper()
file = file.replace(" ", "")
file = file.replace("\n", "")
file = file.replace("\t", "")


def count_alpha_frequencies(sample_text, grp_size):
    temp_frequency_list = []
    duplicate_checker = []

    for char_idx in range(len(sample_text) - grp_size + 1):
        cur_group = sample_text[char_idx: char_idx + grp_size]
        if cur_group not in duplicate_checker:
            temp_frequency_list.append((cur_group, sample_text.count(cur_group)))
            duplicate_checker.append(cur_group)

    return temp_frequency_list


if len(sys.argv) not in [3, 4, 5]:

    print("Usage: ./frequency_analyser.py [File Name] [Group Search Size]\n"
          "       ./frequency_analyser.py [File Name] [Options] [Search Size]\n")
    exit()

elif "-p" in sys.argv:

    key_length = int(sys.argv[sys.argv.index("-p") + 1])

    alt_char_search_num = int(sys.argv[sys.argv.index("-p") + 2]) - 1
    alt_char_text = ''

    iterator = 0
    while iterator + alt_char_search_num <= len(file) - 1:
        alt_char_text += file[iterator + alt_char_search_num]
        iterator += key_length
    cipher_alpha_frequencies = count_alpha_frequencies(alt_char_text, 1)

    print(f"\nFor every alternate {alt_char_search_num + 1} character{'s' * bool(alt_char_search_num)}, the frequency analysis yields: \n")

    for max_occurence in sorted(cipher_alpha_frequencies, key=lambda x: x[1]):
        print(f"{max_occurence[0]}:\t{max_occurence[1]}")

elif "-lp" in sys.argv:

    alt_char_search_num = int(sys.argv[sys.argv.index("-lp") + 1])  # Basically stores the key length
    alt_char_groups = [''] * alt_char_search_num

    for group_character in range(alt_char_search_num):
        iterator = 0
        while iterator + group_character <= len(file) - 1:
            alt_char_groups[group_character] += file[iterator + group_character]
            iterator += alt_char_search_num
        cipher_alpha_frequencies = count_alpha_frequencies(alt_char_groups[group_character], 1)

        print(f"\nFor every alternate {group_character + 1} character{'s' * bool(group_character)}, the frequency analysis yields: \n")

        for max_occurence in sorted(cipher_alpha_frequencies, key=lambda x: x[1]):
            print(f"{max_occurence[0]}:\t{max_occurence[1]}")

else:

    group_size = int(sys.argv[2])
    cipher_alpha_frequencies = count_alpha_frequencies(file, group_size)

    for max_occurence in sorted(cipher_alpha_frequencies, key=lambda x: x[1]):
        print(f"{max_occurence[0]}:\t{max_occurence[1]}")










# Frequent Letters ==> ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P',
#                       'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# Frequent Bigrams ==> ["TH", "HE", "IN", "ER", "AN", "RE", "ON", "AT", "EN", "ND", "TI", "ES", "OR", "TE", "OF", "ED",
#                       "IS", "IT", "AL", "AR", "ST", "TO", "NT", "NG", "SE", "HA", "AS", "OU", "IO", "LE", "VE", "CO",
#                       "ME", "DE", "HI", "RI", "RO", "IC", "NE", "EA", "RA", "CE"]

# Frequent Trigrams ==> ["THE", "AND", "THA", "ENT", "ING", "ION", "TIO", "FOR", "NDE", "HAS", "NCE", "EDT", "TIS",
#                        "OFT", "STH", "MEN"]


# Frequent Quadrigrams

# Of 1,144,085,293 tetra-grams scanned:
# 1. that (8709261, 0.761242%)
# 2. ther (6916008, 0.604501%)
# 3. with (6565513, 0.573866%)
# 4. tion (6314428, 0.551919%)
# 5. here (4285164, 0.374549%)
# 6. ould (4232202, 0.369920%)
# 7. ight (3540253, 0.309440%)
# 8. have (3324067, 0.290544%)
# 9. hich (3252540, 0.284292%)
# 10. whic (3247213, 0.283826%)
# 11. this (3161481, 0.276333%)
# 12. thin (3093756, 0.270413%)
# 13. they (3002324, 0.262421%)
# 14. atio (3001919, 0.262386%)
# 15. ever (2982572, 0.260695%)
# 16. from (2958372, 0.258580%)
# 17. ough (2899649, 0.253447%)
# 18. were (2643859, 0.231089%)
# 19. hing (2630750, 0.229944%)
# 20. ment (2555284, 0.223347%)
