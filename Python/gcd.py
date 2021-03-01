num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))

if num2>num1:
    x = num1
else:
    x = num2

for k in range(1,x+1):
    if num1%k==0 and num2%k==0:
        gcd = k

print("The GCD of this two numbers is ", end ="")
print(gcd)

'''
output:
Enter first number: 4
Enter second number: 2
The GCD of this two numbers is 2
'''