from validate_email import validate_email
import phonenumbers



class PySimpleInput:
    def __init__(self):
        pass
    
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

    def input(self, label="Please enter a input.", f=[]):
        print(label)
        warnings = []
        while True:
            try:
                inp = input(":")
                related_f = {}
                if len(inp) == 0 or inp.isspace():
                    continue

                if "upcase" in f: inp.upper()
                if "lowcase" in f: inp.lower()
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
                if "filternum" in f and not type(inp) == list:
                    if inp.isalpha():
                        warnings.append("[E] NO NUMBER DETECTED")
                        pass
                    else:
                        inp = "".join(filter(str.isdigit, inp))
                if "filteralph" in f and not type(inp) == list:
                    if inp.isnumeric():
                        warnings.append("[E] NO ALPH DETECTED")
                        pass
                    else:
                        tmp = self.filterByNum(inp)
                        inp = "".join(tmp)
                if "valemail" in f and not type(inp) == list: return validate_email(inp)
                if "valphnum" in f and not type(inp) == list:
                    try:
                        if inp.isnumeric(): return phonenumbers.is_valid_number(phonenumbers.parse(inp, None))
                    except Exception as e:
                        warnings.append("[E] "+str(e))
                        pass

                return inp
                
            except KeyboardInterrupt:
                continue


