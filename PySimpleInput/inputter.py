import sys
import os


class modern:
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
                print("Cannot submit empty string/userinput")
                continue

            if "convert_datatype" in options:
                try:
                    if not options_arg["convert_datatype"] == "" or not options_arg["convert_datatype"].isspace() or not options_arg == None:
                        if "str" == options_arg["convert_datatype"]:
                            return str_input
                        elif "int" == options_arg["convert_datatype"]:
                            if not str_input.isnumeric():
                                raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters\n\nSolution:\n\tActivate options \"filter_num\"")
                            return int(str_input)
                        elif "float" == options_ar["convert_datatype"]:
                            if not str_input.isnumeric():
                                    raise Exception("Cannot convert string to int,the string/user input contains Alphabet Characters not Numeric Characters")
                            return float(int(str_input))
                except (KeyError, IndexError):
                    print("Operation canceled, nothing to do.\noptions \"convert_datatype\" are activated but options_arg[\"convert_datatype\"] is empty and options_arg[\"convrrt_datatype\"] is required for this options")
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

            if "filter_alpha" in options and not self.nthinputted:
                if str_input.isnumeric():
                    print("Cannot remove numeric char, all char are numerics!")
                    break
                else:
                    tmp = self.filterByNum(str_input)
                    str_input = "".join(tmp)
            return str_input
            break
    @staticmethod
    def testUnitProcedure():
        return True

# TEST

def test():
    return modern.testUnitProcedure()


