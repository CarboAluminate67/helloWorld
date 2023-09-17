import time as t

# Initializes the hello world print into both a string and a list
helloString = 'Hello World!'  
helloList = list(helloString)

def backspace(): print(f'\b'*12, end="") # Quick function to return to beginning of the string

# Loops until program is ended
while True:
    i = 0

    while i < 12: # Writes Hello World! overtime
        print(f'{helloList[i]}', end="")
        t.sleep(.1)
        i += 1
    
    backspace()

    for j in range(12): # Deletes Hello World! overtime
        print(' ', end="")
        t.sleep(.1)

    backspace()


    
