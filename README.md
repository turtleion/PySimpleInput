# PySimpleInput | v0.0.6
<img src="https://i.ibb.co/DzJgLRW/image.png" width="250" height="230">

Hi! Let me introduce *PySimpleInput*

This library is still on development progress.
    if you've found a bugs, report it to me at [PySimpleInput Github Issues](https://github.com/turtleion/PySimpleInput/issues) 
    
# Installation
You can install PySimpleInput with pip or using .whl
### Using PIP
`pip3 install --upgrade PySimpleInput`
### Using wheel
- First, you need to get the wheel file from PyPi or Github
- And then you can install it
`pip3 install (PySimpleInput Wheel File).whl`

# Docs
*if you want the latest update, choose the devel branch, if you want stable update then choose main branch*

## How to Initialize PySimpleInput module
```
import PySimpleInput

pysim = PySimpleInput.PySimpleInput()
```


### Method 
- input()  
  - label: Give a question to the user
  - options: set additional settings to the input

- process_()
  > process_ might like input but its only used for processing text
  - text: Text to proceed
  - options: set additional settings to the process_
#### ARGUMENTS
  - input
    - LABEL (REQUIRED) : This argument will ask questions to the user
    - OPTIONS (OPTIONAL) : this argument provides additional settings to the input 
                       `ex. filtering user input to return only numbers`
  - process_
    - TEXT (REQUIRED)
    - OPTIONS (OPTIONAL)

### OPTIONS
> Note: argument "options" in method input() and process_() are same
this section contain all options that available in PySimpleInput

- rmwhtspc_* :
    
    this option will remove all white space in user input string
    - rmwhtspc_arr
        > Note: If you're using this option, you might cannot use some of the options
        
        It'll return array/list instead of str
        > ex. `o = pysimpleinput.input("What's your name?", ["rmwhtspc_arr"])

        > Result. `"Joseph Arauro" > "["Joseph", "Arauro"]"`

    - rmwhtspc_str 
    
        It'll return str
        > ex. `o = pysimpleinput.input("What is your name?", ["rmwhtspc_str"])`

        > Result. `"Joseph Arauro" -> "JosephArauro"`


- filter_num 
    
    this option will filter user input to return only numbers

    >   ex. `pysimOut = pysimpleinput.input("How old are you?", ["filternum"])`

    >   Result. --> `"oejnzo299kwjo02" -> "29902"`

- filteralph 
 
    This option will filter user input to return alphabet characters only

    >   ex. `pysimOut = pysimpleinput.input("Type random string!", ["filteralph"])`

    >   Result. --> `"hello219282839my282872name283739191is8287399turtleion" -> "hellomynameisturtleion"`

- passwd_input
    > Note: If you use this option, please make sure you have access to `/dev/tty.` (Unix User)

    This option will make the input hidden

    `(NO EXAMPLE)`

- upcase and lowcase

    This option will change the user input letters to uppercase or vice versa

    >   ex. `pysimOut = pysimpleinput.input("What is your name?", options=["upcase/lowcase"])`

    >   Result. --> `"gerardo martinuez firatzi" <(OR)> "GERARDO MARTINUEZ FIRATZI"`

- min_`[NUMBER]` and max_`[NUMBER]`

  Now, you can set min/max length for the input
  
  > ex. `res = pysimpleinput.input("What's your name?", options["min_8", "max_20"])`

  >> User Inputted: Fred

  >> The prompt will ask you again if you didn't pass the requirements
     - It'll show Warnings
       - Too much answer.
       - Not enough answer.
- translate and tr_`[COUNTRY ISOCODE]`

    >  Note: Please use "translate" option at the end of "options" list argument
    
    This option will translate the input to another language
    You must add "tr_[COUNTRY ISOCODE]" after the translate option
    >  Supported Language [COUNTRY ISOCODE](https://pypi.org/project/translators/#supported-languages)
    
    like this:
    - `tr_en` > translate_english
    - `tr_de` > translate_deutsch or translate_germany
    - `tr_fr` > translate_french
    Example: (Translating from Indonesia to English)
    >  ex. `tr = pysimpleinput.input("Apa makanan favorit mu?", options["translate", "tr_en"])`
    
    >> User inputted: "Aku suka Nasi Goreng"

    > Result. --> `I like fried rice.`
- (DEPRECATED) valemail

    This option will validate an email from the user

    > ex. `pysimOut = pysimpleinput.input("Type an email!",["valemail"])

    > Result. --> `True | False (If the string is an email it will return True otherwise False)`

- (DEPRECATED) validate_phonenumber

    This option will validate an phone number from the user

    > ex. `pysimOut = pysimpleinput.input("Type your phone numbers!", ["valphnum])

    > Result. --> `PhoneNumber | Warning (If the string is a valid number it will return the number back otherwise a warning`


### And Also, You can combine options like this
`pysim = pysimpleinput.input("What is your name?", ["rmwhtspc_str","filteralph")`

### Do not combine "valemail, valphnum" options!
### and also if you are using "rmwhtspc_arr" option.. you might cannot use "valemail, valphnum, filteralph, filternum" options!
--------------

# Contribution
I'm Appreciate you for contributing on this modules
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
--------

--> Changelog | 0.0.5
- Changed the contents of README.md
- Less features to make it lightweighter and simplier
  - Removed features
    - Filter URL
    - Redirect output to a file
    - Prevent User KEY_ENTER press
- Renamed features
- Removed some files

--> Changelog | 0.0.5-REV2
- Update README.md

--> Changelog | 0.0.6
- Update README.md
- Add new method:
  - process_()
- Add new options:
  - translate and tr_`[COUNTRY ISOCODE]`
  - min_`[NUM]` and max_`[NUM]`
  - passwd_input


# About
This project was made 100% by Me (Turtleion) 
This project was licensed by MIT License
Visit my GitHub
https://github.com/turtleion


*Sorry for bad English, I'am Indonesian btw :).*
