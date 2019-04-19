import time 
def errorMessage():
    for i in range(3):
        print() 
    
    print("Please answer correctly to the question !")
    print("Try again !")

    for i in range(3):
        print() 

def timeWaiter():
    for i in range(3):
        print() 

    print("Loading .. ")
    time.sleep(2)

    for i in range(3):
        print() 

def endQuest():
    for i in range(3):
        print() 

    end = input("Press any key to close the programm -- > ")

print("Welcome at Python !")
print("Today we will learn sets !")
print("Remember that in sets, elements CANNOT repeat !")
print()
#Asking the user what does he want to enter in his set
userSet = set([])
while True:
    question = input("Do you want to add something to your set ? -- > ")

    if question == "yes" or question == "Yes":
        element = input("Print here the element that you want to add to your set -- > ")
        try:
            element = eval(element)
            user.add(element)
        except:
            userSet.add(element)
    elif question == "no" or question == "No":
        break 
    else:
        errorMessage()
        continue 

timeWaiter()

print("Here we have used the \"add()\" function to add something to the set. -- > userSet.add(element)")
print("Your set is now -- > {0}".format(userSet))

for i in range(3):
    print()

#Asking the user if he wants to delete something from his set
while True:
    question = input("Do you want to delete something from your set ? -- > ")

    if question == "yes" or question == "Yes":
        element = input("Print here the element that you want to delete from your set -- > ")
        try:
            element = eval(element)
        except:
            pass 
        
        if element not in userSet:
            errorMessage()
            continue 
        else:
            userSet.discard(element) 
    elif question == "no" or question == "No":
        break 
    else:
        errorMessage()
        continue 

timeWaiter()
print("Here we have used the \"discard()\" function to discard/delete something from your set -- > userSet.discard(element)")
print("Your set is now -- > {0}".format(userSet))

for i in range(3):
    print() 

#Asking the user if he wants to copy the set 
while True:
    question = input("Do you want to copy this set ? -- > ")

    if question == "yes" or question == "Yes":
        userCopySet = userSet.copy()
        break
    elif question == "no" or question == "No":
        break
    else:
        errorMessage()
        continue 

timeWaiter()
print("Here we have used the \"copy\" function to copy a set -- > userCopySet = userSet.copy()")
print("This is the copied set -- > {0}".format(userCopySet))

for i in range(3):
    print() 

#Asking the user if he wants to clear the set 
while True:
    question = input("Do you want to clear your set ? -- > ")

    if question == "Yes" or question == "yes":
        userSet.clear()
        break 
    else:
        break 
    
print("Here we have used the \"clear\" function to clear the set -- > userSet.clear()")
print("This is your set now -- > {0}".format(userSet))
endQuest()
