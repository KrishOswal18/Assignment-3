num = int(input("Enter a number: "))

def factorial(num):
    if num == 0 and 1:
        return 1
    else:
        result = num * factorial(num-1)
        return result

ans = factorial(num)

print(f"Factorial of {num} is: {ans}")


