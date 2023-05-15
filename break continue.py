list_1=['x','y','z']
list_2=[11,22,33]
for i in list_1:
    for j in list_2:
        print(i,j)
        if i=='y' and j==33:
            print('BREAK')
            break
        else:
            continue
        break

    
#print(list_2)
