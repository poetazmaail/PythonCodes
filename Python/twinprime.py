def prime(n):
    f = 0
    sqrt = int(n**0.5)
    for i in range(2,sqrt+1):
        if n%i == 0:
            f = 1
            break
    return f
    

num1 = int(input("Enter starting number:"))
num2 = int(input("Enter ending number:"))
print("Twin prime numbers are:")
for i in range(num1,num2+1):
    if prime(i) == 0 and prime(i+2) == 0:
        print(i,"",i+2)

        '''
        output:
        Enter starting number:5
        Enter ending number:20
        Twin prime numbers are:
        5   7
        11  13
        17  19
        '''