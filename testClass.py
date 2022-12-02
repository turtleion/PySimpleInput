import PySimpleInput

psi = PySimpleInput.old()
p = psi.input("Input something here (Testing modern PySimpleInput) : ", None, 1)
print(p)

pc = PySimpleInput.modern()
pf = pc.input("Input something here (Testing old PySimpleInput) : ", options=["remove_whitespace"])
print(pf)
# THIS FILE ONLY FOR TESTING 
# YOU CAN TEST PySimpleInput BEFORE YOU TRY IT IN YOUR REAL PROJECT,
# OR YOU CAN TEST YOUR MODIFICATION OF PySimpleInput
# YOUR CODE SHOULD BE START HERE VVVV


