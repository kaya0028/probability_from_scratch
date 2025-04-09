import random 

number_doors =  3
door_with_prize = random.randint(1,3)

chosen_door = int(input(f'there are {number_doors} doors, pick one: \n'))
opened_door = random.choice([i for i in range(1,4) if i != chosen_door and i != door_with_prize])

switch = input("You chose door {0}, but door {1} was opened. \n Doy you want to switch y/n?\n".format(chosen_door, opened_door))

if switch == 'y':
    opened_door = random.choice(
        [i for i in range(1,4) if i != chosen_door and i != door_with_prize]
    )
    if chosen_door == door_with_prize:
        print("You win a prize!")
    else: 
        print("sorry no prize")
