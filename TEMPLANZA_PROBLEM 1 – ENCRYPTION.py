# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment No.2 - Problem 1

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome to our program! ♥ \033[0m".center(78))

# Ask the name of the user
name = input("\n\033[3mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

print("\033[36m Let's get started! \033[0m".center(78, "~"))

# Ask the user to input message to encrypt
plain_message = input("\nEnter a message to encrypt: ")
encrypted_message = ""

# Check every character
for i in range(len(plain_message)):
    # If a is in the text, encrypt to *
    if plain_message[i] == "a":
        encrypted_message += "*"
    
    # If e change & 
    elif plain_message[i] == "e":
        encrypted_message += "&"
    
    # If i change #
    elif plain_message[i] == "i":
        encrypted_message += "#"
    
    # If o change +
    elif plain_message[i] == "o":
        encrypted_message += "+"
    
    # If u change !
    elif plain_message[i] == "u":
        encrypted_message += "!"
    else:
        encrypted_message += plain_message[i]

print("")
print("-" * 70)
print("\033[1;3;32mProcessing..........\033[0m".center(80))
print("-" * 70)

# Print the output
print("\nYour encrypted message: " + encrypted_message)

# Outro and border line
print("\n")
print("\033[3mThank you for supporting our program!".center(70))
print("")
print("\033[35m※ \033[0m" * 35)
print("")