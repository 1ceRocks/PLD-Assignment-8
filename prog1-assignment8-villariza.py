# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random
verRepeat = False

while not(verRepeat):
    try:
        win_random1 = random.randint(0,9)
        win_random2 = random.randint(0,9)
        win_random3 = random.randint(0,9)
        fnl_win = [win_random1, win_random2, win_random3]

        inval_DGT = False
        inval1 = True; inval2 = True; inval3 = True
        while not(inval_DGT):
            data1 = input("\nEnter your FIRST number \n>>> ")
            while inval1:
                if len(data1) >= 2:
                    if (data1.isalpha() == True) or (data1.isprintable() == False) or (data1.isspace() == True):
                        data1 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    elif data1.replace("!@#$%^&*()_+[];',./?","", 20).isdigit():
                        if len(data1) >= 2:
                            data1 = input("\nNumerical inputs should range only on 0-9. \n>>> ")
                            continue;
                    else:
                        data1 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                elif len(data1) == 1:
                    if data1.isspace():
                        data1 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    else:
                        inval1 = True
                        break;
            data2 = input("\nEnter your SECOND number: \n>>> ")
            while inval2:
                if len(data2) >= 2:
                    if (data2.isalpha() == True) or (data2.isprintable() == False) or (data2.isspace() == True):
                        data2 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    elif data2.replace("!@#$%^&*()_+[];',./?","", 20).isdigit():
                        if len(data2) >= 2:
                            data2 = input("\nNumerical inputs should range only on 0-9. \n>>> ")
                            continue;
                    else:
                        data2 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                elif len(data2) == 1:
                    if data2.isspace():
                        data2 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    else:
                        inval2 = True
                        break;
            data3 = input("\nEnter your THIRD number: \n>>> ")
            while inval3:
                if len(data3) >= 2:
                    if (data3.isalpha() == True) or (data3.isprintable() == False) or (data3.isspace() == True):
                        data3 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    elif data3.replace("!@#$%^&*()_+[];',./?","", 20).isdigit():
                        if len(data3) >= 2:
                            data3 = input("\nNumerical inputs should range only on 0-9. \n>>> ")
                            continue;
                    else:
                        data3 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                elif len(data3) == 1:
                    if data3.isspace():
                        data3 = input("\nDo not include any unnecessary input/s on the program. \nPlease try again by typing and entering a numerical input that should only range from 0-9. \n>>> ")
                        continue;
                    else:
                        inval3 = True
                        break;

            fnl_data = [int(data1), int(data2), int(data3)]
            inval_DGT = True
            break;

        if fnl_data == fnl_win:
            print(f"\n{fnl_data} = {fnl_win} | Winner!\n")
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
                    configRPT = input(f"\nInvalid Input. Please try again by answering y/n \n>>> ")
                    inval_IPT = False
                    break;
            if (verRepeat == True):
                break;
            if (verRepeat == False):
                break;
        elif verRepeat == True:
            break;
        else:
            print(f"\n{fnl_data} = {fnl_win} | You loss\n")
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
                    configRPT = input(f"\nInvalid Input. Please try again by answering y/n \n>>> ")
                    inval_IPT = False
            if (verRepeat == True):
                break;
            if (verRepeat == False):
                continue;

    except ValueError or EOFError as delta:
        progError = '{0}'.format(delta)
        print(f"Invalid input. | {progError}")

print("\nOkay! You may now exit the game.\n")