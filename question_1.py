dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i,j in dic1.items():
    for x,y in dic2.items():
        if i==x:
            dic4[i]=(j+y)
            print(dic4)
        dic4.update(dic1)
        dic4.update(dic2)
        dic4.update(dic3)


