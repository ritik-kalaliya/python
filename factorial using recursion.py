print("Name: Ritik\nRoll No.: 25513\nBranch: ECS") 
def factorial(n):
 if n == 0: 
    return 1
 else:
  return n * factorial(n-1)
num = int(input("Enter a non-negative integer: ")) 
if num < 0:
 print("Factorial is not defined for negative integers.") 
else:
 fact = factorial(num)
print(f"The factorial of {num} is {fact}.")

