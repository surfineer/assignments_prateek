import calendar

# define function

def daycount (x,m,y):
    cal = calendar.monthcalendar(y,m)
    counter=0
    for e in cal:
        if e[x] != 0:
            counter += 1
    return counter

# Header

while True: 
    print("""Which day of the Year would you like to count? 
    Enter as per below""")
    print("0: Monday")
    print("1: Tuesday")
    print("2: Wednesday")
    print("3: Thursday")
    print("4: Friday")
    print("5: Saturday")
    print("6: Sunday")
    print("press 'exit' to quit")
    
# User Input

        #try:
            
    x=input("> ")

    if x == "exit": 
        break

    x=int
    y=int(input("For which year?\n"))
    print("Enter 1=January, 2=February, and so on\n")
    m=int(input("In which month?\n"))

    # Output

    result=daycount(x,m,y)
    print(f"There are {result} {x} in {m} of {y}")     # need translation!!

        #except Exception as e:
            #print("not a valid input!")  

print ("You exited the programm")