for i in range(100000):
    num=i
    result=0
    n=len(str(i)) #convert n into string to find number of digits
    while(i!=0):
        digit=i%10 # to find last digit ex:- (123) the last digit is 3
        result=result+digit**n
        i=i//10 # eliminate the last digit from n for ex:- 123 after eliminate 12
    if num==result:
        print(num)