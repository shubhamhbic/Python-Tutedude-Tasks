def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

x = int(input("Enter a Number: "))
print("Factorial of",x , "is:",factorial(x))
