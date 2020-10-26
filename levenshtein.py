import numpy as np
def createarray(str1,str2):
    mat = np.zeros((len(str1)+1,len(str2)+1))
    for x in range(len(str1)):
        mat[x+1][0]=x+1
    for y in range(len(str2)):
        mat[0][y+1]=y+1
    return mat
def levdist(str1, str2, mat):
    for h in range(len(str1)):
        curval1 = str1[h:h+1]
        for j in range(len(str2)):
            diag = mat[h][j]
            left = mat[h+1][j]
            above = mat[h][j+1]
            curval2 = str2[j:j+1]
            if curval1 == curval2:
                mat[h+1][j+1]=diag
            else:
                min1 = min(diag,above,left)
                mat[h+1][j+1]=min1+1
    levd = mat[len(str1)][len(str2)]
    return levd
print("This program will use levenshtein distance to determine which string (either string two or three) is most similar to string one.")
str1 = input("Enter string one here: ")
str2 = input("Enter string two here: ")
str3 = input("Enter string three here: ")
mat1 = createarray(str1,str2)
mat2 = createarray(str1,str3)
lev1 = levdist(str1,str2,mat1)
lev2 = levdist(str1,str3,mat2)
lst3 = [str2,lev1]
lst2 = [str3,lev2]
ng = min(lev1,lev2)
if ng in lst3:
    print("String 1 is more similar to String 2 than String 3. \n The levenshtein distance is "+str(ng))
elif ng in lst2:
    print("String 1 is more similar to String 3 than String 3.\n The levenshtein distance is "+str(ng))