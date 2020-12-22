print("Lists")
print("-----")
fruits = ["apple", "banana", "cherry"]

for item in fruits:
  print(item)

print("\nSets")
print("-----")
fruits = ("apple", "banana", "cherry")
for item in fruits:
  print(item)

users = {
  "name":"Aime",
  "age": 5,
  "can_swim": True
}

print("return entiere set")
print("-------------------")
for item in users.items():
  print(item)

print("\nreturn values")
print("----------------")

for item in users.values():
  print(item)

print("\nreturn keys")
print("-------------")
for item in users.keys():
  print(item)

print("\nreurn key and values")
print("----------------------")
for k,v in users.items():
  print("key > "+k+", value > "+str(v))

