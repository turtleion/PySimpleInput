# PySimpleInput | v0.0.4

Hi! Let me introduce *PySimpleInput* Library.

This library help you to fix problems with Python Input Built-in Function.

This library still on development progress.
    if you found a bugs, report it to me at [PySimpleInput Github Issues](https://github.com/turtleion/PySimpleInput/issues) 
    
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


# Docs
*if you want the latest update, choose the devel branch, if you want stable then choose main branch, if you want to try the newest and earlier features choose testing branch*

First of all we need to know all class in PySimpleInput modules

- PySimpleInput -> PySimpleInput (PySimpleInput.PySimpleInput)
                    Modern PySimpleInput, got more updates, more bugs have been fixed than the previous version
## How to Initialize PySimpleInput modules in a new ways
```
import PySimpleInput

pysim = PySimpleInput.PySimpleInput()
```

*The difference between new PySimpleInput and old PySimpleInput is in the changelog*
### Method 
- input()  
  - label: Give a question to the user
  - options: set additional settings to the input
  - extra_options: extra arguments for the input options

#### ARGUMENTS on the input method
LABEL (REQUIRED) : This argument will ask questions to the user, without this argument the user will not be able to answer

OPTIONS (OPTIONAL) : this argument provides additional settings to the input 
                       `ex. filtering user input to return only numbers`

EXTRA_OPTIONS (OPTIONAL/SOMETIMES REQUIRED) : Either option requires additional arguments for it to work properly

### OPTIONS on the input method

this section contains all options available in PySimpleInput (Modern)

- remove_whitespace : this option will remove all white space in user input string

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["remove_whitespace"])`

    > Result. `"Joseph Madriguo Terafora" -> "JosephMadrigioTerafora"`

- prevent_enterkeypress : this option will prevent the user from pressing the enter key

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["prevent_enterkeypress"])`

- convert_datatype : this option will change the user input data type from string to ... (str, int, float)

    > ex. `pysimOut = pysimpleinput.input("How old are you?", options=["filter_num", "convert_datatype"], options_arg={"convert_datatype": "(int, float, str)"})`

    > Result. --> `"29 (STR)" -> 29 (Int)`

- filter_num : this option will filter user input to return only numbers

    > ex. `pysimOut = pysimpleinput.input("How old are you?", options=["filter_num"])`

    > Result. --> `"oejnzo299kwjo02" -> "29902"`

- to_upper and to_lower : This option will change the user input letters to uppercase or vice versa

    > ex. `pysimOut = pysimpleinput.input("What is your name?", options=["to_upper/to_lower"])`

    > Result. --> `"gerardo martinuez firatzi" <(OR)> "GERARDO MARTINUEZ FIRATZI"`

- yesno_prompt : This option will make the question yes or no (All OS is now supported) (EXPERIMENTAL)
    > NO EXAMPLES

- redirect_output : this option will write the output to a file (EXPERIMENTAL)
    > NO EXAMPLES

- filter_alpha : This option will filter user input to return alphabet characters only

    > ex. `pysimOut = pysimpleinput.input("Type random string!", options=["filter_alpha"])`

    > Result. --> `"hello219282839my282872name283739191is8287399turtleion" -> "hellomynameisturtleion"`

- validate_email : This option will validate an email from the user

    > ex. `pysimOut = pysimpleinput.input("Type an email!",options=["validate_email"]

    > Result. --> True | False (If the string is an email it will return True otherwise False

- validate_phonenumber : This option will validate an phone number from the user

    > ex. `pysimOut = pysimpleinput.input("Type your phone numbers!",options=["validate_phonenumber"]

    > Result. --> PhoneNumber | Warning (If the string is a valid number it will return the number back otherwise an warnimg

- validate_url : This option will validate an URL from the user

    > ex. `pysimOut = pysimpleinput.input("Show me Famous Artist in YouTube!", options=["validate_url"])

    > Result. --> True | False (If the string is a valid url, it will eeturn True otherwise False

### And Also, You can combine options
like this
`pysim = pysimpleinput.input("What is your name?", options=["remove_whitespace","prevent_enterkeypress")`

Do not combine "validate" options!

--------------

# Contribution
I Appreciate you for contributing on this modules
### How To Contribute
You can Contribute by forking this repo and start adding more features, optimizing code and fixing bugs
Then you can make a pull request to this repo and wait your pull request merged

You can also contribute by giving a star to this repo 👍
-----------


# Changelog
--> Changelog | 0.0.3
- Add Flags 7, 8
- Add Docs to README.md
- Remove wiki.py and PySimpleInput.wiki function (Moved to README.md)
- Fix README.md | version not changed
--------

--> Changelog | 0.0.3.1
- Fix README.md Indentation blocks
- Fixing Typo in README.md
--------

--> Changelog | 0.0.3.5
- Fix README.md
- Make the options simpler and easier to understand (You still can use old way)
- Separate Modern & Old ways
--------

--> Changelog | 0.0.4
- Changed the contents of README.md to make it easier to understand
- Added More Features:
    - "validate_email",
    - "validate_phonenumber"
    - "validate_url"
- Recombining modern & old PySimpleInput
- Create Makefile to simplify the development process

# You need to READ this
I'm not recommended you to download PySimpleInput below this version (0.0.3.1)

And I will focus to fixing bugs over adding features

# About
This project was made 100% by Me (Turtleion) 
This project was licensed by MIT License
Visit my GitHub
https://github.com/turtleion


*Sorry for bad English, I"am Indonesian. so it's normal for me*
