'''
Caleb Ha
23/03/2023
LUNA Cipher

This is the LUNA Cipher. LUNA is an acryonym for Layered Unbreakable Numerical Algorithm. This cipher will be based upon a previous cipher I created named the TESS Cipher.
The TESS Cipher (Transformational Enhanced Shift System) used a modified version of the Ceaser Cipher which increases
the shift used as it encrypts the message. The LUNA Cipher is based on the same principle, however, at the very end of the
encryption, the whole message is put through the Polybius Cipher.

No value greater than 1 billion may be entered for the shift value due to limitations in the code
'''

# Just to use sys.exit(1)
import sys

# Encryptes using TESS1
def encryptionTess(phrase, shift, verbose=False):
    
    # Contains the encrypted phrase
    encryptedPhrase = ""

    # Contains the total shift
    numberShift = 0
    
    # Loops through all the characters in the phrase
    for character in phrase:
        
        # Keeps track of the character
        i = 0
        
        # Finds the character in the character set
        while character != characterSet[i]:
            
            i += 1
        
        # Increases the number shift
        numberShift += shift
        
        # Increments the character
        i += numberShift
        
        # Checks to see if the i variable is outside of the range of the characte set
        while i > len(characterSet) - 1:
            
            i -= len(characterSet)
        
        # Adds the encrypted character the the encrypted phrase
        encryptedPhrase += characterSet[i]

        # Debugging info
        if verbose:
            print(f"Character: {character}, Shift: {numberShift}, Encrypted: {characterSet[i]}")

    # Returns the final encrypted phrase
    return encryptedPhrase

# Decrypts using TESS
def decryptionTess(phrase, shift, verbose=False):
    
    # Contains the decrypted phrase
    decryptedPhrase = ""

    # Contains the total number shift
    numberShift = 0
    
    # Loops through all the characters in the phrase
    for character in phrase:
        
        # Keeps tract in the character
        i = 0
        
        # Finds the character in the character set
        while character != characterSet[i]:
            
            i += 1

        # Increases the number shift
        numberShift += shift

        # Decrements the character
        i -= numberShift
        
        # Checks to see if the variable i is outside of the range of the character set
        while i < 0:
            
            i += len(characterSet)
        
        # Adds the decrypted character to the decrypted phrase
        decryptedPhrase += characterSet[i]

        # Debugging info
        if verbose:
            print(f"Encrypted Character: {character}, Shift: {numberShift}, Decrypted Character: {characterSet[i]}")
    
    # Returns the final decrypted phrase
    return decryptedPhrase

# Encrypts using Polybius Cipher
def encryptionPolybius(phrase, verbose=False):

    # Contains the encrypted phrase
    encryptedPhrase = ""

    # Loops through all the characters in the phrase
    for character in phrase:

        # Loops through all the rows in the polybius square
        for row in range(len(polybiusSquare)):

            # Loops through all the columns in the polybius square
            for column in range(len(polybiusSquare[0])):

                # Checks to see if the character is the same as the item in the list
                if character == polybiusSquare[row][column]:

                    # Debugging info
                    if verbose:
                        print(f"Character: {character}, Row: {row}, Column: {column}, Encrypted: {rowEncryptionCharacters[row] + columnEncryptionCharacters[column]}")

                    # Adds the encrypted characters to the encrypted phrase
                    encryptedPhrase += rowEncryptionCharacters[row]
                    encryptedPhrase += columnEncryptionCharacters[column]
    
    # Returns the encrypted phrase
    return encryptedPhrase

# Decrypts using Polybius Cipher
def decryptionPolybius(phrase, verbose=False):

    # Contains the decrypted phrase
    decryptedPhrase = ""

    # Loops to iterate through all the characters (+1 to ensure that the try-except block is ran)
    for i in range(len(phrase)):

        j = i * 2

        # Checks to see if the phrase[j] is out of the index
        try:

            phrase[j]
    
        # Runs at the end of the characters
        except IndexError:

            # Returns the decypted phrase
            return decryptedPhrase
        
        # Creates the encypted block
        encryptedBlock = phrase[j] + phrase[j + 1]

        # Loops through the all the characters in polybius square row string
        for row in range(len(polybiusSquare)):

            # Finds the row of the character
            if rowEncryptionCharacters[row] == encryptedBlock[0]:

                # Loops through all the characters in the polybius square column string
                for column in range(len(polybiusSquare[0])):

                    # Finds the column of the character
                    if columnEncryptionCharacters[column] == encryptedBlock[1]:

                        # Adds the decrypted character to the decrypted phrase
                        decryptedPhrase += polybiusSquare[row][column]

                        # Debugging info
                        if verbose:

                            print(f"Encrypted Block: {encryptedBlock}, Row: {row}, Column: {column}, Decrypted: {polybiusSquare[row][column]}")

