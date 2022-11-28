import sys
import warnings

class PySimpleInput:
    def __init__(self):

        self.nthinputted = False


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

            if 3 in args and not returnDatatypes == None:
                if "str":
                    return str_input
                elif "int":
                    if not str_input.isnumeric():
                        raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters\n\nSolution:\n\tActivate flags number 4")
                    return int(str_input)
                elif "float":
                    if not str_input.isnumeric():                                             raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters")
                    return float(int(str_input))
            if 4 in args and not self.nthinputted:
                if str_input.isalpha():
                    print("Cannot filter all numeric number, No Numeric numbers are detected")
                    break
                str_input = "".join(filter(str.isdigit, str_input))
            
            if 5 in args and not self.nthinputted:
                str_input = str_input.upper()

            if 6 in args and not self.nthinputted:
                str_input = str_input.lower()
                
            return str_input
            break

    def testUnitProcedure(self):
        return True

# TEST

def test():
    t = PySimpleInput()
    return t.testUnitProcedure()
