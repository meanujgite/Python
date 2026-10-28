# IF Statements
a=10
if a > 10:
    print("a is greater than 10")

# IF ELSE Statements
a=10
if a > 10:
    print("a is greater than 10")
else:
    print("a is less than 10")

money = int(input("Please provide me the money:-"))

if money == 10:
    print("I will buy ice cream")

else:
    print("I will Buy Ice Cream Cone")

# ELIF Statements

money = int(input("Please Provide me money :- "))
if money == 10:
    print("I have a ChocoBar")
elif money == 20:
    print("I have a Mango Dolly")
else:
    print("I have a ice cream cone")


# Q1. Accept Two Numbers and Print gretest Between Them
A = int(input("Enter Number:- "))
B = int(input("Enter Number:- "))

if A > B:
    print(A,"is greater than",B)
else:
    print(B,"is greater than",A)

# Q2. Accept the Gender From The User as Char and Print the respective greeting message(Ex- Good Morning Sir(on the Basis of Gender)) 
Gender = input("Please Enter Your Gender as Charecter(M or F) :- ")
if Gender == 'M':
    print("Good Morning Sir")
elif Gender == 'F':
    print("Good Morning Madam")
else:
    print("Gender is Invalid")

# Q3. Accept an integer and check whether it is an even number or odd

num = int(input("Please Enter Your Number :- "))
if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not. Ex. "Hello Anuj you are a valid voter"

Name =input("Please Enter Your Name :- ")
Age =int(input("Please Enter Age :- "))
if Age<=18:
    print("Hello",Name,"you are valid voter")
else:
    print("Hello",Name,"you are not valid voter")
#OR
Name =input("Please Enter Your Name :- ")
Age =int(input("Please Enter Age :- "))
if Age>=18:
    print(f"Hello {Name} you are valid voter")
else:
    print(f"Hello {Name} you are not valid voter")

# Q5.Accept a year and check if it is a leap year or not 
year = int(input("Tell your year :-"))
if year %100 == 0 and year %400 == 0:
    print("Its a leap year")
elif year %100 !=0 and year %4 ==0:
    print("Its a leap year")
else:
     print("Its a normal year")
     
# IF ELIF Ladder
t = int(input("Please tell the temperature :- "))
if t < 0:
    print("Freezing Cold")
elif t >= 0 and t < 10:
    print("Very Cold")
elif t >= 10 and t < 20:
    print("Cold")
elif t >= 20 and t < 30:
    print("Pleasant")
elif t >= 30 and t < 40:
    print("Hot")
else:
    print("Very Hot")