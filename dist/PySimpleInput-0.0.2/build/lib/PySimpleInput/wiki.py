import os


wikistr = """
A Simple Python Library | v0.0.1
----------------------------------
This library help you to fix problems with Python Input Built-in Function
This library still on development progress. 
    if you found a bugs, report it to me with Github Issues at https://github.com/turtleion/PySimpleInput/issues

PySimpleInput Class - Method:
    (Initiated PySimpleInput class).input(arg1,arg2,arg...)
    Like Python, you can give a question to the user throught this function

    Method input() Argument:
        arg1 (STRING) This argument will send a question to the user (REQUIRED)
        arg2 (STRING) This argument will convert the user input datatypes (OPTIONAL)(NEED FLAG 3 ACTIVATED)
        arg3 (INTEGER/UNLIMITED) This argument will activate a flags
            List of flags that can be activated:
                1 -> Remove all whitespace in the user input
                2 -> Ignore user pressing enter key while user input string are empty
                3 -> Allow you to convert the datatype of user input (From String to Intor Float)
                    Flag 3 code:
                        "str" -> will convert user input to str
                        ++ THIS METHOD BELOW NEED A NUMERIC ONLY USER INPUT,NO ALPHABET CHARACTERS ALLOWED ++
                        "int" -> will convert user input to int
                        "float" -> will convert user input to float
                4 -> Remove all alphabet char from user input
                5 -> Convert user input from lower -> upper
                6 -> Convert user input from upper -> lower
"""

def wiki():
    with open(os.path.expanduser("~")+"/.PySimpleInput.wiki","w") as m:
        m.write(wikistr)
        m.close()
    os.system("vi -M ~/.PySimpleInput.wiki")

def old_long_wiki():
        print("A Simple Python Library | v1.0PROTO\nThis library may help you with general input problem like user doesn't input anything it will break your program\nThis library is on development/prototype, Buggy\n\nMethod:\n\tinput()\n\t\tJust like python you need to give a question to shown to the user\n\t\tAll the arguments that required\n\n\t\t- input(strg, ...) | STRG <- This argument is REQUIRED\n\t\t\t(STRING) With this string, you can give a question to the user\n\n\t\t- input(strg,returnDatatypes,...)| RETURNDATATYPES <- This argument is optional\n\t\t\t(STRING) This argument will convert the datatypes of user input (ex. you want to get age from user but the datatype of user input are string, Simple. Just call int() function and all are done ||| But I can make it simple again, You can convert it without calling the int() function with only entering \"int\" in the returnDatatypes argument and this method is same like int() even you can do \"float\"\n\t\t\t(NOTE) THIS METHOD ARE REQUIRED FLAG 3 ACTIVATED!\n\n\t\tinput(strg,returnDatatypes,*FLAGS) | FLAGS <- This argument are optional except you want to use argument-method returnDatatypes (Flag 3)\n\t\t\t(INTEGER) This argument will activate the flag you wntered in the argument (ex. Flag 3 that needed for argument-method returnDatatypes). This arguments have 3 flags:\n\t\t\t\t- 1 : Remove All Whitespace = This flag will remove all whitespace in the user input | CANCELED if user input doesn't have amy whitespace again\n\t\t\t\t2 : Ignore User Press Enter While Input is Still Empty = This flag will ignoring user pressing enter while input is still empty\n\t\t\t\t3 : Selected Data Types = This flag is allow you to convert user input from string to other data types")


