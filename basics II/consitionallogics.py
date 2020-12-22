# consitional logics

is_old = True
is_licenced = True

if is_old:
  print("You can drive")
elif is_licenced:
  print("You have a licence")
else:
  print("Go in prison")

if is_old and is_licenced:
  print("You can drive")
else:
  print("Go in prison")

# tenary operators

can_drive = "allowed" if is_old else "live the cart"

print(can_drive)