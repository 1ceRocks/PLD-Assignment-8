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
progGreet = "{}".format(f"\n\033[0;92;1mWelcome to\033[0m \033[41;33;1m🎰 Villariza Lottery 🎰\033[0m\n")

# Acronym: Exit Input          | A Formal Valedictory of the Program to the user.
progExt = '{}'.format("\n\033[0;1mThank you for playing \033[0;41;33;1m🎰 Villariza Lottery 🎰\033[0;1m !\nWe'll see you again next time! 🤝\n\n\033[0;34;1m💡 Python \033[33;1mInformation\033[0;1m: The \033[36mProgram\033[0;1m has been closed. 🔐\033[0m\n")

# Acronym: Program Information | General Indicator on the Program Settings.
progInfo = "{}".format(f"\n\033[0m📍 \033[47;30;1mPROGRAM INFORMATION AND INSTRUCTIONS\033[0m 📌\n")

# Acronym: Program Variable A  | Progam Setting A.
prog_varA = "{}".format(f"\n\033[0;94;1mA\033[0;1m. You just simply have to generate \033[92;1mTHREE (3) Random Numbers\033[0;1m as your \033[0;33;4mnumerical input ↵\033[0;1m that will only range from \033[0;33;1m(0-9).\033[0m")

# Acronym: Program Variable B  | Progam Setting B.
prog_varB = '{varA} \033[0;36;3;1me.g. \033[0;41;33;1m{varB}\033[0m'.format(varA = f"\n\033[0;94;1mB\033[0;1m. \033[0;35;1mVice versa\033[0;1m; the \033[0;36;1mProgram will also \033[33;4mgenerate ↵\033[0m \033[92;1mTHREE (3) Winning Numbers\033[0;1m regarded in the \033[33;1mLottery Menu\033[0m.", varB = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)])

# Acronym: Program Variable C  | Progam Setting C.
prog_varC = "{}".format(f"\n\033[0;94;1mC\033[0;1m. \033[0;35;1mIf\033[0;1m the \033[92mWinning Numbers \033[0;33;4;1mmatches\033[0;1m with your \033[92mRandom Numbers\033[0;1m, then the program output \033[0;35;1mshall respond\033[0;1m saying \033[0;36;3;1m\"You Win!\"\033[0;1m.")

# Acronym: Program Variable D  | Progam Setting D.
prog_varD = "{}".format(f"\n\033[0;94;1mD\033[0;1m. \033[0;35;1mIf\033[0;1m the \033[92mWinning Numbers \033[0;33;4;1mdoes not match\033[0;1m with your \033[92mRandom Numbers\033[0;1m, '' \033[0;35;1m'' \033[0;36;3;1m\"You Lost.\"\033[0;1m.")

# Aggregated variable formats to be printed as def-named function. << (Also used for the user input to repeat the program or game).
def prog_Intf():
    print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD)
prog_Intf()

