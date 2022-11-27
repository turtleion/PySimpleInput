import sys
import warnings

class PySimpleInput:
    def __init__(self):

        self.nthinputted = False

    # SET FLAG
    # 1 / REM_SPACE (REMOVE SPACE/WHITESPACE) used to remove all whitespace in the string
    # 2 / IGN_EMT_INPTD_ENTKEY (IGNORE ENTERKEY WHILE INPUTVAR IS EMPTY) used to ignore the enter key if the input is still empty
    # 3 / RQSTD_INTPD_RETURN (...) used to return data from input by converting the data type you need

    def wiki(self):
        print("A Simple Python Library | v1.0PROTO\nThis library may help you with general input problem like user doesn't input anything it will break your program\nThis library is on development/prototype, Buggy\n\nMethod:\n\tinput()\n\t\tJust like python you need to give a question to shown to the user\n\t\tAll the arguments that required\n\n\t\t- input(strg, ...) | STRG <- This argument is REQUIRED\n\t\t\t(STRING) With this string, you can give a question to the user\n\n\t\t- input(strg,returnDatatypes,...)| RETURNDATATYPES <- This argument is optional\n\t\t\t(STRING) This argument will convert the datatypes of user input (ex. you want to get age from user but the datatype of user input are string, Simple. Just call int() function and all are done ||| But I can make it simple again, You can convert it without calling the int() function with only entering \"int\" in the returnDatatypes argument and this method is same like int() even you can do \"float\"\n\t\t\t(NOTE) THIS METHOD ARE REQUIRED FLAG 3 ACTIVATED!\n\n\t\tinput(strg,returnDatatypes,*FLAGS) | FLAGS <- This argument are optional except you want to use argument-method returnDatatypes (Flag 3)\n\t\t\t(INTEGER) This argument will activate the flag you wntered in the argument (ex. Flag 3 that needed for argument-method returnDatatypes). This arguments have 3 flags:\n\t\t\t\t- 1 : Remove All Whitespace = This flag will remove all whitespace in the user input | CANCELED if user input doesn't have amy whitespace again\n\t\t\t\t2 : Ignore User Press Enter While Input is Still Empty = This flag will ignoring user pressing enter while input is still empty\n\t\t\t\t3 : Selected Data Types = This flag is allow you to convert user input from string to other data types")
    def input(self,strg,returnDatatypes=None,*args):
        ectr= 0
        while ectr == 0:
            ectr+=1
            str_input = input(strg)
            # Check if user input nothing or only a space
            if  not 1 in args:
                if not 2 in args:
                    if str_input == None or str_input.isspace() or str_input == "":
                        self.nthinputted = True
                        print("blank string detected | flag nthinputted activated (NO_ISSUE)")
            # Used to remove all whitespace in the string
            
            if 1 in args and not self.nthinputted:
                tmp_str1 = str_input.split(" ")
                tmp_str1 = "".join(tmp_str1)
                self.backupStr = tmp_str1
                str_input = tmp_str1
            elif 1 in args and str_input.isspace() and not str_input == "":
                print("The user input string are empty | OPERATION CANCELED")
                str_input = ""
            elif 1 in args and self.nthinputted and not str_input == "":
                print("Cannot Remove all whitespace on the string | OPERATION CANCELED")

            # Used to ignore enter key while the input string are empty
            if 2 in args and str_input == "":
                ectr-=1
                continue

            if 3 and not returnDatatypes == None:
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

simple = PySimpleInput()
ss = simple.input("Please Input your name!",None,2)
print(ss)

simple.wiki()
