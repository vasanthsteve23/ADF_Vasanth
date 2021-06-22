try:
    def gcd(x,y):
        if x<y:
          smaller=x
        else:
          smaller=y

        for i in range(1,smaller+1):
            if x%i==0 and y%i==0:
                hcf=i
        return hcf

    a=int(input())
    b=int(input())
    a=abs(a)
    b=abs(b)
    c=gcd(a,b)
    print("The GCD is : ",c)
except:
    print("Exception occurs")