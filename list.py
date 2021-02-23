squares = [1, 4, 9, 16, 25]


squares[0]  # indexing returns the item
squares[-3:]  # slicing returns a new list

squares[:]

squares + [36, 49, 64, 81, 100]  #concatenation


cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(len(letters))

#nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)