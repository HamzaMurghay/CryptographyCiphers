# This program enables the Kasiski test/method to find put the most probable key length of a key-based poly-alphabetic
# cipher, most likely vignere cipher

# It assumes that the repeated patters occur due to repeated plaintext and key match ups, although it is possible for
# the repeated pattern to emerge as pure chance of a different plaintext and key match up, the probability of this gets
# significantly reduced with repeated pattern occurences, so its change is very, very low


import sys

with open(sys.argv[1], "r") as f:
    file = f.read()

file = file.upper()
file = file.replace(" ", "")
file = file.replace("\n", "")
file = file.replace("\t", "")


def find_common_divisors(list_of_num):
    common_divisors = []
    for factor in range(1, min(list_of_num) + 1):
        if all(num % factor == 0 for num in list_of_num):
            common_divisors.append(factor)
    return common_divisors


for pattern_len in range(3, 7+1):
    rep_pattern_distances = []

    for char_idx in range(len(file)):
        if char_idx + pattern_len <= len(file):
            pattern = file[char_idx: char_idx + pattern_len]
            if file.count(pattern) >= 3:
                for pattern_checks in range(char_idx + 1, len(file)):
                    pattern_check = file[pattern_checks: pattern_checks + pattern_len]
                    if pattern_check == pattern:
                        rep_pattern_distances.append(pattern_checks - char_idx)
                        # break  - Add this line if you want a less extensive search

    if rep_pattern_distances:
        all_possible_key_lengths = find_common_divisors(rep_pattern_distances)
    print(f"Possible Key lengths after analysing {pattern_len} letter long pattern distances: {all_possible_key_lengths}")
