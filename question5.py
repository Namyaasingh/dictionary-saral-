list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
a={}
for i in range(len(list1)):
    a[list2[i]]=list1[i]
print(a)
