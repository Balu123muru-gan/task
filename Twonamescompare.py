##n=input()
##
##ed=len(n)-1
##for i in range(len(n)//2):
##    print(n[i],n[ed],end="",sep="")
##    ed=ed-1
##if len(n)%2==1:
##    print(n[len(n)//2])

#=============================================================
# Python program to check if two
# to get unique values from list
# using numpy.unique
import numpy as np

# function to get unique values

list1 = [10, 20, 10, 30, 40, 40]
#def unique(list1):
for i in range(len(list1)):
    x = np.array(list1)
/// print(np.unique(x))


# driver code
##list1 = [10, 20, 10, 30, 40, 40]
##print("the unique values from 1st list is")
##unique(list1)

##
##list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
##print("\nthe unique values from 2nd list is")
##unique(list2)

