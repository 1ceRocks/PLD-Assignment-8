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

guessNum = random.randint(0,100)
verRepeat = False # Acronym: Verify Repeat       | The main while loop of the program; when True, the program shall bound to stop and exit the terminal.
verConfig = True # Acronym: Verify Configuration | The second while loop of the program; when False, the program shall terminate the Verify Repeat User Input inside the program.
countdownSec = 1 # Acronym: Countdown Seconds    | The main int variable for Time Module.
os.system('cls') # The terminal output beforehand will be cleared.

"""
Variable Formats to be used for the program interface and settings.
"""
# Acronym: Program Greet       | The Entire Program Name Welcoming the User.
progGreet = '{}'.format("\n\033[0;1mWelcome to ❓🔢 \033[33m Villariza's \033[0;31;1mGuess the Number \033[32mGame\033[0m ❓🔢\n")

# Acronym: Exit Input          | A Formal Valedictory of the Program to the user.
progExt = '{}'.format("\n\n\033[0;1mThank you for playing ❓🔢 \033[33m Villariza's \033[0;31;1mGuess the Number \033[32mGame\033[0;1m ❓🔢 \033[0;1m! \nWe'll see you again next time! 🤝\n\n\033[0;34;1m💡 Python \033[33;1mInformation\033[0;1m: The \033[36mProgram\033[0;1m has been closed. 🔐\033[0m\n")

# Acronym: Program Information | General Indicator on the Program Settings.
progInfo = '{}'.format("\n\033[0m📍 \033[47;30;1mPROGRAM INFORMATION AND INSTRUCTIONS\033[0m 📌\n")

# Acronym: Program Variable A  | Progam Setting A.
prog_varA = '{}'.format("\n\033[0;94;1mA\033[0;1m. This \033[34mPy\033[0;33;1mthon\033[0;1m \033[36mProgram\033[0;1m will \033[35msecretly conduct\033[0;1m a \033[34mGuess Number\033[0;1m that would range from \033[33m(0-100)\033[0;1m.")

# Acronym: Program Variable B  | Progam Setting B.
prog_varB = '{}'.format("\n\033[0;94;1mB\033[0;1m. From there, you'll only \033[35mneed to guess\033[0;1m which number \033[34mPy\033[0;33;1mthon\033[0;1m has pulled \033[33mbetween the specified range\033[0;1m of \033[32mnumericals\033[0;1m.")

# Acronym: Program Variable C  | Progam Setting C.
prog_varC = '{}'.format("\n\033[0;94;1mC\033[0;1m. The \033[36mProgram\033[0;1m will \033[35mloop over and over\033[0;1m until your \033[0;33;4mnumerical input ↵\033[0;1m and \033[34mPy\033[0;33;1mthon\033[0;1m's \033[32mpulled number\033[0;1m match consequently.")

# Acronym: Program Variable D  | Progam Setting D.
prog_varD = '{}'.format("\n\033[0;94;1mD\033[0;1m. \033[35mIf\033[0;1m your \033[0;33;4mnumerical input ↵\033[0;1m is \033[33;4;1mgreater than\033[0;1m the \033[34mPy\033[0;33;1mthon\033[0;1m's pulled number, the program will state its response \033[32m(Greater Than)\033[0;1m and continue its loop; \033[35mvice versa\033[0;1m.")

# Acronym: Program Variable E  | Progam Setting E.
prog_varE = '{}'.format("\n\033[0;94;1mE\033[0;1m. \033[35mIf\033[0;1m your \033[0;33;4mnumerical input ↵\033[0;1m is \033[33;4;1mless than\033[0;1m the \033[34mPy\033[0;33;1mthon\033[0;1m's pulled number,     '' \033[32m''\033[0;1m ; \033[35mvice versa\033[0;1m.")

# Acronym: Program Variable F  | Progam Setting F.
prog_varF = '{}'.format("\n\033[0;94;1mF\033[0;1m. After \033[35myou've gussed\033[0;1m the right number \033[33m(as answer)\033[0;1m, it will ask you to \033[35mrepeat the game\033[0;1m or \033[35mmainly\033[0;1m exit the \033[36mProgram\033[0;1m.")

# Aggregated variable formats to be printed as def-named function. << (Also used for the user input to repeat the program or game).
def prog_Intf():
    print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD, prog_varE, prog_varF)
prog_Intf()

