from validate_email import validate_email
import phonenumbers
from colorama import Fore, Style
import translators as ts
import getpass
sr = Style.RESET_ALL



class PySimpleInput:
    def __init__(self):
        self.warnings =[]
        self.showWarn = False
    def filterAlpha(self,x):
        chars = []
        for char in x:
            try:
                if char.isalpha(): chars.append(char)
                elif char.isspace(): chars.append(" ")
            except:
                pass

        return chars
    def show_error(self, t=False):
        if t:
            self.showWarn = False
        else:
            print("["+Fore.CYAN+"!"+sr+"]"+" ERROR WILL BE SHOWN.")
            self.showWarn =True

    def __process(self, inp, f):
        related_f = {}
        tr_res = ""
        warnings = []
        for i in f:
            if "min_" in i:
                _ = i.split("_")[-1]

                if _.isnumeric():
                    if not len(inp) >= int(_):
                        print("[" + Fore.RED + "E" + sr + "] Not enough answer, required: "+str(_)+" Detected/Given: "+str(len(inp)))
                        return False
                else:
                    pass
            if "max_" in i:
                _ = i.split("_")[-1]

                if _.isnumeric():
                    if not len(inp) < int(_):
                        print("[" + Fore.RED + "E" + sr + "] Too much answer, required: "+str(_)+" Detected/Given: "+str(len(inp)))
                        return False
                else:
                    pass
        if "upcase" in f: inp = inp.upper()
        if "lowcase" in f: inp = inp.lower()
        if "translate" in f:
            length = len(f)
            pos = f.index("translate")
            print(pos)
            if type(pos) is None:
                pass
            else:
                if not pos == 0 and not pos == (length - 2):
                    print("[" + Fore.RED + "E" + sr + "] Please write translate option at the end.")
                    pass
                else:
                    if length == 0:
                        pass
                    else:
                        if "tr_" in f[-1]:
                            lang = f[-1].split("_")[-1]
                            try:
                                res = ts.translate_text(inp, translator="google", to_language=lang)
                                print(res)
                                tr_res = res

                            except ts.server.TranslatorError as e:
                                if "Unsupported to_language" in str(e):
                                    print("[" + Fore.RED + "E" + sr + "] Unknown target language: " + lang)

                        else:
                            print("[" + Fore.RED + "E" + sr + "] Please provide a target language.")
        if "rmwhtspc_str" in f:
            if not related_f["rmwhtspc"] == False:
                pass
            else:
                if " " in inp: inp = "".join(inp.split(" "))
                related_f["rmwhtspc"] = True
        if "rmwhtspc_arr" in f:
            if not related_f["rmwhtspc"] == False:
                pass
            else:
                if " " in inp: inp = inp.split(" ")
                related_f["rmwhtspc"] = True
                isarr = True
        if "filternum" in f and not type(inp) == list:
            if inp.isalpha():
                warnings.append("[" + Fore.RED + "E" + sr + "]" + Fore.YELLOW + " NO NUMBER HAS FOUNDED." + sr)
                pass
            else:
                inp = "".join(filter(str.isdigit, inp))
        if "filteralph" in f and not type(inp) == list:
            if inp.isnumeric():
                warnings.append("[" + Fore.RED + "E" + sr + "]" + Fore.YELLOW + " NO ALPH HAS FOUNDED." + sr)

                pass
            else:
                tmp = self.filterAlpha(inp)
                inp = "".join(tmp)
        if "valemail" in f and not type(inp) == list: return validate_email(inp)
        if "valphnum" in f and not type(inp) == list:
            try:
                if inp.isnumeric(): return phonenumbers.is_valid_number(phonenumbers.parse(inp, None))
            except Exception as e:
                warnings.append("[E] " + str(e))
                pass


        if self.showWarn:
            enc = 0
            for warn in warnings:
                enc += 1
                print("[" + str(enc) + "] " + warn)
        if len(tr_res) == 0:
            return inp
        elif not len(tr_res) == 0:
            return tr_res

    def process_(self, text, f):
        proc = self.__process(text, f)
        return proc
    def input(self, label="Please enter an input.", f=[]):
        print(label)
        while True:
            try:
                inp = ""
                if "passwd_input" in f:
                    inp = getpass.getpass("PW: ")
                else:
                    inp = input("> ")

                if len(inp) == 0 or inp.isspace():
                    continue

                prec = self.__process(inp, f)
                if type(prec) == bool and prec==False: continue
                return prec

            except KeyboardInterrupt:
                continue


