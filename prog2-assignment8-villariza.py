# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import os, random

randNum = random.randint(0,100)
verRepeat = False
verConfig = True

#
os.system('cls')
progGreet = '{}'.format("\nWelcome to ? Villariza's Guessing Number Game ?\n")
progInfo = '{}'.format("\nPROGRAM INFORMATION AND INSTRUCTIONS.")
prog_varA = '{}'.format("\nA. This Python program will secretly conduct a Random Integer Number that will range only from (0-100).")
prog_varB = '{}'.format("\nB. From there, you'll only need to guess which number Python has pulled between the specified range given above the information.")
prog_varC = '{}'.format("\nC. The program will loop over and over until your input integer and Python's pulled number match consequently.")
prog_varD = '{}'.format("\nD. If your input integer is greater than the Python's pulled number, the program will state its response (Greater Than) and continue its loop; vice versa.")
prog_varE = '{}'.format("\nE. If your input integer is less than the Python's pulled number, the program will state its response (Less Than) and continue its loop; vice versa.")
prog_varF = '{}'.format("\nF. After you've gussed the right number (as answer), it will ask you to repeat the game or mainly exit the program.")

print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD, prog_varE, prog_varF)

#
usr_InputError = "{}".format("Input Invalid. Please enter only a numerical integer input ranging from (0-100). \n>>> ")
verRPT_Error = "{}".format("\nInput Invalid. Type and Enter your Answer only in Yes or No. \n>>> ")
NEG_valError = "{}".format(f"Input Invalid. Your numerical integer input is less than 0 as shown:")
EXC_valError = "{}".format(f"Input Invalid. Your numerical integer input is greater than 100 as shown:")

#
prog_usrInput = "{}".format("\nType and Enter your GUESS in NUMERICAL INPUT in the space provided below. \n>>> ")
verRPT_Input = "{}".format("\nWould you like to try again? Type and Enter only Yes or No. \n>>> ")
ext_Input = "{}".format("\nThank you for playing ? Villariza's Guessing Number Game ? \nWe'll see you again next time! \n\nPython Info: The program has been closed.\n")
GTR_Tip = "{}".format("TIP \nTry incrementing the integer of your numerical input. \n>>> ")
LESS_Tip = "{}".format("TIP \nTry decreasing the integer of your numerical input. \n>>> ")
user_Input = input(f"{prog_usrInput}")
os.system('cls')

while not(verRepeat):
    if (user_Input.isalpha() == True) or (user_Input.isprintable() == False) or (user_Input.isspace() == True):
        user_Input = input(f"{usr_InputError}")
        os.system('cls')
        continue;
    elif user_Input.replace("-","",1).isdigit():
        fnl_Input = int(user_Input)
        if fnl_Input == randNum:
            os.system('cls')
            print(f"\nYou are right!\n \nYour Input: {fnl_Input} \nRandom Number: {randNum}\n")
            config_Inpt = input(f"{verRPT_Input}")
            os.system('cls')
            while verConfig:
                if (config_Inpt.replace(".","",10).upper() or config_Inpt.replace("!","",10).upper()) == "YES":
                    user_Input = input(f"{prog_usrInput}")
                    os.system('cls')
                    verRepeat = False
                    break;
                elif (config_Inpt.replace(".","",10).upper() or config_Inpt.replace("!","",10).upper()) == "NO":
                    verRepeat = True
                    break;
                else:
                    config_Inpt = input(f"{verRPT_Error}")
                    os.system('cls')
                    continue;
        elif fnl_Input < 0 or fnl_Input > 100:
            if fnl_Input < 0:
                user_Input = input(f"{NEG_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                os.system('cls')
                continue;
            elif fnl_Input > 100:
                user_Input = input(f"{EXC_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                os.system('cls')
                continue;
        elif fnl_Input < randNum:
            print(f"\nLess than the Random Number. \nYour Input: {fnl_Input}\n")
            user_Input = input(f"{GTR_Tip}")
            os.system('cls')
            continue;
        elif fnl_Input > randNum:
            print(f"\nGreater than the Random Number.\nYour Input: {fnl_Input}\n")
            user_Input = input(f"{LESS_Tip}")
            os.system('cls')
            continue;
    else:
        user_Input = input(f"{usr_InputError}")
        os.system('cls')
        continue;

print(f"{ext_Input}")