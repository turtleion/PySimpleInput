import sys
import os
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
            
            if 7 in args:
                if hasattr(sys, 'getandroidapilevel'):
                    raise Exception("Flag 7 is doesn't support in android (non-root)!")
                    break
                if sys.platform == "darwin":
                    from msvcrt import getch
                    key = ord(getch())
                    if key == 121:
                        # Yes
                        print("Yes")
                    elif key == 110:
                        #NO
                        print("No")

            if 8 in args and not self.nthinputted:
                print("Flag 8 U-CMD\n")
                p = self.input("Name of File: ", None, 2)
                if p == "" or p == None or p.isspace():
                    raise Exception("File cannot be writen : INVALID_FILENAME")
                    break
                pd = self.input("Path (ex. Users/McFrozie/WorkDir): ", None, 2)
                if pd == "" or pd == None or pd.isspace():
                    raise Exception("File cannot be writen : INVALID_PATH_NAME")
                    break
                if not os.path.isdir(pd):
                    raise Exception("File cannot be writen : INVALID_PATH_NOTDIR")
                    break

                with open(pd + "/" + p, 'w') as f:
                    f.write(str_input)
                    f.close()
                if not os.path.isfile(pd + "/" + p):

                    raise Exception("File cannot be writen : UNKNOWN_ERR")
                    break
                print("\nWRITE FILE SUCCESS\nFilename: " + p + "\nPath: " + pd + "\nCODE: WRITE_FILE_SUC")
                return True
                break

            return str_input
            break

    def testUnitProcedure(self):
        return True

# TEST

def test():
    t = PySimpleInput()
    return t.testUnitProcedure()
