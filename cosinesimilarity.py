import numpy as np 
import math as mt
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
str3=input("Enter the third string: ")
n = max(len(str1),len(str2),len(str3))
def lettonum(strw,n):
  vect = np.zeros((1,n))
  for c in range(len(strw)):
    curlet = strw[c:c+1]
    b = ord(curlet)-96
    vect[0][c]=b
  return vect
def dotprod(vect1,vect2,n):
  d = 0
  for c in range(n):
    cur1 = vect1[0][c]
    cir2 = vect2[0][c]
    ds = cur1*cir2
    d+=ds
  return d
def mag(vect,n):
  h =0
  for s in range(n):
    cur = vect[0][s]
    cur = cur**2
    h+=cur
  h = mt.sqrt(h)
  return h
def cossim(mag1,mag2, dotprod):
  prodmag = mag1*mag2
  j = dotprod/prodmag
  return j
vecta = lettonum(str1,n)
vectb = lettonum(str2,n)
vectc = lettonum(str3,n)
dtpr = dotprod(vecta,vectb,n)
dtpr1 = dotprod(vecta,vectc,n)
mag1 = mag(vecta,n)
mag2 = mag(vectb,n)
mag3 = mag(vectc,n)
cossi = cossim(mag1,mag2,dtpr)
cossi1 = cossim(mag1,mag3,dtpr1)
lst1 = [cossi,str2]
lst2 = [cossi1,str3]
min1 = max(cossi,cossi1)
dist = 1-min1
if min1 in lst1:
    print("String 1 is more similar to string 2 than string 3 \n The Cossine similarity with string 2 was "+str(cossi)+"\n The cosine distance was "+str(dist))
elif min1 in lst2:
    print("String 1 is more similar to string 3 than string 2 \n The Cossine similarity with string 3 was "+str(cossi1)+"\n The cosine distance was "+str(dist))