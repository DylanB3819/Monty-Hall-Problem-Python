import random

def main():
    doors = ["goat", "goat", "car"]
    wins = 0
    switch = input("Switch (y/n): ").strip().lower()

    for _ in range(500):
        choice = game(doors, switch)
        if doors[choice - 1] == "car":  # Check if final choice is the car
            wins += 1

    print(f"Wins: {wins} out of 500")

def game(doors, switch):
    shuffled_doors = doors[:]  # Create a copy to avoid modifying the original list
    random.shuffle(shuffled_doors)

    choice = random.randint(1, 3)  # Pick a random door (1, 2, or 3)
    
    # Find the doors with goats that are NOT the chosen door
    goats = [i+1 for i in range(3) if shuffled_doors[i] == "goat" and (i+1) != choice]
    revealed_goat = random.choice(goats)  # The host reveals one goat

    if switch == "y":
        # Choose the only remaining door
        final_choice = [i+1 for i in range(3) if (i+1 != choice and i+1 != revealed_goat)][0]
        return final_choice
    else:
        return choice  # Stick with original choice

main()
