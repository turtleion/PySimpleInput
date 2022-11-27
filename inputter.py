import sys
import warnings

class BetterInput:
    def __init__(self):
        print("Inputter has started")
        self.nthinputted = False

    # SET FLAG
    # 1 / REM_SPACE (REMOVE SPACE/WHITESPACE) used to remove all whitespace in the string
    # 2 / IGN_EMT_INPTD_ENTKEY (IGNORE ENTERKEY WHILE INPUTVAR IS EMPTY) used to ignore the enter key if the input is still empty
    # 3 / RQSTD_INTPD_RETURN (...) used to return data from input by converting the data type you need

    # input ARGUMENTS

    # self << represents the instance of the class
    # strg << string that used to make a question to the user
    # returnDatatypes << input data type that you need to convert user input data types (ex. int | this will change from originally a string to an integer) | ignored if flag 3 is not enabled
    #               to enable it you must pass last argument with 3 or RQSTD_INPTD_RETURN
    # *args << digunakan untuk mengaktifkan flag yang ada di anda masukan di argumen terakhir sesudah (self), strg, returnDatatypes
    # Enter flags here                                    VVVVVV
    #   inp = BettetInput.input("What is your name?",None,(HERE))

    def input(self,strg,returnDatatypes=None,*args):
        ectr= 0
        while ectr == 0:
            ectr+=1
            str_input = input(strg)
            # Check if user input nothing or only a space
            if not "REM_SPACE" in args or not 1 in args:
                if not "IGN_EMT_INTPD_ENTKEY" in args or not 2 in args:
                    if str_input == None or str_input.isspace() or str_input == "":
                        self.nthinputted = True
                        print("pWARNING ONLY | PROGRAM IS STILL RUNNING\nUser is inputted nothing or only a blank space, this may break the program!")
            # Used to remove all whitespace in the string
            
            if "REM_SPACE" in args or 1 in args and not self.nthinputted:
                tmp_str1 = str_input.split(" ")
                tmp_str1 = "".join(tmp_str1)
                self.backupStr = tmp_str1
                str_input = tmp_str1
            elif "REM_SPACE" in args and str_input.isspace() and not str_input == "":
                print("WARNING ONLY | PROGRAM STILL RUNNING\nUser is inputted a blank space this will return empty string!")
                str_input = ""
            elif "REM_SPACE" in args and self.nthinputted and not str_input == "":
                print("Cannot Remove all whitespace on the string!")

            # Used to ignore enter key while the input string are empty
            if "IGN_EMT_INPTD_ENTKEY" in args or 2 in args and str_input == "":
                ectr-=1

            if "RQSTD_INPTD_RETURN" in args or 3 and not returnDatatypes == None:
                if "str":
                    return str_input
                elif "int":
                    if not str_input.isnumeric():
                        raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters")
                    return int(str_input)
                elif "float":
                    if not str_input.isnumeric():                                             raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters")
                    return float(int(str_input))

            return str_input
            break


# HOW TO USE

betterinp = BetterInput()
sttrs = betterinp.input("Please Input your name!",None,2)
print(sttrs)
