def divide(ourdividend,ourDivisor):
    sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1)
    ourdividend = abs(ourdividend)
    ourDivisor = abs(ourDivisor)
    quotientNumber = 0
    tempNumber = 0
    for i in range(31,-1,-1):
        if(tempNumber + (ourDivisor << i) <= ourdividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i
        if sign == -1:
            quotientNumber = -quotientNumber
            return quotientNumber
a = int(input("Enter a value for a/b:\n"))
b = int(input("Enter b value for a/b\n"))
print("Result of a/b without dividing is:\n", divide(a,b))