import random

def main():
  doors = ["goat", "goat", "car"]
  wins = 0
  switch = input("Switch (y/n): ")
  if switch == "y":
    for i in range(10000):
      choice = game(doors,switch)
      if choice == doors.index("car"):
        wins += 1
  else:
    for i in range(10000):
      choice = game(doors,switch)
      if choice == doors.index("car"):
        wins += 1
  print(wins)

def game(doors,switch):
  random.shuffle(doors)
  choice = random.randint(0,2)
  goats = [i for i in range(3) if doors[i] == "goat" and i != choice]
  revealedGoat = random.choice(goats)
  if switch == "y":
    final = [i for i in range(3) if i != choice and i != revealedGoat][0]
  else:
    return choice
  return final
  
main()