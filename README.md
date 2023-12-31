# CryptographyCiphers

For all the programs in this repository:

 - There are two modes:

   - Encrypt Mode: Enter any text to see it get encrypted according to the key(s) selected by the user (It is case-sensitive, i.e. your encoded string will be in the exact format that you entered it with. Example: INPUT: hEllO, Encrypted String: zEbbW)
  
   - Decrypt Mode: Enter a key and encoded text to see it get decrypted according to the key(s) provided by user,decryption is successful as long as you have the correct keys (Case sensitive, same as above)


  -  Enter 'd' to switch to Decrypt Mode or 'e' to switch to Encrypt Mode when asked to change mode (Not case-sensitive)

  - You can enter "exit" at any time to exit the program 

# **Important Things to note for Shift Cipher:**

  (The program encrypts according to the Shift Cipher, also known as Caesar Cipher)

  - At the start of the program it will ask you if you want to use different keys for lowercase letters and uppercase letters, if you chose yes, this will apply to both encryption      and decryption (During encryption, the program will generate two random keys for lower and uppercase letters and use those, leading to a more secure encrypted result, in decryption, you will have to input two keys, one for lowercase and the other for uppercase letters)
    
  - You are able to input negative keys as well as keys greater than 26, the program will give you the according key mod to 26. But do not give the program a key of 0 or any multiple of 26, it will ask you to re-enter your key (Since that results in no encryption/decryption)

  # **Important Things to note for Affine Cipher:**

- Do not give the program an A coefficient/key of 0 or any multiple of 2 or multiples of 13, it will ask you to re-enter your key (Since that results in an imperfect encryption, i.e. multiple letters get encrypted to the same letter, same for decryption.This is a fundamental flaw in the affine cipher itself due to it being an ancient cipher)
  
- An example of an imperfect A coefficient/key is 4 (assume B key is 0), if you encrypt according to this key set, both A and N get encrypted to A, thus making decryption impossible to be 100% accurate (You can research more on this by yourself, this is just basic info I need to give you for the program)
 
- You are able to input negative keys as well as keys greater than 26, the program will give you the according key mod to 26.

# **Important Things to note for Vignere Cipher:**

- The key for Vignere Cipher, unlike the previous ciphers, is a string of alphabetical letters, Eg: "MIKE"
  
- The key is not case-sensitive, so "mIkE" is a valid key and will return the same ciphertext as the key "MIKE"
  
- You can make the key a sentence with spaces, and it will work just fine, Eg: "MIKE IS TALL" still works, and again it's not case-sensitive
