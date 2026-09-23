print("==========welcome=============")
print("==========menu detail===========")
print("1:add(+)")
print("2:suubtract(-)")
print("3:multiply(*)")
print("4:dividion(/)")
print("5:modulus(%)")
print("6:exit")
while True:
    choice=int(input("enter the choice:"))
    num1=int(input("enter the number:"))
    num2=int(input("enter the 2nd number:"))
    if(choice==1):
        sum=num1+num2
        print=("sum is:",sum)
    elif(choice==2):
        sub=num1-num2
        print("subtract is:",sub)
    elif(choice==3):
        multi=num1*num2
        print("multiply is:",multi)
    elif(choice==4):
        divid=num1/num2
        print("dividion is:",divid)
    elif(choice==5):
        modul=num1%num2
        print("reminder is:",modul)
    elif(choice==6):
        "exit"
        break
    else:
        print("invalid choice")
