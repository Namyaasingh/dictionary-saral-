a=[{"first":"1"},{"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"6"},{"seven":"7"}]
b=[{"first":"1"},{"second": "2"}, {"third": "3"}, {"four": "4"}, {"five":"5"}, {"six":"6"},{"seven":"7"}]
i=0
d=[]
while i<len(a):
    if a[i]==b[i]:
        d.append(a[i])
    i=i+1
print(d)