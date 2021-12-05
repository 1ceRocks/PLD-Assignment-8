# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

"""
Purpose of specified modules into the program
OS       : System('cls') for a character terminal cleanup on input and output of the program.
Random   : Random Integer will display by the program that will be the game's core value after its run or loop.
Sys      : Sys.exit() to end the program loop when the user wants to exit the game.
Time     : Timer Countdown when the user has inputted numerical correspondence on the program requirement used to match the Program Guessed Number.
Winsound : Audio Peripherals have been inserted for a compelling context outflow of the program. (Works only for Windows Desktop Users)
"""
import os, random, sys, time, winsound

randNum = random.randint(0,100)
verRepeat = False # Acronym: Verify Repeat       | The main while loop of the program; when True, the program shall bound to stop and exit the terminal.
verConfig = True # Acronym: Verify Configuration | The second while loop of the program; when False, the program shall terminate the Verify Repeat User Input inside the program.
countdownSec = 1 # Acronym: Countdown Seconds    | The main int variable for Time Module.
os.system('cls') # The terminal output beforehand will be cleared.

"""
Variable Formats to be used for the program interface and settings.
"""
# Acronym: Program Greet       | The Entire Program Name Welcoming the User.
progGreet = '{}'.format("\nWelcome to ? Villariza's Guessing Number Game ?\n")

# Acronym: Exit Input          | A Formal Valedictory of the Program to the user.
progExt = '{}'.format("\n\nThank you for playing ? Villariza's Guessing Number Game ? \nWe'll see you again next time! \n\nPython Info: The program has been closed.\n\n")

# Acronym: Program Information | General Indicator on the Program Settings.
progInfo = '{}'.format("\nPROGRAM INFORMATION AND INSTRUCTIONS.")

# Acronym: Program Variable A  | Progam Setting A.
prog_varA = '{}'.format("\nA. This Python program will secretly conduct a Random Integer Number that will range only from (0-100).")

# Acronym: Program Variable B  | Progam Setting B.
prog_varB = '{}'.format("\nB. From there, you'll only need to guess which number Python has pulled between the specified range given above the information.")

# Acronym: Program Variable C  | Progam Setting C.
prog_varC = '{}'.format("\nC. The program will loop over and over until your input integer and Python's pulled number match consequently.")

# Acronym: Program Variable D  | Progam Setting D.
prog_varD = '{}'.format("\nD. If your input integer is greater than the Python's pulled number, the program will state its response (Greater Than) and continue its loop; vice versa.")

# Acronym: Program Variable E  | Progam Setting E.
prog_varE = '{}'.format("\nE. If your input integer is less than the Python's pulled number, the program will state its response (Less Than) and continue its loop; vice versa.")

# Acronym: Program Variable F  | Progam Setting F.
prog_varF = '{}'.format("\nF. After you've gussed the right number (as answer), it will ask you to repeat the game or mainly exit the program.")

# Aggregated variable formats to be printed as def-named function. << (Also used for the user input to repeat the program or game).
def prog_Intf():
    print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD, prog_varE, prog_varF)
prog_Intf()

"""
Variable Invalid or Error Formats to be used on the main program below.
"""
# Acronym: User Input Error      | User did not input any numerical integer or is in character invalidity.
usr_InputError = "{}".format("Input Invalid. Please enter only a numerical integer input ranging from (0-100). \n>>> ")

# Acronym: Verify Repeat Error   | User not inputting "Yes" or "No" on the program repeat or is in character invalidity.
verRPT_Error = "{}".format("\nInput Invalid. Type and Enter your Answer only in Yes or No. \n>>> ")

# Acronym: Negative Value Error  | User Numerical Input - Less than 0 (Negative Integers).
NEG_valError = "{}".format(f"Input Invalid. Your numerical integer input is less than 0 as shown:")

# Acronym: Excel Value Error     | User Numerical Input - Greater than or Equal to 10 (Regarded Range: 0-9).
EXC_valError = "{}".format(f"Input Invalid. Your numerical integer input is greater than 100 as shown:")

"""
The General Format Variables for User Numerical Input
"""
# Acronym: Program user Input    | User Numerical Input.
prog_usrInput = "{}".format("\nType and Enter your GUESS in NUMERICAL INPUT in the space provided below. \n>>> ")

# Acronym: Verify Input          | User Character Input.
verRPT_Input = "{}".format("\nWould you like to try again? Type and Enter only Yes or No. \n>>> ")

# Acronym: Greater Than Tip      | User Greater Numerical Input.
GTR_Tip = "{}".format("TIP \nTry incrementing the integer of your numerical input. \n>>> ")

