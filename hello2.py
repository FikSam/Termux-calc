
print("= Termux Calculator =")

var1 = input("var1: ")
var2 = input("var2: ")
operation = input("+, - :")
if operation == "+":
  var1 += var2
  print(var1)
else:
  var1 -= var2
  print(var1)