# Uses both methods of encryption, as well as tacking on the shift value as well as how long the shift is
def totalEncryption(phrase, shift, verbose=False):

    # Checks if the shift value is greater or equal to 1 billion. If it is, it stops the program
    if shift > 999999999:

        print("Error: Please do not attempt to encrypt with a shift equal or greater than 1 billion")
        sys.exit(1)

    # Encrypts the phrase using TESS
    encryptedPhraseTess = encryptionTess(phrase, shift, verbose)

    # Encrypts the phrase using the Polybius Square and adds the shift value as well as how long the shift is
    encryptedPhrasePolybius = encryptionPolybius(encryptedPhraseTess, verbose) + str(shift) + str(len(str(shift)))

    # Returns the totally encrypted phrase
    return encryptedPhrasePolybius

# Uses both methods of decryption
def totalDecryption(phrase, verbose=False):

    # Gets how long the shift value is
    charLength = int(phrase[-1])

    # Keeps track of the shift value
    shiftValue = ""

    # Finds the shift value from the end of the phrase
    for i in range(charLength - 1, -1, -1):

        shiftValue += phrase[-(i +2)]

    # Translates the shift value from a string to an integer
    shiftValue = int(shiftValue)

    # Checks if the shift value is greater or equal to 1 billion. If it is, it stops the program
    if shiftValue > 999999999:

        print("\n---------- ERROR ----------")
        print("Do not enter a number greater than 999,999,999 as the shift value")
        print("---------- ERROR ----------")

        sys.exit(1)

    # Removes the tacked on shift value as well as how long the shift is from the phrase
    phrase = phrase.replace(str(shiftValue) + str(charLength), "")

    # Decrypts using the Polybius Square
    polybiusDecryption = decryptionPolybius(phrase, verbose)

    # Decrypts using TESS
    tessDecryption = decryptionTess(polybiusDecryption, shiftValue, verbose)

    # Returns the decrypted phrase
    return tessDecryption

# A list of 95 characters, organized in the order on a keyboard
characterSet = [
    '`', '~', '1', '!', '2', '@', '3', '#', '4', '$', '5', '%', '6', '^', '7', '&', '8', '*', '9', '(', '0', ')', '-', '_', '=', '+',
    'q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', '[', '{', ']', '}', 
    'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', ';', ':', '\'', '\"', '\\', '|', 
    'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', ',', '<', '.', '>', '/', '?',
    ' '
]

# A 5x19 Polybius Square (Rectangle)
polybiusSquare = [
    # 0    1    2    3    4
    ['`', '~', '1', '!', '2'], # 0
    ['@', '3', '#', '4', '$'], # 1
    ['5', '%', '6', '^', '7'], # 2
    ['&', '8', '*', '9', '('], # 3
    ['0', ')', '-', '_', '='], # 4
    ['+', 'q', 'Q', 'w', 'W'], # 5
    ['e', 'E', 'r', 'R', 't'], # 6
    ['T', 'y', 'Y', 'u', 'U'], # 7
    ['i', 'I', 'o', 'O', 'p'], # 8
    ['P', '[', '{', ']', '}'], # 9
    ['a', 'A', 's', 'S', 'd'], # A 10
    ['D', 'f', 'F', 'g', 'G'], # B 11
    ['h', 'H', 'j', 'J', 'k'], # C 12
    ['K', 'l', 'L', ';', ':'], # D 13
    ['\'', '\"', '\\', '|', 'z'], # E 14
    ['Z', 'x', 'X', 'c', 'C'], # F 15
    ['v', 'V', 'b', 'B', 'n'], # G 16
    ['N', 'm', 'M', ',', '<'], # H 17
    ['.', '>', '/', '?', ' '] # I 18
]

# Holders of the characters used to encode in the polybius square
rowEncryptionCharacters = "0123456789ABCDEFGHI"
columnEncryptionCharacters = "01234"

# Takes user input to encrypt or decrypt
encryptOrDecrypt = input("Do you want to encrypt or decrypt? (e/d): ")

# Option to encrypt
if encryptOrDecrypt == "e":

    # Takes the user message to encrypt
    message = input("\nPlease input message: ")

    # Takes user input for the shift value
    shift = int(input("\nPlease input shift: "))

    # Checks if the shift value is invalid
    if shift > 999999999:

        print("\n---------- ERROR ----------")
        print("Do not enter a number greater than 999,999,999 as the shift value")
        print("---------- ERROR ----------")

        sys.exit(1)

    # Determines if to print verbose output
    verboseInput = input("\nVerbose? (y/n): ")

    if verboseInput == "y":

        verbose = True
        
    elif verboseInput == "n":

        verbose = False

    else:

        print("Invalid input. Verbose is set to false.")
        verbose = False

    encryptedMessage = totalEncryption(message, shift, verbose)

    print(f"\nEncrypted Message: {encryptedMessage}")

# Option to decrypt
elif encryptOrDecrypt == "d":

    message = input("\nPlease input message: ")

    # Determines if to print verbose output
    verboseInput = input("\nVerbose? (y/n): ")

    if verboseInput == "y":

        verbose = True
        
    elif verboseInput == "n":

        verbose = False

    else:

        print("Invalid input. Verbose is set to false.")
        verbose = False

    decryptedMessage = totalDecryption(message, verbose)

    print(f"\nDecrypted Message: {decryptedMessage}")

else:

    print("\nInvalid input.")
