# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment No.2 - Problem 2

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

# Ask the user to input the encrypted message
encrypted_message = input("\n\033[3;35mPlease enter the message you want to decrypt: \033[0m")
decrypted_message = ""

# Change every symbol
for i in range(len(encrypted_message)):
    # If * is encrypted, decrypt to a
    if encrypted_message[i] == "*":
        decrypted_message += "a"
    
    # If & is encrypted, decrypt to e
    elif encrypted_message[i] == "&":
        decrypted_message += "e"
    
    # If # is encrypted, decrypt to i
    elif encrypted_message[i] == "#":
        decrypted_message += "i"
    
    # If + is encrypted, decrypt to o
    elif encrypted_message[i] == "+":
        decrypted_message += "o"
    
    # If ! is encrypted, decrypt to u
    elif encrypted_message[i] == "!":
        decrypted_message += "u"
    else:
        decrypted_message += encrypted_message[i]

print("")
print("-" * 70)
print("\033[1;3;32mProcessing..........\033[0m".center(80))
print("-" * 70)

print("\n\033[1;36mDecrypted message:\033[0m", decrypted_message)

# Outro and border line
print("\n") 
print("\033[3mThank you for supporting our program!".center(70))
print("")
print("\033[35m※ \033[0m" * 35)
print("")
