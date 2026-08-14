

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=input("choose(+, -, *, /,):")

if     operation == "+" :
        print("Answer:", num1 + num2)
elif operation == "-" :
        print("Answer:", num1 - num2)
elif operation == "*" :
        print("Answer:", num1 * num2)
elif operation == "/" :
        if num2 == 0:   
            print("you cannot divide by zero!")
        else: 	
            print("Answer:", num1 / num2)
else::	
        print("The operation is invalid")  
        
                  
        print("Thanks for using Adebola's Calculator")