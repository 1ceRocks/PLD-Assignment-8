# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

"""
Purpose of specified modules into the program
OS       : System('cls') for a character terminal cleanup on input and output of the program.
Random   : Random Integer will display by the program that will be the game's core value after its run or loop.
Sys      : Sys.exit() to end the program loop when the user wants to exit the game.
Time     : Timer Countdown when the user has inputted numerical correspondence on the program requirements used to match the Lotto Winning Numbers.
Winsound : Audio Peripherals have been inserted for a compelling context outflow of the program. (Works only for Windows Desktop Users)
"""
import os, random, sys, time, winsound
verRepeat = False # Acronym: Verify Repeat | The main while loop of the program; when True, the program shall bound to stop and exit the terminal.
os.system('cls') # The terminal output beforehand will be cleared.

"""
Variable Formats to be used for the program interface and settings.
"""
# Acronym: Program Greet       | The Entire Program Name Welcoming the User.
progGreet = "{}".format(f"\n$! Welcome to Villariza Lottery !$\n")

# Acronym: Exit Input          | A Formal Valedictory of the Program to the user.
progExt = '{}'.format("\nThank you for playing $! Villariza Lottery $! \nWe'll see you again next time! \n\nPython Info: The program has been closed.\n")

# Acronym: Program Information | General Indicator on the Program Settings.
progInfo = "{}".format(f"\nPROGRAM INFORMATION AND INSTRUCTIONS")

# Acronym: Program Variable A  | Progam Setting A.
prog_varA = "{}".format(f"\nA. You just simply have to input THREE (3) random numbers ranging from 0-9 on the terminal.")

# Acronym: Program Variable B  | Progam Setting B.
prog_varB = '{varA} e.g. {varB}'.format(varA = f"\nB. The Program will input THREE (3) Random Winning Numbers regarded on the Lottery Menu.", varB = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)])

# Acronym: Program Variable C  | Progam Setting C.
prog_varC = "{}".format(f"\nC. If the Random Winning Numbers matches with your Numerical Input, then the program output will respond saying \"You Win!\"")

# Acronym: Program Variable D  | Progam Setting D.
prog_varD = "{}".format(f"\nD. If the Random Winning Numbers does not match with your Numerical Input, then the program output will respond saying \"You've Lost.\"")

# Aggregated variable formats to be printed as def-named function. << (Also used for the user input to repeat the program or game).
def prog_Intf():
    print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD)
prog_Intf()

"""
Variable Invalid or Error Formats to be used on the main program below.
"""
# Acronym: Number Data Invalid         | Inputs should range only on 0-9.
num_dataInval = '{}'.format("\nNumerical inputs should range only on 0-9. \n>>> ")

# Acronym: Alpha-Numerical Print Error | Inputs should range only on 0-9.
alnum_printError = '{}'.format("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")

# Acronym: Number Duplicate Error      | Duplicated Numerical Input.
num_duplcError = '{}'.format("\nYour numerical input should not be the same as your previous input stored on the tuple list. \nPlease try again by typing and entering a different numerical input that should only range from 0-9. \n>>> ")

# Acronym: Repeating Print Error       | User not inputting "Y" or "N" on the program repeat.
RPT_printError = '{}'.format("\nInvalid Input. Please try again by answering \"Y\" / \"N\" (Yes / No) \nY , N >>> ")

# Acronym: Negative Value Error        | User Numerical Input - Less than 0 (Negative Integers).
NEG_valError = '{}'.format("\nYour Numerical Input is Invalid. It should not be negative or less than 0. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")

# Acronym: Excel Value Error           | User Numerical Input - Greater than or Equal to 10 (Regarded Range: 0-9).
EXC_valError = '{}'.format("\nYour Numerical Input is Invalid. It should not be greater or equal to 10. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")

"""
The General Format Variables for User Numerical Input
"""
# Acronym: First (1st) Data Input      | User Numerical Input.
data1_Inpt = '{}'.format("\nEnter your FIRST (1st) number on the space provided below.")

# Acronym: Second (2nd) Data Input     | User Numerical Input.
data2_Inpt = '{}'.format("\nEnter your SECOND (2nd) number on the space provided below.")

# Acronym: Third (3rd) Data Input      | User Numerical Input.
data3_Inpt = '{}'.format("\nEnter your THIRD (3rd) number on the space provided below.")

# Acronym: Configuration Repeat Input  | User Character Input (Y / N).
configRPT_Inpt = '{}'.format("\nDo you want to try again? Answer only in characters \"Y\" / \"N\" (Yes / No). \nY , N >>> ")

