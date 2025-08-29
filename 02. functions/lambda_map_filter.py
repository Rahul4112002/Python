'''Lambda Map Filter'''

#lambda function
square = lambda x:x*x
print("Square of 5 = ",square(5))


#Map with lambda
nums = [1,2,3,4,5]
doubles = list(map(lambda x:x*2, nums))
print(doubles)


#filter with lambda
nums = [1,2,3,4,5]
evens = list(filter(lambda x:x%2==0,nums))
print(evens)


#Reduce example
from functools import reduce
sum_all = reduce(lambda a,b:a+b,nums)
print(sum_all)