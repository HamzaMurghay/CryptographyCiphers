import sys


def convert_to_data_format(sample_text, grp_size):
    temp_frequency_list = []
    duplicate_checker = []

    sample_text = sample_text.replace(" ", "")
    sample_text = sample_text.replace("\n", "")

    for char_idx in range(len(sample_text) - grp_size + 1):
        cur_group = sample_text[char_idx: char_idx + grp_size]
        if cur_group not in duplicate_checker: temp_frequency_list.append((cur_group, sample_text.count(cur_group)))
        duplicate_checker.append(cur_group)

    return temp_frequency_list


if len(sys.argv) != 3:
    print("Usage: ./frequency_analyser.py [File Name] [Group Search Size]\n")
    exit()

file = open(sys.argv[1], "r").read()
group_size = int(sys.argv[2])

cipher_alpha_frequencies = convert_to_data_format(file, group_size)

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

# Of 1,144,085,293 quadrigrams scanned:
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