"""
THE ENTIRE METHOD OF THE VILLARIZA LOTTERY PROGRAM

Table of Contents: Acronym for the Variables Used

alpha        = Alpha
beta         = Beta
configRPT    = Configuration Repeat
countdownSec = Countdown in Seconds
data         = Data (1st, 2nd, 3rd)
delta        = Delta
EOFError     = End Of File Error
fnl_data     = Final Data
fnl_winNum   = Final Winning Numbers
inval        = Invalid (1st, 2nd, 3rd)
inval_DGT    = Invalid Digit
inval_IPT    = Invalid Input
progError    = Program Error
rand_Duplc   = Random Duplicate
ValueError   = Value Error 
verRepeat    = Verify Repeat
win_randNum  = Winning Random Number (1st, 2nd, 3rd)
"""
while not(verRepeat): # While = Statement False. // while False + verRepeat False ;= True to break.
    try:
        win_randNum1 = random.randint(0,9)
        win_randNum2 = random.randint(0,9)
        win_randNum3 = random.randint(0,9)
        countdownSec = 3

        rand_Duplc = False
        while not(rand_Duplc):
            if win_randNum1 == win_randNum2:
                win_randNum2 = random.randint(0,9)
                continue;
            elif win_randNum1 == win_randNum3:
                win_randNum3 = random.randint(0,9)
                continue;
            elif win_randNum2 == win_randNum3:
                win_randNum3 = random.randint(0,9)
                continue;
            else:
                rand_Duplc = True
                break;

        fnl_winNum = [win_randNum1, win_randNum2, win_randNum3]

        inval_DGT = False
        inval1 = True; inval2 = True; inval3 = True
        while not(inval_DGT):
            data1 = input(f"{data1_Inpt}   [N/A, N/A, N/A] \n>>> ")
            while inval1:
                if len(data1) >= 2:
                    if (data1.isalpha() == True) or (data1.isprintable() == False) or (data1.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                    elif data1.isdigit() == True:
                        for beta in data1:
                            if beta in "0":
                                if len(data1) >= 3:
                                    if float(data1) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data1 = input(f"\nFIRST (1st) Number Input \n{EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data1 = input(f"\nFIRST (1st) Number Input \n{num_dataInval}")
                                        break;
                                else:
                                    inval1 = False
                                    break;
                            elif float(data1) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                data1 = input(f"\nFIRST (1st) Number Input \n{EXC_valError}")
                                break;
                            else:
                                continue;
                        if inval1 == False:
                            break;
                    elif data1.replace("-","",10).isdigit() == True:
                        if int(data1) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            data1 = input(f"\nFIRST (1st) Number Input \n{NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                elif len(data1) == 1:
                    if data1.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                    else:
                        inval1 = False
                        break;
            os.system('cls') # The terminal output beforehand will be cleared.
            data2 = input(f"{data2_Inpt}  [{int(data1)}, N/A, N/A] \n>>> ")
            while inval2:
                if len(data2) >= 2:
                    if (data2.isalpha() == True) or (data2.isprintable() == False) or (data2.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                    elif data2.isdigit() == True:
                        for beta in data2:
                            if beta in "0":
                                if len(data2) >= 3:
                                    if float(data2) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data2 = input(f"\nSECOND (2nd) Number Input \n{EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data2 = input(f"\nSECOND (2nd) Number Input \n{num_dataInval}")
                                        break;
                                else:
                                    inval2 = False
                                    break;
                            elif float(data2) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                data2 = input(f"\nSECOND (2nd) Number Input \n{EXC_valError}")
                                break;    
                            else:
                                continue;
                        if inval2 == False:
                            break;
                    elif data2.replace("-","",10).isdigit() == True:
                        if int(data2) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            data2 = input(f"\nSECOND (2nd) Number Input \n{NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                elif len(data2) == 1:
                    if data2.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                    elif int(data2) == int(data1):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data2 = input(f"\nSECOND (2nd) Number Input \n[{int(data1)}, {int(data2)}, N/A] \n{num_duplcError}")
                        continue;
                    else:
                        inval2 = False
                        break;
            os.system('cls') # The terminal output beforehand will be cleared.
            data3 = input(f"{data3_Inpt}   [{int(data1)}, {int(data2)}, N/A] \n>>> ")
            while inval3:
                if len(data3) >= 2:
                    if (data3.isalpha() == True) or (data3.isprintable() == False) or (data3.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                    elif data3.isdigit() == True:
                        for beta in data3:
                            if beta in "0":
                                if len(data3) >= 3:
                                    if float(data3) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data3 = input(f"\nTHIRD (3rd) Number Input \n{EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        data3 = input(f"\nTHIRD (3rd) Number Input \n{num_dataInval}")
                                        break;
                                else:
                                    inval3 = False
                                    break;
                            elif float(data3) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                data3 = input(f"\nTHIRD (3rd) Number Input \n{EXC_valError}")
                                break;
                            else:
                                continue;
                        if inval3 == False:
                            break;
                    elif data3.replace("-","",10).isdigit() == True:
                        if int(data3) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            data3 = input(f"\nTHIRD (3rd) Number Input \n{NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                elif len(data3) == 1:
                    if data3.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                    elif int(data3) == int(data1) or int(data3) == int(data2):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        data3 = input(f"\nTHIRD (3rd) Number Input \n[{int(data1)}, {int(data2)}, {int(data3)}] \n{num_duplcError}")
                        continue;
                    else:
                        inval3 = False
                        break;

            fnl_data = [int(data1), int(data2), int(data3)]
            inval_DGT = True
            break;

        os.system('cls') # The terminal output beforehand will be cleared.
        print(f"\nPython will match it now! Did you win or not? \nYour Numbers: [{int(data1)}, {int(data2)}, {int(data3)}]\n")

        if sorted(fnl_data, reverse = True) == sorted(fnl_winNum, reverse = True):
            for alpha in range(countdownSec): # Objective: 3 seconds elapsed for the loop to exit
                if alpha == 0:
                    print("Matching in    " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                elif alpha == 1:
                    print("Evaluating in  " + str(countdownSec - alpha) + " ...") # 1 second elapsed
                elif alpha == 2:
                    print("Revealing in   " + str(countdownSec - alpha) + " ...") # 2 seconds elapsed
                time.sleep(1) # 1 second duration for every iteration
            os.system('cls') # The terminal output beforehand will be cleared.
            print(f"\nYour Number: {fnl_data} = Lotto Number: {fnl_winNum} | You Win!")
            winsound.PlaySound("Hello", winsound.SND_FILENAME)
            configRPT = input(f"{configRPT_Inpt}")
            os.system('cls') # The terminal output beforehand will be cleared.
            inval_IPT = False
            while not(inval_IPT): # While = Statement False. // while False + inval_IPT False ;= True to break.
                if configRPT.upper().replace(".,?!","",10) == "Y":
                    verRepeat = False
                    inval_IPT = True
                    break;
                elif configRPT.upper().replace(".,?!","",10) == "N":
                    verRepeat = True
                    inval_IPT = True
                    continue;
                else:
                    configRPT = input(f"{RPT_printError}")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    inval_IPT = False
                    break;
            if (verRepeat == True):
                break;
            elif (verRepeat == False):
                continue;
        elif verRepeat == True:
            break;
        else:
            for alpha in range(countdownSec): # Objective: 3 seconds elapsed for the loop to exit
                if alpha == 0:
                    print("Matching in    " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                elif alpha == 1:
                    print("Evaluating in  " + str(countdownSec - alpha) + " ...") # 1 second elapsed
                elif alpha == 2:
                    print("Revealing in   " + str(countdownSec - alpha) + " ...") # 2 seconds elapsed
                time.sleep(1) # 1 second duration for every iteration
            os.system('cls') # The terminal output beforehand will be cleared.
            print(f"\nYour Number: {fnl_data} = Lotto Number: {fnl_winNum} | You've Lost.")
            winsound.PlaySound("Hello", winsound.SND_FILENAME)
            configRPT = input(f"{configRPT_Inpt}")
            os.system('cls') # The terminal output beforehand will be cleared.
            inval_IPT = False
            while not(inval_IPT): # While = Statement False. // while False + inval_IPT False ;= True to break.
                if configRPT.upper().replace(".","",10) == "Y" or configRPT.upper().replace(".","",10) == "Y":
                    verRepeat = False
                    inval_IPT = True
                    prog_Intf()
                    break;
                elif configRPT.upper().replace(".","",10) == "N" or configRPT.upper().replace("!","",10) == "N":
                    verRepeat = True
                    inval_IPT = True
                    continue;
                else:
                    configRPT = input(f"{RPT_printError}")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    inval_IPT = False
            if (verRepeat == True):
                break;
            elif (verRepeat == False):
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