"""
Variable Invalid or Error Formats to be used on the main program below.
"""
# Acronym: User Input Error      | User did not input any numerical integer or is in character invalidity.
usr_InputError = "{}".format(f"\n\033[0;31;1mInvalid Input\033[0;1m. Your \033[0;33;4mnumerical input ↵\033[0;1m must be ranging from \033[0;33;4m(0-100)\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Verify Repeat Error   | User not inputting "Yes" or "No" on the program repeat or is in character invalidity.
verRPT_Error = "{}".format(f"\n\033[0;31;1mInvalid Input\033[0;1m. Your \033[0;33;4minput ↵\033[0;1m must only be in \033[36mCharacters\033[0;1m \"\033[34mYes\033[0;1m\" or \"\033[33mNo\033[0;1m\". \n\n\033[34mYes \033[0;31;1m,\033[0;1m \033[33mNo\033[0;1m \033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;35;1m")

# Acronym: Negative Value Error  | User Numerical Input - Less than 0 (Negative Integers).
NEG_valError = "{}".format(f"\n\033[0;31;1mInvalid Input\033[0;1m. Your \033[0;33;4mnumerical input ↵\033[0;1m is \033[35mless than\033[0;1m \033[32m0\033[0;1m as shown:")

# Acronym: Excel Value Error     | User Numerical Input - Greater than or Equal to 10 (Regarded Range: 0-9).
EXC_valError = "{}".format(f"\n\033[0;31;1mInvalid Input\033[0;1m. Your \033[0;33;4mnumerical input ↵\033[0;1m is \033[35mgreater than\033[0;1m \033[32m100\033[0;1m as shown:")

"""
The General Format Variables for User Numerical Input
"""
# Acronym: Program user Input         | User Numerical Input.
prog_usrInput = "{}".format("\n\033[0;35;1mType and Enter\033[0;1m your \033[31m❓GUESS❓\033[0;1m on the provided \033[0;33;4mnumerical input ↵\033[0;1m below. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Verify Input               | User Character Input.
verRPT_Input = "{}".format("\n\033[0;1mDo you want to try again? \033[0;35;1mAnswer\033[0;1m only in \033[36mAlpbetical Character\033[0;1m \"\033[34mYes\033[0;1m\" \033[31m/\033[0;1m \"\033[33mNo\033[0;1m\" \n\n\033[34mYes\033[34m \033[0;31;1m,\033[0;1m \033[33mNo\033[0;1m \033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;35;1m")

# Acronym: Greater Than Tip           | User Greater Numerical Input.
GTR_Tip = "{}".format("\033[0;36;1mTIP \n\033[0;35;1mTry \033[32mincrementing the integer\033[0;1m of your \033[0;33;4mnumerical input ↵\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Less Than Tip              | User Lesser Numerical Input.
LESS_Tip = "{}".format("\033[0;36;1mTIP \n\033[0;35;1mTry \033[31mdecreasing the integer\033[0;1m of your \033[0;33;4mnumerical input ↵\033[0;1m. \n\n\033[34m>\033[0;34;1m>\033[0;33;1m> \033[0;32;1m")

# Acronym: Peripheral Greater Number  | Print Function Output.
pphl_greatNum = '{}'.format("\n\033[0;32;1mGreater than\033[0;1m the \033[34;1mGuess Number\033[0;1m.\n\033[36mYour Input: \033[0;32;1m")

# Acronym: Peripheral Lesser Number   | Print Function Output.
pphl_lessNum = '{}'.format("\n\033[0;31;1mLess than\033[0;1m the \033[34;1mGuess Number\033[0;1m.\n\033[36mYour Input: \033[0;32;1m")

"""
THE ENTIRE METHOD OF VILLARIZA'S GUESS THE NUMBER GAME PROGRAM

Table of Contents: Acronym for the Variables Used

alpha        = Alpha
config_Inpt  = Configuration Input
data         = Data (1st, 2nd, 3rd)
delta        = Delta
EOFError     = End Of File Error
fnl_Input    = Final Input
progError    = Program Error
guessNum     = Guess Number
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
                    print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                time.sleep(1)
            os.system('cls') # The terminal output beforehand will be cleared.
            user_Input = input(f"{usr_InputError}")
            os.system('cls') # The terminal output beforehand will be cleared.
            continue;
        elif user_Input.replace("-","",10).isdigit():
            fnl_Input = int(user_Input)
            if fnl_Input == guessNum:
                for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                    if alpha == 0:
                        print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                time.sleep(1)
                os.system('cls') # The terminal output beforehand will be cleared.
                print(f"\n\033[0;1mYour \033[31m❓GUESS❓\033[0;1m is \033[32mcorrect\033[0;1m! \n\n\033[36mYour Input\033[0;1m: \033[32m{fnl_Input}\033[0;1m \n\033[34mGuess Number\033[0;1m: \033[32m{guessNum}\033[0m\n")
                winsound.PlaySound("Hello", winsound.SND_FILENAME)
                config_Inpt = input(f"{verRPT_Input}")
                os.system('cls') # The terminal output beforehand will be cleared.
                while verConfig: # While = Statement False. // while False + verConfig True ;= False to break.
                    if (config_Inpt.replace(".","",10).upper() or config_Inpt.replace("!","",10).upper()) == "YES":
                        for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                            if alpha == 0:
                                print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
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
                                print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                        time.sleep(1)
                        os.system('cls') # The terminal output beforehand will be cleared.
                        config_Inpt = input(f"{verRPT_Error}")
                        os.system('cls') # The terminal output beforehand will be cleared.
                        continue;
            elif fnl_Input < 0 or fnl_Input > 100:
                if fnl_Input < 0:
                    for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                        if alpha == 0:
                            print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                    time.sleep(1)
                    os.system('cls') # The terminal output beforehand will be cleared.
                    user_Input = input(f"{NEG_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    continue;
                elif fnl_Input > 100:
                    for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                        if alpha == 0:
                            print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                    time.sleep(1)
                    os.system('cls') # The terminal output beforehand will be cleared.
                    user_Input = input(f"{EXC_valError} {fnl_Input:,} \nIt should range from (0-100); please try again. \n>>> ")
                    os.system('cls') # The terminal output beforehand will be cleared.
                    continue;
            elif fnl_Input < guessNum:
                os.system('cls') # The terminal output beforehand will be cleared.
                print(f"{pphl_lessNum} {fnl_Input}\033[0m\n")
                user_Input = input(f"{GTR_Tip}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
            elif fnl_Input > guessNum:
                print(f"{pphl_greatNum} {fnl_Input}\033[0m\n")
                user_Input = input(f"{LESS_Tip}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
            else:
                for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                    if alpha == 0:
                        print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
                time.sleep(1)
                os.system('cls') # The terminal output beforehand will be cleared.
                user_Input = input(f"{usr_InputError}")
                os.system('cls') # The terminal output beforehand will be cleared.
                continue;
        else:
            for alpha in range(countdownSec): # Objective: 1 second shall elapse for the loop to exit
                if alpha == 0:
                    print("\033[0;33;1mEvaluating in " + str(countdownSec - alpha) + " ...\033[0m") # 0 second elapsed
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
