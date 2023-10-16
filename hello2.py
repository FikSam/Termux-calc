
print("= Termux Calculator =")

var1 = float(input("var1: "))
var2 = float(input("var2: ")) 
operation = input("Enter + or -: ") 

if operation == "+":
  result = var1 + var2
  print("Var1: ", result)
elif operation == "-":
  result = var1 - var2
  print("Var2: ", result)
else:
  print("Invalid operation")
