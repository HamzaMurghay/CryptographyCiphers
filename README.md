# CryptographyCiphers

For all of the programs in this repository:

  -  Enter 'd' to switch to Decrypt Mode or 'e' to switch to Encrypt Mode when asked to change mode (Not case sensitive)
  
  - You can enter "exit" at any time to exit the program 

# **Things to note for Shift Cipher Program:**

  (The program encrypts according to the Shift Cipher, also known as Ceasar Cipher)

   You are able to use two modes: 
  
  i) Encrypt Mode: Enter any text to see it get encrypted according to the key(s) selected by the user (It is case sensitive, i.e your encoded string will be in the exact                          format that you entered it with. Example: INPUT: hEllO, Encrypted String: bYffI)
  
  ii) Decrypt Mode: Enter a key and encoded text to see it get decrypted according to the key(s) you provided (Case sensitive, same as above)

  - You can thus decrypt a given encoded phrase, given that you know the key, if you dont know the key you can still try inputting all possible 25 keys to see which one gives a         sensible output (not recommended though, mainly only use this mode when you know the key)

Important points to note:

  - At the start of the program it will ask you if you want to use different keys for lowercase letters and uppercase letters, if you chose yes, this will apply to both encryption      and decryption (During encryption, the program will generate two random keys for lower and uppercase letters and use those, leading to a more secure encrypted result, in            decryption, you will have to input two keys, one for lowercase and the other for uppercase letters)
  - You are able to input negative keys as well as keys greater than 26, the program will give you the according key mod to 26. But do not give the program a key of 0 or any multiple of 26, it will ask you to re-enter your key (Since that results in no encryption)

  # **Things to note for Affine Cipher Program:**

  You still use the same two modes as previous program:

  i) Encrypt Mode: Enter any text to see it get encrypted according to the keys selected by the user (It is case sensitive, the encrypted/decrypted message will be in the same case format as input, Example: INPUT: hEllO, Encrypted String: zEbbW)
    
  ii) Decrypt Mode:  Enter the two keys and encoded text to see it get decrypted according to the keys you provided. (Case sensitive, same as above) 

  - However you must know the keys used during encyption, brute force is not an effective option in this cipher 
    
Important points to note:

- Do not give the program an A coefficient/key of 0 or any multiple of 2 or multiples of 13, it will ask you to re-enter your key (Since that results in an imperfect encryption, i.e multiple letters get encrypted to the same letter, same for decryption.This is a fundamental flaw in the affine cipher itself due to it being an ancient cipher)
- An example of an imperfect Akey is 4 (assume Bkey is 0), if you encrypt according to this key set, both A and N get encrypted to A, thus making decryption impossible to be 100% accurate (You can research more on this by yourself, this is justt basic info i need to give you for the program)

- You are able to input negative keys as well as keys greater than 26, the program will give you the according key mod to 26.