# Acronym: Less Than Tip         | User Lesser Numerical Input.
LESS_Tip = "{}".format("TIP \nTry decreasing the integer of your numerical input. \n>>> ")

"""
THE ENTIRE METHOD OF VILLARIZA'S GUESSING NUMBER GAME PROGRAM

Table of Contents: Acronym for the Variables Used

alpha        = Alpha
config_Inpt  = Configuration Input
data         = Data (1st, 2nd, 3rd)
delta        = Delta
EOFError     = End Of File Error
fnl_Input    = Final Input
progError    = Program Error
randNum      = Random Number
user_Input   = User Input
ValueError   = Value Error 
verRepeat    = Verify Repeat
"""
user_Input = input(f"{prog_usrInput}")
os.system('cls') # The terminal output beforehand will be cleared.

while not(verRepeat): # While = Statement False. // while False + verRepeat False ;= True to break.
    try:
        if (user_Input.isalpha() == True) or (user_Input.isprintable() == False) or (user_Input.isspace() == True):
            for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                if alpha == 0:
                    print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                time.sleep(1)
            os.system('cls') # The terminal output beforehand will be cleared.
            user_Input = input(f"{usr_InputError}")
            os.system('cls') # The terminal output beforehand will be cleared.
            continue;
        elif user_Input.replace("-","",10).isdigit():
            fnl_Input = int(user_Input)
            if fnl_Input == randNum:
                for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                    if alpha == 0:
                        print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                time.sleep(1)
                os.system('cls') # The terminal output beforehand will be cleared.
                print(f"\nYou are right!\n \nYour Input: {fnl_Input} \nRandom Number: {randNum}\n")
                winsound.PlaySound("Hello", winsound.SND_FILENAME)
                config_Inpt = input(f"{verRPT_Input}")
                os.system('cls') # The terminal output beforehand will be cleared.
                while verConfig: # While = Statement False. // while False + verConfig True ;= False to break.
                    if (config_Inpt.replace(".","",10).upper() or config_Inpt.replace("!","",10).upper()) == "YES":
                        for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                            if alpha == 0:
                                print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                        time.sleep(1)
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        user_Input = input(f"{prog_usrInput}")
                        os.system('cls') # The terminal output beforehand will be cleared.
                        verRepeat = False
                        break;
                    elif (config_Inpt.replace(".","",10).upper() or config_Inpt.replace("!","",10).upper()) == "NO":
                        verRepeat = True
                        break;
                    else:
                        for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                            if alpha == 0:
                                print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                        time.sleep(1)
                        os.system('cls') # The terminal output beforehand will be cleared.
                        config_Inpt = input(f"{verRPT_Error}")
                        os.system('cls') # The terminal output beforehand will be cleared.
                        continue;
            elif fnl_Input < 0 or fnl_Input > 100:
                if fnl_Input < 0:
                    for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                        if alpha == 0:
                            print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                    time.sleep(1)
                    os.system('cls') # The terminal output beforehand will be cleared.
                    user_Input = input(f"{NEG_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    continue;
                elif fnl_Input > 100:
                    for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                        if alpha == 0:
                            print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                    time.sleep(1)
                    os.system('cls') # The terminal output beforehand will be cleared.
                    user_Input = input(f"{EXC_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    continue;
            elif fnl_Input < randNum:
                os.system('cls') # The terminal output beforehand will be cleared.
                print(f"\nLess than the Random Number. \nYour Input: {fnl_Input}\n")
                user_Input = input(f"{GTR_Tip}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
            elif fnl_Input > randNum:
                print(f"\nGreater than the Random Number.\nYour Input: {fnl_Input}\n")
                user_Input = input(f"{LESS_Tip}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
            else:
                for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                    if alpha == 0:
                        print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                time.sleep(1)
                os.system('cls') # The terminal output beforehand will be cleared.
                user_Input = input(f"{usr_InputError}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
        else:
            for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                if alpha == 0:
                    print("Evaluating in " + str(countdownSec - alpha) + " ...") # 0 second elapsed
            time.sleep(1)
            os.system('cls') # The terminal output beforehand will be cleared.
            user_Input = input(f"{usr_InputError}")
            os.system('cls') # The terminal output beforehand will be cleared.
            continue;

    except ValueError or EOFError as delta:
        progError = '{0}'.format(delta)
        os.system('cls') # The terminal output beforehand will be cleared.
        print(f"Invalid input. | \n{progError}")

    finally:
        None

os.system('cls') # The terminal output beforehand will be cleared.
print(f"{progExt}")
sys.exit()