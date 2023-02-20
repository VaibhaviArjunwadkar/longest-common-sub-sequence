import random
import time

def alternateMerge(arr1, arr2, n1, n2, arr3, case):
    i = 0
    if case == "special":
        j = 1
    else:  
        j = 0
    k = 0
 
    # Traverse both array
    while (i < n1 and j < n2):
        arr3[k] = arr1[i]
        i += 1
        k += 1

        if arr2[j] == 0:
            arr3[k] = " "
        else:
            arr3[k] = arr2[j]  
        j += 1
        k += 1
 
    # Store remaining elements of first array
    while (i < n1):
        arr3[k] = arr1[i]
        i += 1
        k += 1
 
    # Store remaining elements of second array
    while (j < n2):
        arr3[k] = arr2[j]
        k += 1
        j += 1
    
    
# function for implementation of LCS 
def LCS_DP_CB(X,Y,m,n):
    L = [[0 for i in range(n+1)] for j in range(m+1)] # array b from the book
    R = [[0 for i in range(n+1)] for j in range(m+1)] # array c from the book

    # Following steps build L[m+1][n+1] in bottom up fashion. Note that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                R[i][j] = "\\"
            elif L[i-1][j] >= L[i][j-1]:
                L[i][j] = L[i-1][j]
                R[i][j] = "^"
            else:
                L[i][j] = L[i][j-1]
                R[i][j] = "<"  


    lcs = ""
 
    # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
 
        # If not same, then find the larger of two and go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
             
        else:
            j -= 1

    
    
    # code to print header part as follows:
    #------------- 
    #   1 2 3 4
    # Y B O A T
    #-------------

    print("- - - - - - - - - - - - - - - - - - - - - - - - - \n")        

    case = "normal"
    basearray1 = [" ", " ", " "," ", "|", " ", " "]
    basearray2 = [" ", " ", " ", " ", "|", " ", "Y"]

    arrayY = list(Y)
    arrayX = list(X)
    l3 = len(arrayY)
    array1 = []
    array2 = []

    for o in range(0, l3):
        array1.append(" ") # array1 = [" ", " ", " "," "]
    for p in range(0, l3):
        array2.append(p+1) # array2 = ["1", "2", "3", "4"]
    l1 = len(array1) # 4
    l2 = len(array2) # 4
    
    array3 = [0] * (l1 + l2)
    alternateMerge(array1, array2, l1, l2, array3, case)
    for i in range(0, (l1 + l2)):
        basearray1.append(array3[i]) # basearray1 = [" ", " ", "1", " ", "2", " ", "3", " ", "4"]
    for i in range(0, len(basearray1)):
        print(basearray1[i], end=" ") # space space 1 space 2 space 3 space 4
    print("\n")

    array4 = [0] * (l1 + l3)
    alternateMerge(array1, arrayY, l1, l3, array4, case)
    for i in range(0, (l1 + l3)):
        basearray2.append(array4[i]) # basearray2 = ["Y", " ", "B", " ", "O", " ", "A", " ", "T"]
    for i in range(0, len(basearray2)):
        print(basearray2[i], end=" ") # Y space B space O space A space T
    print("\n")

    print("- - - - - - - - - - - - - - - - - - - - - - - - - \n")        


    # code to print main matrix
    for t in range(len(L)):
        tempVariable = arrayX[t-1]
        if t == 0:
           columnBaseArray = [" ", " ", "X", " ", "|", " "]
        else:
            columnBaseArray = [t, " ", tempVariable, " ", "|", " "]
        case = "special"
        n1 = len(L[t])
        n2 = len(R[t])
        arr3 = [0] * ((n1 + n2)-1)
        alternateMerge(L[t], R[t], n1, n2, arr3, case)
       
        for r in range(0, ((n1 + n2)-1)):
            columnBaseArray.append(arr3[r])
        for s in range(0, len(columnBaseArray)):
            print(columnBaseArray[s], end=" ")
        print("\n")

    print("- - - - - - - - - - - - - - - - - - - - - - - - - \n")        


        
    # We traversed the table in reverse order LCS is the reverse of what we got
    lcs = lcs[::-1]
    print ("Length of Longest Common Subsequence is: ", len(lcs))
    print("The Longest Common Subsequence of " + f'"{X}"' + " and " + f'"{Y}"' + " is " + "'" + lcs + "'")


# function to read the n number of rows with X and Y strings
def read_textFile(inputTextfile):
    with open(inputTextfile, 'r') as f:
        readSingleRow = ([row.strip().split() for row in f])
    
    # loop for considering two strings x, y in a single row at a time for n number of rows.
    for n in range(len(readSingleRow)):
        abc = readSingleRow[n][0]
        chunks = abc.split(',')
        X = chunks[0]
        Y = chunks[1]
        print("\n")
        print("X = ",f'"{X}"' "        Y = ",f'"{Y}"',"\n")

        # calling main LCS logic function with parameters X and Y as two strings of respective row
        LCS_DP_CB(X, Y, len(X), len(Y))


# calling read_textFile function
read_textFile('LCS1.txt')