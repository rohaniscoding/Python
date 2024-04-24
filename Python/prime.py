def prime(num):
    if num==2:
        return True
    if num%2==0 or num<=1:
        return False
    for i in range(3,int(num*0.5)+1,2):
        if num%i==0:
            return False
    return True
def isprime(start,End):
    print("the Prime Number in the range",start,"and",End,'Are')
    for num in range(start,End+1):
        if prime(num):
            print(num)
start=int(input("Enter the Starting Range"))
End=int(input("Enter the Ending Range"))
isprime(start,End)
