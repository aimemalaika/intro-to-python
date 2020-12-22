is_magician = True
is_expert = False


if is_magician and is_expert:
  print("You are a magicien and an expert")

elif is_magician and not(is_expert):
  print("You are a magician but not an expert")

elif not(is_expert):
  print("You are an expert")