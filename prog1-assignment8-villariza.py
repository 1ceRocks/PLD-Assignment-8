# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import os, random, sys, time, winsound
verRepeat = False
os.system('cls')

#
progGreet = "{}".format(f"\n$! Welcome to Villariza Lottery !$\n")
progInfo = "{}".format(f"\nPROGRAM INFORMATION AND INSTRUCTIONS")
prog_varA = "{}".format(f"\nA. You just simply have to input THREE (3) random numbers ranging from 0-9 on the terminal.")
prog_varB = '{varA} e.g. {varB}'.format(varA = f"\nB. The Program will input THREE (3) Random Winning Numbers regarded on the Lottery Menu.", varB = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)])
prog_varC = "{}".format(f"\nC. If the Random Winning Numbers matches with your Numerical Input, then the program output will respond saying \"You Win!\"")
prog_varD = "{}".format(f"\nD. If the Random Winning Numbers does not match with your Numerical Input, then the program output will respond saying \"You've Lost.\"")

print(progGreet, progInfo, prog_varA, prog_varB, prog_varC, prog_varD)

#
num_dataInval = '{}'.format("\nNumerical inputs should range only on 0-9. \n>>> ")
alnum_printError = '{}'.format("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
RPT_printError = '{}'.format("\nInvalid Input. Please try again by answering Y / N (Yes / No) \nY , N >>> ")

#
data1_Inpt = '{}'.format("\nEnter your FIRST (1st) number on the space provided below.")
data2_Inpt = '{}'.format("\nEnter your SECOND (2nd) number on the space provided below.")
data3_Inpt = '{}'.format("\nEnter your THIRD (3rd) number on the space provided below.")
configRPT_Inpt = '{}'.format("\nTry again? Answer only in characters Y / N (Yes / No) \nY , N >>> ")
countdownSec = 3

while not(verRepeat):
    try:
        win_random1 = random.randint(0,9)
        win_random2 = random.randint(0,9)
        win_random3 = random.randint(0,9)
        fnl_win = [win_random1, win_random2, win_random3]

        inval_DGT = False
        inval1 = True; inval2 = True; inval3 = True
        while not(inval_DGT):
            data1 = input(f"{data1_Inpt}   [N/A, N/A, N/A] \n>>> ")
            while inval1:
                if len(data1) >= 2:
                    if (data1.isalpha() == True) or (data1.isprintable() == False) or (data1.isspace() == True):
                        os.system('cls')
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                    elif data1.isdigit() == True:
                        for beta in data1:
                            if beta in "0":
                                if len(data1) >= 3:
                                    os.system('cls')
                                    data1 = input(f"\nFIRST (1st) Number Input \n{num_dataInval}")
                                    break;
                                else:
                                    inval1 = False
                                    break;
                            else:
                                continue;
                        if inval1 == False:
                            break;
                    else:
                        os.system('cls')
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                elif len(data1) == 1:
                    if data1.isspace():
                        os.system('cls')
                        data1 = input(f"\nFIRST (1st) Number Input \n{alnum_printError}")
                        continue;
                    else:
                        inval1 = False
                        break;
            os.system('cls')
            data2 = input(f"{data2_Inpt}  [{int(data1)}, N/A, N/A] \n>>> ")
            while inval2:
                if len(data2) >= 2:
                    if (data2.isalpha() == True) or (data2.isprintable() == False) or (data2.isspace() == True):
                        os.system('cls')
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                    elif data2.isdigit() == True:
                        for beta in data2:
                            if beta in "0":
                                if len(data2) >= 3:
                                    os.system('cls')
                                    data2 = input(f"\nSECOND (2nd) Number Input \n{num_dataInval}")
                                    break;
                                else:
                                    inval2 = False
                                    break;
                            else:
                                continue;
                        if inval2 == False:
                            break;
                    else:
                        os.system('cls')
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                elif len(data2) == 1:
                    if data2.isspace():
                        os.system('cls')
                        data2 = input(f"\nSECOND (2nd) Number Input \n{alnum_printError}")
                        continue;
                    else:
                        inval2 = False
                        break;
            os.system('cls')
            data3 = input(f"{data3_Inpt}   [{int(data1)}, {int(data2)}, N/A] \n>>> ")
            while inval3:
                if len(data3) >= 2:
                    if (data3.isalpha() == True) or (data3.isprintable() == False) or (data3.isspace() == True):
                        os.system('cls')
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                    elif data3.isdigit() == True:
                        for beta in data3:
                            if beta in "0":
                                if len(data3) >= 3:
                                    os.system('cls')
                                    data3 = input(f"\nTHIRD (3rd) Number Input \n{num_dataInval}")
                                    break;
                                else:
                                    inval3 = False
                                    break;
                            else:
                                continue;
                        if inval3 == False:
                            break;
                    else:
                        os.system('cls')
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                elif len(data3) == 1:
                    if data3.isspace():
                        os.system('cls')
                        data3 = input(f"\nTHIRD (3rd) Number Input \n{alnum_printError}")
                        continue;
                    else:
                        inval3 = False
                        break;

            fnl_data = [int(data1), int(data2), int(data3)]
            inval_DGT = True
            break;

        os.system('cls')
        print(f"\nPython will match it now! Did you win or not?\nYour Numbers: [{int(data1)}, {int(data2)}, {int(data3)}]\n")

        if sorted(fnl_data, reverse = True) == sorted(fnl_win, reverse = True):
            for beta in range(countdownSec):
                if beta == 0:
                    print("Matching in    " + str(countdownSec - beta) + " ...")
                elif beta == 1:
                    print("Evaluating in  " + str(countdownSec - beta) + " ...")
                elif beta == 2:
                    print("Revealing in   " + str(countdownSec - beta) + " ...")
                time.sleep(10)
            os.system('cls')
            print(f"\nYour Num: {fnl_data} = Lotto Num: {fnl_win} | You Win!")
            winsound.PlaySound("Hello", winsound.SND_FILENAME)
            configRPT = input("\nTry again y/n \n>>> ")
            inval_IPT = False
            while not(inval_IPT):
                if configRPT.upper().replace(".,?!","",10) == "Y":
                    verRepeat = False
                    inval_IPT = True
                    break;
                elif configRPT.upper().replace(".,?!","",10) == "N":
                    verRepeat = True
                    inval_IPT = True
                    continue;
                else:
                    configRPT = input(f"{configRPT_Inpt}")
                    inval_IPT = False
                    break;
            if (verRepeat == True):
                break;
            if (verRepeat == False):
                break;
        elif verRepeat == True:
            break;
        else:
            for beta in range(countdownSec):
                if beta == 0:
                    print("Matching in    " + str(countdownSec - beta) + " ...")
                elif beta == 1:
                    print("Evaluating in  " + str(countdownSec - beta) + " ...")
                elif beta == 2:
                    print("Revealing in   " + str(countdownSec - beta) + " ...")
                time.sleep(1)
            os.system('cls')
            print(f"\nYour Num: {fnl_data} = Lotto Num: {fnl_win} | You've Lost.")
            winsound.PlaySound("Hello", winsound.SND_FILENAME)
            configRPT = input(f"{configRPT_Inpt}")
            os.system('cls')
            inval_IPT = False
            while not(inval_IPT):
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
                    os.system('cls')
                    inval_IPT = False
            if (verRepeat == True):
                break;
            if (verRepeat == False):
                continue;

    except ValueError or EOFError as delta:
        progError = '{0}'.format(delta)
        print(f"Invalid input. | {progError}")

    finally:
        None

os.system('cls')
print("\nThank you for playing $! Villariza Lottery $! \nWe'll see you again next time! \n\nPython Info: The program has been closed.\n")
sys.exit()