# PySimpleInput | v0.0.3.5 (The Tiny Pluto Update)

Hi! Let me introduce *PySimpleInput* Library.

This library help you to fix problems with Python Input Built-in Function.

This library still on development progress.
    if you found a bugs, report it to me with Github Issues at [PySimpeInput Github Issues](https://github.com/turtleion/PySimpleInput/issues) 
    
# Installation
You can install PySimpleInput with pip or using .whl or manually with .tar.gz
### Using PIP
`pip3 install --upgrade PySimpleInput`
### Using wheel
- First, you need to get the wheel file from PyPi or Github
- And, you can install it
`pip3 install (PySimpleInput Wheel File).whl`
### Using .tar.gz
- Same as using wheel, you need to get the .tar.gz file from PyPi or Github
- Extract the .tar.gz file using `tar -xvf (PySimpleInput TAR GZ File).tar.gz`
- Cd into PySimpleInput directory : `cd PySimpleInput-(VERSION)/`
- Then you can install it : `python3 setup.py install`


# Docs - Modern
First of all we need to know all class in PySimpleInput modules
MODULES            CLASS
- PySimpleInput -> modern (PySimpleInput.modern)
                    Modern PySimpleInput, got more updates, more bugs have been fixed than the previous version

- PySimpleInput -> old (PySimpleInput.old)
                    Old PySimpleInput, simpler and faster but more bugs than later versions


## How to Initialize PySimpleInput modules in a new ways
Old:

```
import PySimpleInput

pysim = PySimpleInput.PySimpleInput()
```

New:

```
import PySimpleInput
pyold = PySimpleInput.old() 
pynew = PySimpleInput.new()
```

*The difference between is in the changelog*


### Method 
- input()  
  - label: Give a question to the user
  - options: set additional settings to the input
  - extra_options: extra arguments for the input options

#### ARGUMENTS - INPUT()
LABEL (REQUIRED) : This argument will ask questions to the user, without this argument the user will not be able to answer

OPTIONS (OPTIONAL) : this argument provides additional settings to the input 
                       `ex. filtering user input to return only numbers`

EXTRA_OPTIONS (OPTIONAL/SOMETIMES REQUIRED) : Either option requires additional arguments for it to work properly

### OPTIONS - ARG/INPUT()

this section contains all options available in PySimpleInput (Modern)

- remove_whitespace : this option will remove all white space in user input string

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["remove_whitespace"])`

    > Result. `"Joseph Madriguo Terafora" -> "JosephMadrigioTerafora"`

- prevent_enterkeypress : this option will block the user from pressing the enter key

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["prevent_enterkeypress"])`

- convert_datatype : this option will change the user input data type from string to ... (str, int, float)

    > ex. `pysimOut = pysimpleinput.input("How old are you?", options=["filter_num", "convert_datatype"], options_arg={"convert_datatype": "(int, float, str)"})`

    > Result. --> `"29 (STR)" -> 29 (Int)`

- filter_num : this option will filter user input to return only numbers

    > ex. `pysimOut = pysimpleinput.input("How old are you?", options=["filter_num"])`

    > Result. --> `"oejnzo299kwjo02" -> "29902"`

- to_upper and to_lower : This argument will change the user input letters to uppercase or vice versa

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["to_upper/to_lower"])`

    > Result. --> `"gerardo martinuez firatzi" <(OR)> "GERARDO MARTINUEZ FIRATZI"`

- yesno_prompt : This argument will make the question yes or no (For now, only windows is supported) (EXPERIMENTAL)
    > NO EXAMPLE

- redirect_output : this argument will write the output to a file (EXPERIMENTAL)
    > NO EXAMPLE

- filter_alpha : This argument will filter user input to return alphabet characters only (NEW)

    > ex. `pysimOut = pysimpleinput.input("Type random string!", options=["filter_alpha"])`

    > Result. --> `"hello219282839my282872name283739191is8287399turtleion" -> "hellomynameisturtleion"`

### And Also, You can combine options
like this
`pysim = pysimpleinput.input("What is your name?", options=["remove_whitespace","prevent_enterkeypress")`


*Sorry for bad english, i'am indonesian so it's normal*

--------------
# Docs - Old
First of all, you need to initiate the PySimpleInput class to variable
`import PySimpleInput
 
 PySim = PySimpleInput.PySimpleInput()
`
# Know what is .input(...) Method
PySim.input(..)
Like Python, you can give a question to the user throught this function

input() Required/Optional Arguments:    arg1 (STRING)  This argument will send a question to the user (REQUIRED) 
- arg2 (STRING) This argument will convert the user input datatypes (OPTIONAL)(NEED FLAG 3 ACTIVATED)
- arg3 (INTEGER) This argument will activate a flags:
- List of flags (options/settings) that can be activated:
    -   1 -> Remove all whitespace in the user input
  
            ex. `Joe Gregor Van Dones` -> `JoeGregorVanDones`
    -   2 -> Prevent user pressing enter while the input field is empty

            This options will preventing user to corrupt your input
    -   3 -> Allow you to convert the datatype of user input (From String to Int or Float)

            This options will convert result datatypes (This options need argument num 2 filled with this `Flag 3 Code`
    -   4 -> Remove all alphabet charactets from user input
    -   5 -> Convert user input from lower -> upper
    -   6 -> Convert user input from upper -> lower
    -   7 -> Yes/No input (EXPERIMENTAL)
    -   8 -> Redirect user input to a file (EXPERIMENTAL)
    -   9 -> the opposite of flags 4 [COMING SOON]
    -   10 -> E-Mail input support [COMING SOON]
    
### All Flags 3 Code
- "str" -> convert user input to st

++ CAUTION ++
> This method need you to prevent the user entering alphabet characters that can be destroy PySimpleInput system / Use flags 4
- "int" ->  convert user input to int
- "float" ->  convert user input to float
You can also use multiple flags, like this

### Did you know, you can combine a flags
You can combine a flags like this
`userinp = PySim.input("What is your name?", None, 1, 2, 5)
the user inputted: Joe McCallison, because flag 1 and 5 activated, it will be like this: JOEMCCALLISON`

# Contribution
I Appreciate you for contributing on this modules
### How To Contribute
You can Contribute by forking this repo and start adding more features, optimizing code and fixing bugs
Then you can make a pull request to this repo and wait your pull request merged

You can also contribute by giving a star to this repo 👍
-----------


# Changelog
--> Changelog at version 0.0.3
- Add Flags 7, 8
- Add Docs to README.md
- Remove wiki.py and PySimpleInput.wiki function (Moved to README.md)
- Fix README.md | version not changed
--------

--> Changelog at version 0.0.3.1
- Fix README.md Indentation blocks
- Fixing Typo in README.md
--------

--> Changelog at version 0.0.3.5
- Fix README.md
- Make the options simpler and easier to understand (You still can use old way)
- Separate Modern & Old ways
--------

# You need to READ this
I'm not recommended you to download PySimpleInput below this version (0.0.3.1)

And I will focus to fixing bugs over adding features

# About
This project was made 100% by Me (Turtleion) 
This project was licensed by MIT License
Visit my GitHub
https://github.com/turtleion


*Sorry for bad English, I"am Indonesian. so it's normal for me*
