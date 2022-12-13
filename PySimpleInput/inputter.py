import sys
import os
from validate_email import validate_email
import phonenumbers
import check_url

class PySimpleInput:
    def filterAlpha(self,x):
        num = x[:]
        for char in num:
            try:
                if char.isnumeric():
                    del num[num.index(char)]
            except:
                pass

        recnum = []
        for g in num:
            recnum.append(str(g))

        return recnum
    def __init__(self):

        self.nthinputted = False


    def input(self,strg,options=[],options_arg={}):
        ectr= 0
        while ectr == 0:
            ectr+=1
            str_input = input(strg)
            # Check if user input nothing or only a space
            if str_input == None or str_input.isspace() or str_input == "":
                        self.nthinputted = True
            # Used to remove all whitespace in the string
            # Non Flags



            if "remove_whitespace" in options and not self.nthinputted:
                tmp_str1 = str_input.split(" ")
                tmp_str1 = "".join(tmp_str1)
                self.backupStr = tmp_str1
                str_input = tmp_str1
            elif "remove_whitespace" in options and str_input.isspace() and not str_input == "":
                print("The user input string are empty")
                str_input = ""
            elif "remove_whitespace" in options and self.nthinputted and not str_input == "":
                print("Cannot Remove all whitespace on the string")

            # Used to ignore enter key while the input string are empty
            if "prevent_enterkeypress" in options and str_input == "":
                ectr-=1
                print("You must enter a text/string to continue")
                continue

            if "convert_datatype" in options:
                try:
                    if not options_arg["convert_datatype"] == "" or not options_arg["convert_datatype"].isspace() or not options_arg == None:
                        if "str" == options_arg["convert_datatype"]:
                            return str_input
                        elif "int" == options_arg["convert_datatype"]:
                            if not str_input.isnumeric():
                                raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters\n\nSolution:\n\toptions \"filter_num\"")
                            return int(str_input)
                        elif "float" == options_ar["convert_datatype"]:
                            if not str_input.isnumeric():
                                    raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters")
                            return float(int(str_input))
                except (KeyError, IndexError):
                    print("Operation canceled, nothing todo.\noptions \"convert_datatype\" are activated but options_arg[\"convert_datatype\"] is empty and options_arg[\"convert_datatype\"] is required for this options")
                    break

            if "filter_num" in options and not self.nthinputted:
                if str_input.isalpha():
                    print("Cannot filter all numeric number, No Numeric numbers are detected")
                    break
                str_input = "".join(filter(str.isdigit, str_input))
            
            if "to_upper" in options and not self.nthinputted:
                str_input = str_input.upper()

            if "to_lower" in options and not self.nthinputted:
                str_input = str_input.lower()

            # Mode Section not options
            if "yesno_prompt" in options:
                if str_input.lower() == "y":
                    return True
                else:
                    return False

            # Mode section
            if "redirect_output" in options and not self.nthinputted:
                print("Flag 8 : Redirecting output to file\n")
                p = self.input("Name of File: ", None, 2)
                if p == "" or p == None or p.isspace():
                    raise Exception("File cannot be writen : INVALID_FILENAME")
                    break
                pd = self.input("Path (ex. Users/McFrozie/WorkDir): ", None, 2)
                if pd == "" or pd == None or pd.isspace():
                    raise Exception("File cannot be writen : INVALID_PATH_NAME")
                    break
                if not os.path.isdir(pd):
                    raise Exception("File cannot be written : INVALID_PATH_NOTDIR")
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

            if "filter_alpha" in options and not self.nthinputted:
                if str_input.isnumeric():
                    print("Cannot remove numeric char, all char are numerics!")
                    break
                else:
                    tmp = self.filterByNum(str_input)
                    str_input = "".join(tmp)
            if "validate_email" in options and not self.nthinputted: return validate_email(str_input)
            if "validate_phonenumber" in options and not self.nthinputted:
                try:
                    if str_input.isnumeric(): return phonenumbers.is_valid_number(phonenumbers.parse(str_input, None))
                except Exception as e:
                    print(e)
                    break
            if "validate_url" in options and not self.nthinputted: return check_url.check(str_input, test=True)
            return str_input
            break
    @staticmethod
    def testUnitProcedure():
        return True

# TEST

def test():
    return modern.testUnitProcedure()


