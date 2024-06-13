# CSC 122
# Substitution Cipher
# By <Your Name>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""

def main():
    cipher = [] #empty list
    message = input("Enter the message to be encrypted: ")
    for letter in message:   #letter will take on each value in the string inputed by the user
        cipher.append(chr(ord(letter) + 3))   #order of operations will do the ord first to convert letter to ord, then add 3 to it, then convert back to ACS character, then add to list in ciper by appending it
    print(F"Encrypted message = {''.join(cipher)}\n")   #use join method of cipher list to combine all values into 1 string. Its why we used the empty string ''.

    plaintext = []
    message = input("Enter the cipher to be decrypted: ")
    for letter in message:
        plaintext.append(chr(ord(letter) - 3)) #now we do inverse by subtracting 3
    print(F"Decrypted message = {''.join(plaintext)}\n")

if __name__ == '__main__':
    main()
