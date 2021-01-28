# References:
# https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php
# https://blog.finxter.com/a-simple-python-morse-code-translator/
# https://en.wikipedia.org/wiki/Morse_code#

import re

# Dictionary to store characters with their corresponding Morse Codes
morse_code_table = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '0':'-----','1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', ',':'--..--',
                    '.':'.-.-.-', '?': '..--..',';':'-.-.-.',':':'---...',
                    '/':'-..-.', '-' : '-....-', '(': '-.--.', ')' : '-.--.-',
                    '=':'-...-', '+':'.-.-.', '@': '.--.-.', ' ': '.......'
                    }

# Function to convert a sentence into Morse Code. Returns the encoded message.
def convert_to_morse_code(sentence):
    encoded_txt = '';
    char = ''

    for letter in sentence.upper().strip():
        char = morse_code_table[letter]
        encoded_txt += char + ' ';

    return encoded_txt

# Function to convert an encoded message into plain text. Returns the decoded sentence.
def convert_to_text(encoded_msg):
    char = ''
    cipher = encoded_msg.split(' ');
    decoded_msg = ''

    # Swap key/values in morse_code_table
    decrypt_dict = dict([(v, k) for k, v in morse_code_table.items()])
    
    for value in cipher:
        if value == '':    # End of message
            break
        
        char = decrypt_dict[value]
        decoded_msg += char 
    
    return decoded_msg

# Function to check whether each character in the plain text is encodable i.e. exists in the morse_code_table dictionary
def is_encodable(plain_text):
    for letter in plain_text.upper():
        if (not(letter in morse_code_table.keys())):
            print("Unable to encode message! No entry for '{}' found! Try again.".format(letter))
            return False
    
    return True

# Function to check whether each character in the morse_text is decodable i.e. exists in the decrypt_dict
def is_decodable(morse_text):
    cipher = morse_text.upper().strip().split(' ');

    # Swap key/values in morse_code_table
    decrypt_dict = dict([(v, k) for k, v in morse_code_table.items()])

    for value in cipher:
        if (not(value in decrypt_dict.keys())):
            print("Unable to decode message! No entry for '{}' found! Try again.".format(value))
            return False

    return True


def input_message():
    flag = 1
    
    while (flag):
        message = input("\nEnter the message to decode/encode : ")
        result = re.match(r'^[ ]*$',message)    

        if (result):    # Empty message/contains only spaces
            print("Invalid input! Message must not be empty!")

        else:
            # RegEx pattern for Morse code
            pattern = r'^[. / -]+$'

            result = re.match(pattern,message)

            if (result):    # Message is in morse code and needs to be decoded
                if (is_decodable(message)):    # Check if all characters are decodable
                    flag = 0
            
            else:
                if (is_encodable(message)):    # Check if all characters are encodable 
                    flag = 0

    return message

def input_choice():
    flag = 1
    while (flag):
        choice = input("\nDo you want to continue? (Y/N) : ").upper()
        if (choice == 'Y' or choice == 'N'):
            flag = 0
        else:
            print("Invalid choice! Try again.")

    return choice


if __name__ == "__main__":
    flag = 1
    choice = ''

    # RegEx pattern for Morse code
    pattern = r'^[. / -]+$'

    while (flag):    # Continue until user decides to exit

        message = input_message()    # Call function to input a valid message
        result = re.match(pattern,message)

        if (result):
            sentence = convert_to_text(message)
            print("The decoded message is '{}'".format(sentence))

        else:
            encoded_msg = convert_to_morse_code(message)
            print("The encoded message is '{}'".format(encoded_msg.strip()))

        choice = input_choice()    # Call function to input a valid choice

        if (choice == 'N'):
            print("\nExiting program...")
            flag = 0

