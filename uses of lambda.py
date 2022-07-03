from functools import reduce

nums = [2,4,9,3,6,5,1]
evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda  n : n*2,evens))
sum = reduce(lambda a,b : a+b,doubles)
print(evens)
print(doubles)
print(sum)

print('edited on git hub repository')

print('edited on my local machine: varma prasad')

print('edited again in the cloud')

print('now i am editing in local machine with updated project')
