
print("= Termux Calculator =")

var1 = float(input("var1: "))
var2 = float(input("var2: ")) 
operation = input("Enter + or -: ") 

if operation == "+":
  result = var1 + var2
  print("Результат:", result)
elif operation == "-":
  result = var1 - var2
  print("Результат:", result)
else:
  print("Неподдерживаемая операция. Поддерживаются только + и -.")
