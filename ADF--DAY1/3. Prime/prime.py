import time
try:
    n=100
    i=2
    while True:
       a = False
       for j in range(2,(i//2)+1):
           if (i%j)==0:
              a=True
       if a==False:
           print(i)
           time.sleep(5)
       i=i+1
except:
    print("Exception occurs")