"""
Variable Invalid or Error Formats to be used on the main program below.
"""
# Acronym: Number Data Invalid         | Inputs should range only on 0-9.
num_dataInval = '{}'.format("\n\033[0;32;1mRandom Number\033[0;1m should only \033[0;35;1mrange\033[0;1m from \033[33m(0-9)\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Alpha-Numerical Print Error | Inputs should range only on 0-9.
alnum_printError = '{}'.format("\n\033[0;35;1mDo not include any \033[0;33;4munnecessary input/s ↵\033[0;1m on the \033[0;36;1mProgram\033[0;1m. \nPlease try again by generating a \033[0;32;1mRandom Number\033[0;1m that would range from \033[33m(0-9)\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Number Duplicate Error      | Duplicated Numerical Input.
num_duplcError = '{}'.format("\n\033[0;1mYour \033[32mRandom Number\033[0;1m should \033[0;35;1mnot be the same\033[0;1m as your \033[0;33;4mprevious input ↵\033[0;1m stored in the \033[33;1mLottery Menu\033[0;1m. \nPlease try again by generating a different \033[32mRandom Number\033[0;1m on your \033[0;33;4minput ↵\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Repeating Print Error       | User not inputting "Y" or "N" on the program repeat.
RPT_printError = '{}'.format("\n\033[0;31;1mInvalid Input\033[0;1m. Please try again by \033[0;35;1manswering\033[0;1m \"\033[34mY\033[0;1m\" \033[31m/\033[0;1m \"\033[33mN\033[0;1m\" (\033[34mYes\033[0;1m \033[31m/\033[0;1m \033[33mNo\033[0;1m) \n\n\033[34mY\033[34m \033[0;31;1m,\033[0;1m \033[33mN\033[0;1m \033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;35;1m")

# Acronym: Negative Value Error        | User Numerical Input - Less than 0 (Negative Integers).
NEG_valError = '{}'.format("\n\033[0;1mYour \033[0;32;1mRandom Number\033[0;1m is \033[0;35;1mless than\033[0;32;1m0\033[0;1m; typically a \033[31mNegative Integer\033[0;1m. \nPlease try again by generating a \033[0;32;1mRandom Number\033[0;1m that would range from \033[33m(0-9)\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Excel Value Error           | User Numerical Input - Greater than or Equal to 10 (Regarded Range: 0-9).
EXC_valError = '{}'.format("\n\033[0;1mYour \033[0;32;1mRandom Number\033[0;1m is \033[0;35;1mgreater than \033[0;32;1m9\033[0;1m; typically an \033[31mExcel Integer\033[0;1m. \nPlease try again by generating a \033[0;32;1mRandom Number\033[0;1m that would range from \033[33m(0-9)\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

"""
The General Format Variables for User Numerical Input
"""
# Acronym: First (1st) Data Input      | User Numerical Input.
data1_Inpt = '{}'.format("\n\033[0;35;1mGenerate\033[0;1m your \033[36mFIRST (1st)\033[0;32;1m Random Number\033[0;1m on the \033[33;4minput ↵\033[0;1m provided below.")

# Acronym: Second (2nd) Data Input     | User Numerical Input.
data2_Inpt = '{}'.format("\n\033[0;35;1mGenerate\033[0;1m your \033[36mSECOND (2nd)\033[0;32;1m Random Number\033[0;1m on the \033[33;4minput ↵\033[0;1m provided below.")

# Acronym: Third (3rd) Data Input      | User Numerical Input.
data3_Inpt = '{}'.format("\n\033[0;35;1mGenerate\033[0;1m your \033[36mTHIRD (3rd)\033[0;32;1m Random Number\033[0;1m on the \033[33;4minput ↵\033[0;1m provided below.")

# Acronym: Configuration Repeat Input  | User Character Input (Y / N).
configRPT_Inpt = '{}'.format("\n\033[0;1mDo you want to try again? \033[0;35;1mAnswer\033[0;1m only in \033[36mAlpbetical Character\033[0;1m \"\033[34mY\033[0;1m\" \033[31m/\033[0;1m \"\033[33mN\033[0;1m\" (\033[34mYes\033[0;1m \033[31m/\033[0;1m \033[33mNo\033[0;1m) \n\n\033[34mY\033[34m \033[0;31;1m,\033[0;1m \033[33mN\033[0;1m \033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;35;1m")

# Acronym: Configuration Repeat Input  | Print Function Output.
pphl_data1 = '{}'.format("\n\033[0;36;1mFIRST (1st)\033[0;32;1m Random Number\033[0m\n")

# Acronym: Configuration Repeat Input  | Print Function Output.
pphl_data2 = '{}'.format("\n\033[0;36;1mSECOND (2nd)\033[0;32;1m Random Number\033[0m\n")

# Acronym: Configuration Repeat Input  | Print Function Output.
pphl_data3 = '{}'.format("\n\033[0;36;1mTHIRD (3rd)\033[0;32;1m Random Number\033[0m\n")

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
            data1 = input(f"{data1_Inpt}   \033[0;41;33;1m[N/A, N/A, N/A]\033[0m \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")
            while inval1:
                if len(data1) >= 2:
                    if (data1.isalpha() == True) or (data1.isprintable() == False) or (data1.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data1 = input(f"{pphl_data1} {alnum_printError}")
                        continue;
                    elif data1.isdigit() == True:
                        for beta in data1:
                            if beta in "0":
                                if len(data1) >= 3:
                                    if float(data1) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data1 = input(f"{pphl_data1} {EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data1 = input(f"{pphl_data1} {num_dataInval}")
                                        break;
                                else:
                                    inval1 = False
                                    break;
                            elif float(data1) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                prog_Intf()
                                data1 = input(f"{pphl_data1} {EXC_valError}")
                                break;
                            else:
                                continue;
                        if inval1 == False:
                            break;
                    elif data1.replace("-","",10).isdigit() == True:
                        if int(data1) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            prog_Intf()
                            data1 = input(f"{pphl_data1} {NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data1 = input(f"{pphl_data1} {alnum_printError}")
                        continue;
                elif len(data1) == 1:
                    if data1.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data1 = input(f"{pphl_data1} {alnum_printError}")
                        continue;
                    else:
                        inval1 = False
                        break;
                else:
                    os.system('cls') # The terminal output beforehand will be cleared.
                    prog_Intf()
                    data1 = input(f"{pphl_data1} {alnum_printError}")
                    continue;
            os.system('cls') # The terminal output beforehand will be cleared.
            prog_Intf()
            data2 = input(f"{data2_Inpt}  \033[41;33;1m[{int(data1)}, N/A, N/A]\033[0m \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")
            while inval2:
                if len(data2) >= 2:
                    if (data2.isalpha() == True) or (data2.isprintable() == False) or (data2.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data2 = input(f"{pphl_data2} {alnum_printError}")
                        continue;
                    elif data2.isdigit() == True:
                        for beta in data2:
                            if beta in "0":
                                if len(data2) >= 3:
                                    if float(data2) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data2 = input(f"{pphl_data2} {EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data2 = input(f"{pphl_data2} {num_dataInval}")
                                        break;
                                elif len(data2) == 2:
                                    if int(data2) == int(data1):
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data2 = input(f"{pphl_data2} \033[0;41;33;1m[{int(data1)}, N/A, N/A]\033[0m \n{num_duplcError}")
                                        continue;
                                    else:
                                        inval2 = False
                                        break;
                                else:
                                    inval2 = False
                                    break;
                            elif float(data2) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                prog_Intf()
                                data2 = input(f"{pphl_data2} {EXC_valError}")
                                break;    
                            else:
                                continue;
                        if inval2 == False:
                            break;
                    elif data2.replace("-","",10).isdigit() == True:
                        if int(data2) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            prog_Intf()
                            data2 = input(f"{pphl_data2} {NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data2 = input(f"{pphl_data2} {alnum_printError}")
                        continue;
                elif len(data2) == 1:
                    if data2.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data2 = input(f"{pphl_data2} {alnum_printError}")
                        continue;
                    elif int(data2) == int(data1):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data2 = input(f"{pphl_data2} \033[0;41;33;1m[{int(data1)}, N/A, N/A]\033[0m \n{num_duplcError}")
                        continue;
                    else:
                        inval2 = False
                        break;
                else:
                    os.system('cls') # The terminal output beforehand will be cleared.
                    prog_Intf()
                    data2 = input(f"{pphl_data2} {alnum_printError}")
                    continue;
            os.system('cls') # The terminal output beforehand will be cleared.
            prog_Intf()
            data3 = input(f"{data3_Inpt}   \033[0;41;33;1m[{int(data1)}, {int(data2)}, N/A]\033[0m \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")
            while inval3:
                if len(data3) >= 2:
                    if (data3.isalpha() == True) or (data3.isprintable() == False) or (data3.isspace() == True):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data3 = input(f"{pphl_data3} {alnum_printError}")
                        continue;
                    elif data3.isdigit() == True:
                        for beta in data3:
                            if beta in "0":
                                if len(data3) >= 3:
                                    if float(data3) >= 100:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data3 = input(f"{pphl_data3} {EXC_valError}")
                                        continue;
                                    else:
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data3 = input(f"{pphl_data3} {num_dataInval}")
                                        break;
                                elif len(data3) == 2:
                                    if int(data3) == int(data1) or int(data3) == int(data2):
                                        os.system('cls') # The terminal output beforehand will be cleared.
                                        prog_Intf()
                                        data3 = input(f"{pphl_data3} \033[0;41;33;1m[{int(data1)}, {int(data2)}, N/A]\033[0m \n{num_duplcError}")
                                        continue;
                                    else:
                                        inval3 = False
                                        break;
                                else:
                                    inval3 = False
                                    break;
                            elif float(data3) >= 10:
                                os.system('cls') # The terminal output beforehand will be cleared.
                                prog_Intf()
                                data3 = input(f"{pphl_data3} {EXC_valError}")
                                break;
                            else:
                                continue;
                        if inval3 == False:
                            break;
                    elif data3.replace("-","",10).isdigit() == True:
                        if int(data3) <= -1:
                            os.system('cls') # The terminal output beforehand will be cleared.
                            prog_Intf()
                            data3 = input(f"{pphl_data3} {NEG_valError}")
                            continue;
                    else:
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data3 = input(f"{pphl_data3} {alnum_printError}")
                        continue;
                elif len(data3) == 1:
                    if data3.isspace():
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data3 = input(f"{pphl_data3} {alnum_printError}")
                        continue;
                    elif int(data3) == int(data1) or int(data3) == int(data2):
                        os.system('cls') # The terminal output beforehand will be cleared.
                        prog_Intf()
                        data3 = input(f"{pphl_data3} \033[0;41;33;1m[{int(data1)}, {int(data2)}, N/A]\033[0m \n{num_duplcError}")
                        continue;
                    else:
                        inval3 = False
                        break;
                else:
                    os.system('cls') # The terminal output beforehand will be cleared.
                    prog_Intf()
                    data3 = input(f"{pphl_data3} {alnum_printError}")
                    continue;

            fnl_data = [int(data1), int(data2), int(data3)]
            inval_DGT = True
            break;

        os.system('cls') # The terminal output beforehand will be cleared.
        print(f"\n\033[0mPython will match it now! Did you win or not? \nYour Numbers: \033[0;41;33;1m[{int(data1)}, {int(data2)}, {int(data3)}]\033[0m\n")

        if sorted(fnl_data, reverse = True) == sorted(fnl_winNum, reverse = True):
            for alpha in range(countdownSec): # Objective: 3 seconds shall elapse for the loop to exit
                if alpha == 0:
                    print("Matching in    " + str(countdownSec - alpha) + " ...") # 0 second elapsed
                elif alpha == 1:
                    print("Evaluating in  " + str(countdownSec - alpha) + " ...") # 1 second elapsed
                elif alpha == 2:
                    print("Revealing in   " + str(countdownSec - alpha) + " ...") # 2 seconds elapsed
                time.sleep(1) # 1 second duration for every iteration
            os.system('cls') # The terminal output beforehand will be cleared.
            print(f"\nYour Number: {fnl_data} = Lotto Number: {fnl_winNum} | \033[32;1You Win\033[0m!")
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
                    print("\033[0;31;1mMatching in\033[0;1m    " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                elif alpha == 1:
                    print("\033[0;33;1mEvaluating in\033[0;1m  " + str(countdownSec - alpha) + " ...\033[0m") # 1 second elapsed
                elif alpha == 2:
                    print("\033[0;32;1mRevealing in\033[0;1m   " + str(countdownSec - alpha) + " ...\033[0m") # 2 seconds elapsed
                time.sleep(1) # 1 second duration for every iteration
            os.system('cls') # The terminal output beforehand will be cleared.
            print(f"\n\033[0;1mYour Number: \033[0;41;33;1m{fnl_data}\033[0;1m \033[35m=\033[0;1m Lotto Number: \033[0;41;33;1m{fnl_winNum}\033[0;1m | \033[31mYou Lost\033[0m.")
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