num = int(input("Enter a number:"))
sqrt = int(num**0.5)

for x in range(2,sqrt+1):
    if num%x==0:
        print(num," is not prime")                          
    else:
        print(num,"is prime")


        '''
        output:
        Enter a number:6
        6 is not prime

        '''