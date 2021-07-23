dict=  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
total = 0
for i in dict:
    value_list = dict[i]
    count = len(value_list)
    total += count
print(total)
