is_magician = True
is_expert = False


if is_magician and is_expert:
  print("You are a magicien and an expert")

elif is_magician and not(is_expert):
  print("You are a magician but not an expert")

elif not(is_expert):
  print("You are an expert")

# find highest

def highest_event(*args):
  i = 0
  temp = []
  while i < len(args[0]):
    if args[0][i] % 2 == 0:
      temp.append(args[0][i])
    i+=1
  def get_max(temp):
    highest = 0
    for number in temp:
      if number > highest:
        highest = number
    return highest

  return get_max(temp)

print(highest_event([10,2,1,4,6,3,8,11,66]))