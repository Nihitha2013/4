valid=False
while not valid:
    try:
        n=int(input("Enter the number:"))
        while n%2==0:
            print("Bye")
            valid=True
    except:
        print("Invalid number")
    finally:
        print("This is typed by Nihitha")