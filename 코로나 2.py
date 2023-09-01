list=[[2000, 3050, 2050, 1980],[7500, 2050, 2050, 1980],[15450, 15050, 15550,14900]]
list3=[]
for i in list:
    list2 = []
    
    for v in i:
        list2.append(v*0.014)

     list3.append(list2)
print(list3)


