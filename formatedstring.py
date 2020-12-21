# formated string
name = "Aime"
age = 25
print("Hi "+name+" you are "+str(age)+" years old")

# print in formated string better way

print(f"Hi {name} you are {age} years old")

# print in formates string python 2
print("Hi {0} you are {1} years old".format(name,age))

# sings indexation

selfish = "01234567"

#rule [start:stop:stepover]
# use negative index to start at the end on the string
print(selfish[0:8:3])
print(selfish[::-2])