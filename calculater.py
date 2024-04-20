# i am writting a program to make calculator
# + is used to Addition
# - is used to Subtraction
# * is used to Multiplication
# / is used to division
# % is used to Modulo
#  ** is used to Exponentiation
# // is used to Floor division
num1=int(input("Enter number 1:-"))# take input from user
num2=int(input("Enter number2:-"))
oper=input("Enter any operation:-")
if oper=="+":
  print(num1+num2)
elif oper=="-":
  print(num1-num2)
elif oper=="*":
  print(num1*num2)
elif oper=="/":
  if num2!=0:
    print(num1/num2)
  else:
    print("Error division by zero")
elif oper=="//":
  print(num1//num2)
elif oper=="**":
  print(num1**num2)
elif oper=="%":
  print(num1%num2)

