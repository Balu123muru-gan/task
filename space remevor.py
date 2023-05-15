t="i    am      balu        from    karur"
#t=len(t)
#print(t)
#01234567890
for i in range(len(t)+1):
    if t[i]==' ' and t[i+1]=='  ':
        continue
    else:
        print(t[i],end=' ')
print(t[len(t)]-1)

