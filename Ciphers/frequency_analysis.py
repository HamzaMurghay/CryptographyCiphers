inp = """A: 55
B: 246
C: 227
D: 210
E: 64
F: 28
G: 227
H: 4
I: 19
J: 301
K: 67
L: 60
M: 86
N: 240
O: 12
P: 2
Q: 340
R: 4
S: 456
T: 75
U: 257
V: 130
W: 129
X: 71
Y: 84
Z: 132"""

total_letters = 0

freq_letters = ["E", "A", "R", "I", "O", "T", "N", "S", "L", "C", "U", "D", "P", "M", "H", "G", "B", "F", "Y", "W", "K",
                "V", "X", "Z", "J", "Q"]

cipher_alpha_frequencies = {}
duplicate_checker = []
cipher_to_plain = {}

for line in inp.splitlines():
    total_letters += int(line.split(": ")[1])
    cipher_alpha_frequencies[line.split(": ")[0]] = int(line.split(": ")[1])

counter = 0
for frequency in sorted(cipher_alpha_frequencies.values(), reverse=True):
    for key in cipher_alpha_frequencies:
        if cipher_alpha_frequencies[key] == frequency and key not in duplicate_checker:
            cipher_to_plain[key] = freq_letters[counter]
            duplicate_checker.append(key)
            break
    counter += 1

for char in "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS":
    if char.isspace():
        print(" ", end="")
    else:
        print(cipher_to_plain[char], end='')

print("\n\n")
# for key in cipher_to_plain:
#     print(f"{key} ==> {cipher_to_plain[key]}, {sorted(cipher_alpha_frequencies.values(), reverse=True)}")
