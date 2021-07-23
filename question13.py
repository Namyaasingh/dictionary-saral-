# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 
# s=[]
# s1=[]
# for i in my_dict.values():
#     s.append(i)
# for j in my_dict.keys():
#     s1.append(j)
# var1=0
# var2=0
# n=0
# l=len(s)
# s2=[]
# while n<l:
#     n1=0
#     while n1<l:
#         if s[n1]>s[n]:
#             if s1[n1] not in s2:
#                 s2.append(s1[n1])
#         n1+=1
#     break
#     n+=1
# print(s2)


#second_method of _

my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list1=[]
list2=[]
for i in my_dict.values():
    list1.append(i)
for f in my_dict.keys():
    list2.append(f)
max1=0
max2=0
max3=0
j=0
while j<len(list1):
    if list1[j]>max1:
        max2=max1
        max1=list1[j]
    if max1>list1[j]and max2<list1[j]:
        max2=max3
        max2=list1[j]
        if max3<max2 and max3<max1:
            max3=max2
            max3=list1[j]
    j+=1                                       
print(max1,max2,max3)
print(list2)
print(list1)
for_key=[]
index=0
while index<len(list1):
    if max1==list1[index] or max2==list1[index] or max3==list1[index]:
        for_key.append(list2[index])
    index=index+1
print(for_key)