print("= Termux Calculator =")

var1 = float(input("var1: "))  
var2 = float(input("var2: "))  
operation = input("+, - :")

if operation == "+":
  result = var1 + var2
  print(result)
elif operation == "-":
  result = var1 - var2
  print(result)
else:
  print("Invalid operation. Please enter '+' or '-' for addition or subtraction.")