from art import logo
import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    print(logo)  # Display the logo from the art module.
    while True:  # Start an infinite loop to keep the program running until the user decides to exit.
        # Get user input for the operation type (encode/decode).
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction != "encode" and direction != "decode":
            print('''Please enter "encode" or "decode"!''')
            continue  

        text = input("Type your message:\n").lower()  
        
        
        while True:
            user_input = input("Type the shift number:\n")
            if user_input.isdigit():
                shift = int(user_input)
                break  
            else:
                print("Please enter an integer number!")
    
        caesar(text, shift, direction)  # Call the Caesar cipher function with the user's inputs.

        # Ask the user if they want to restart the program.
        while True:
           restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
           if restart == "yes":
               break  
           elif restart == "no":
               print("Goodbye!")
               sys.exit()  # Exit the program if the user types 'no'.
           else:
               print("Invalid input. Please type 'yes' or 'no'.")
               continue  # Continue asking for valid input.

def caesar(text, shift, direction):
    encrypted_word = ""
    for letter in text:  # Iterate through each letter in the text.
        if letter in alphabet:  # Check if the letter is in the alphabet list.
            index = alphabet.index(letter)  # Find the index of the letter in the alphabet.
            # Calculate the new index for encoding or decoding.
            if direction == "encode":
                new_index = (index + shift) % len(alphabet)
            if direction == "decode":
                new_index = (index - shift) % len(alphabet)
            encrypted_word += alphabet[new_index]  # Add the new letter to the encrypted word.
        else:
            encrypted_word += letter  # If the character is not a letter, add it as it is.
    print(f"The encoded text is {encrypted_word}")  # Display the result.

if __name__ == "__main__":
    main()  # Run the main function when the script is executed.
            