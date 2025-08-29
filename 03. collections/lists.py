'''Lists Example'''

#iterating through lists
a = [12,13,14,15,16,17,34.5,-45,-87]
for i in range(len(a)):
    print(a[i])
    
# Direct Iterations
for i in a:
    print(i)
    
# Positive negative elements
print("Positve elements: ")
for i in a:
    if i >=0: 
        print(i)
print("Negative elements:")
for i in a:
    if i<=0:
        print(i)


#Average of list
l = [12, 435, 67, 89, 23, 25, 69]
print("Average: ",sum(l)/len(l))


#Largest element from the list
l = [12, 567, 43, 235, 347, 568, 45, 7]
largest = l[0]
for i in range(1,len(l)):
    if l[i]>largest:
        largest = l[i]
print(largest)


#second largest from the list
l = [12, 567, 43, 235, 347, 568, 45, 7]
largest = l[0]
second_largest = l[0]
for i in l:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(largest,second_largest)


#check if list is sorted
a = [12,13,18,15,16]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        print("List is not sorted")
        break
else:
    print("List is Sorted")