operator=input("enter a operator (+,-,*,/):")
num1=int(input("enter a number:"))
num2=int(input("enter the second number:"))
ans=0
if operator=="+":
  ans=num1+num2
  print("the answer for that will be",round(ans))
elif operator=="-":
  ans=num1-num2
  print(ans)
elif operator=="*":
  ans=num1*num2
  print(ans)
elif operator=="/":
  ans=num1/num2
  print(ans)
else:
  print("fucking idiot wrong operator")