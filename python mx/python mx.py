
def fact(n):
    if n==0 or n==1:
        return 1
    if n>1:
        return n*fact(n-1)
num=int(input("Entre the number:"))
print(fact(num))
