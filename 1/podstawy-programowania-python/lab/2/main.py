import sys
 
def stanlicznika(n):
  w = [0 for _ in range(n)]
  while (True):
   yield w
   for i in range(n+1):
    if (i==n):
     return None  # przewinięcie licznika
    if w[i]==0:
     w[i]=1
     break
    else: 
     w[i]=0 


def stanlicznikaodwrotnie(n):
  w = [1 for _ in range(n)]
  while (True):
   yield w
   for i in range(n-1, -1, -1):
    if (w == [0 for _ in range(n)]):
     return None  # przewinięcie licznika
    if w[i]==1:
     w[i]=0 
     break
    else: 
     w[i]=1

if __name__ == "__main__":
   n = int(sys.argv[1]) if (len(sys.argv)>1) else 5
   for w in stanlicznika(n):
     print(w)
   print("=====================")

   for w in stanlicznikaodwrotnie(n):
     print(w)
     print(sum(w))
