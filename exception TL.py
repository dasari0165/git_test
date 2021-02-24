# Examples on nested try and except,except with else,finally
no1=int(input("Enter first value:"))
no2=int(input("Enter second value:"))
try:
    print("the sum:",no1+no2)
    print("the multi:",no1/no2)
    print("the multi:", no1*no2)
    print("the multi:", no1-no2)
    try:
        print("the divison:",no1/no2)
        print("the sub:", no1 - no2)
    except ZeroDivisionError as Zde:
         print("can not devide by zero")
except ValueError as e:
     print("invalid input")
else:
     print("It is a else block")
finally:
    print("iam finally function")
print("thank you")



