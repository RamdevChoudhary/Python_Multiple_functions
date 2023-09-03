def is_prime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i = 5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

def odd_even(num):
    if num%2==0:
        print("It's even Number")
    else:
        print("It's odd Number")

def armstrong(num):
    sum = 0
    order = len(str(num))
    copy_n = num
    while(num>0):
        digit = num%10
        sum+= digit ** order
        num = num//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong numebr")
        return True
    else:
        print(f"{copy_n} is not an armstrong number")
        return False