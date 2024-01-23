import os, sys, random, string

# defines the logo and outputs it
logo = """
██████╗ ██╗  ██╗███████╗███████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗╚██╗██╔╝██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝ ╚███╔╝ ███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝  ██╔██╗ ╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██╔╝ ██╗███████║███████║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
            Password generator by TrippleMSoftware
"""

print(logo)

# defines the letters
letters = string.ascii_letters

# defines other chars
punc = string.punctuation

# defines numbers
numbs = string.digits

# adds them all together
chars = letters + punc + numbs

# gets user input for the length of the password
length = int(input("Enter password length: "))

# gets user input for the amount of passwords
amount = int(input("Enter amount of passwords to generate: "))

# generates and outputs the password to the console
def gen_pass(length, amount):
    print('\n')
    with open('generatedpasswords.txt', 'a') as file:
        for i in range(amount):
            password = ''.join(random.choice(chars) for i in range (length))
            print(password)
            file.write(password + "\n")

gen_pass(length, amount)
