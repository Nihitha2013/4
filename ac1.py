try:
    n=int(input("Enter the number:"))
    print(n)
except ValueError as e:
    print("Exeption is:",e)


print("Finally I am outside of above blocks")
print("Bye")