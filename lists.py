# list are like array 
list = ["home","tools",23,True]

print(list)

print(list[3])


# list slicing

cars = ["Ford", "Volvo", "BMW"]

print(cars)

cars[2] = "Ferari"

print(cars[0:3])

print(cars)

# matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])

# lists methods

cars = ["Ford", "Volvo", "BMW"]

#get lenght
print(len(cars))

cars.append("Ferari")

print(cars)

# add at e index
cars.insert(3,"Hummer")

print(cars)

# to merge two array
cars.extend(["Lambourgini","Limosine"])

print(cars)

# remove the last element
cars.pop()

print(cars)

# remove the element at an idex
cars.pop(3)

print(cars)

# remove all the elements
cars.clear()

print(cars)

# find index of element

cars = ['Ford', 'Volvo', 'BMW', 'Hummer', 'Ferari', 'Lambourgini', 'Limosine']

print('Hummer' in cars)

print ("i" in "in my nama")

print(cars.count('BMW'))

# find index of element

cars = ['Ford', 'Volvo', 'BMW', 'Hummer', 'Ferari', 'Lambourgini', 'Limosine']
print(sorted(cars))
cars.sort()
print(cars)
cars.reverse()
print(cars)

#list unpacking
cars = ['Ford', 'Volvo', 'BMW', 'Hummer', 'Ferari', 'Lambourgini', 'Limosine']

a,b,c,d,e,f,g = cars

a,b,c,*others = cars

print(a)

print(others)