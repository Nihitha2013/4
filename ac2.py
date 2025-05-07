try:
    n1=int(input("Enter the number1:"))
    n2=int(input("Enter the number2:"))
    r=n1/n2
    print("result=",r)
    print("result=",r1)
except ZeroDivisionError :
    print("Division by zero not allowed")
except NameError as e:
    print("NameError:",e)
except ValueError:
    print("Enter integer only")
except:
    print("some other error")

print("Goodbye")