Numb1 = float((input ("Enter the first number")))
operator = input ("Enter an operator (+, -, * , /)") 
Numb2 = float ((input ("Enter the second number")))

if operator == "+" :
    results = Numb1 + Numb2
    print (round(results, 3))
elif operator == "-":
    results = Numb1 - Numb2
    print (round(results, 3))
elif operator == "*" :
    results = Numb1 * Numb2
    print (round(results, 3))
elif operator == "/":
    results = Numb1 / Numb2
    print (round(results, 3))
else :
    print (f"{operator} is not a valid operator ")



