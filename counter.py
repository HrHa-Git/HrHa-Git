# Project 1

numbers=[1,2,3,4,5,6,7,8,9]
count_even=0
count_odd=0

for n in numbers:
  if n%2 == 0:
  count_even=count_even+1
else:
  count_odd=count_odd+1

print('There are', count_odd, 'odd numbers in this set.')
print('There are', count_even, 'even numbers in this set.')
