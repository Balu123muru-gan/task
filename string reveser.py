"""def reverse(string):
    reverse_string=" "
    for i in string:
        reverse_string=i+reverse_string
    print("reversed string:",reverse_string)
string=input("enter:")
print(string)
reverse(string)"""
   #-------------------------------------------------------
#1 slicing
#day="sunday"
#print(day[::-1])
#------------------------------------------------
#2.for loop method
"""n=input()
temp=' '
for char in n:   
    temp=char+temp  # t=b+' '=t, t=u+s=ab,t=l+ab=lab,t=u+lab=ulab
print(temp)"""
#------------------------------------------
#3.while loop
"""temp=" "
day='sunday'
length=len(day)-1 #6
while length>=0: # 6>=0
    temp=temp+day[length]  #t=' '+y=y,t=y+a=ya
    length=length-1 # 6-1=5
print(temp)"""
#-----------------------------------------------------------------------
# 4. using list Reverse()
"""day="sunday"
mylist=list(day)
mylist.reverse()
print("".join(mylist))"""
#----------------------------------------------------------
# 5.Recursion

def reverse_rec(str):
    if len(str)==0:
        return str
    else:
        return reverse_rec(str[1:])+str[0]
print(reverse_rec("sunday"))

#-----------------------------------------
#6.Reversed()
"""day="sunday"
reverse_str="".join(reversed(day))
print(reverse_str)"""
#=====================================
#

#============================
#========================================


