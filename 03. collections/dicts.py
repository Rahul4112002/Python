"""Dictionary Examples"""

# Dictionary CRUD
d = {10: 100, 20: 200, 30: 300, 40: 400}
d[10] = 150 #update
d[50] = 600 #add
del d[30] #delete
print("Dictionary: ",d)


# Dictionary items
print("Items:", d.items())


#Merge 2 Dictionary
d1 = {10: 100, 20: 200, 40: 300}
d2 = {40: 400, 50: 500, 60: 600}

for i in d2:
    d1[i] = d2[i]
print("Merged: ", d1)

#Sum of dictionary values
d1 = {10: 100, 20: 200, 40: 300}
print("Sum of values:", sum(d1.values()))

#Frequency count using dictionary
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for i in a:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print("Frequency: ", frequency)
        
# Merge with addition if key exists
d1 = {10: 100, 20: 200, 40: 300}
d2 = {40: 400, 50: 500, 60: 600}
for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print("Merged with addition:", d1)