numbers = range(1, 101)
for number in numbers:
  if number%3 == 0 and number%5 == 0:
    print("CracklePop")    
  elif number%5 == 0:
    print("Pop")
  elif number%3 == 0:
    print("Crackle")
  else:
    print(number)