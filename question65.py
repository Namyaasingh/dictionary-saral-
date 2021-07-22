dic={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
total_length=0
for value in dic.values():
    length=len(value)
    total_length=total_length+length
print(total_length)
