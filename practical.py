print("Name: Aditya\nRoll No.: 25500") 
num = int(input("Enter a Number: "))
order = len(str(num)) 
sum = 0
temp = num
while temp > 0:
 digit = temp % 10 
 sum += digit ** order
 temp //= 10
if num == sum:
 print(num,"is an Armstrong Number.")
else:
 print(num,"is not an Armstrong Number.")