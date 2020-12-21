# dictionaries

dictionary = {
  "a" : 1,
  "b" : {
    "a" : 12,
    "b" : 32
  }
}


print(dictionary)

# dictionaries methods

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# get property
print(car.get("brand","MAZDA"))

# other way to create dictionary
car2 = dict(brand = "Ford",electric = False,year = 1964,colors = ["red", "white", "blue"])

print(car2)

car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print("brand" in car.keys())
print("Ford" in car.values())
print(car.items())
car2 = car.copy()
car.clear()
print(car)
print(car2)
print(car2.pop("colors"))
print(car2)
print(car2.update({"year":1995}))
print(car2)