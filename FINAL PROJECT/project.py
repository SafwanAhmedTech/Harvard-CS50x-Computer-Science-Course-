import random

class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, level, xp):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.xp = xp

    def show_stats(self):
        print(f"{self.name}")
        print(f"Current HP: {self.current_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")

    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)

    def is_fainted(self):
        return self.current_hp <= 0

    def __str__(self):
        return self.name

#starters
bulbasaur = Pokemon("Bulbasaur", 21, 12, 11, 10, 5, 0)
charmander = Pokemon("Charmander", 20, 11, 10, 13, 5, 0)
squirtle = Pokemon("Squirtle", 20, 11, 13, 10, 5, 0)

# Early route
pidgey = Pokemon("Pidgey", 15, 9, 8, 12, 3, 0)
rattata = Pokemon("Rattata", 14, 11, 8, 13, 3, 0)
caterpie = Pokemon("Caterpie", 12, 7, 9, 7, 2, 0)
weedle = Pokemon("Weedle", 12, 8, 8, 9, 2, 0)

# Popular Pokémon
pikachu = Pokemon("Pikachu", 18, 13, 10, 15, 5, 0)
eevee = Pokemon("Eevee", 19, 12, 11, 12, 5, 0)

# Cave Pokémon
zubat = Pokemon("Zubat", 16, 10, 9, 14, 4, 0)
geodude = Pokemon("Geodude", 22, 13, 15, 6, 5, 0)
onix = Pokemon("Onix", 23, 11, 16, 9, 5, 0)

# Special attackers
abra = Pokemon("Abra", 15, 16, 7, 14, 5, 0)
gastly = Pokemon("Gastly", 17, 15, 9, 13, 5, 0)

# Fighters
machop = Pokemon("Machop", 21, 14, 11, 9, 5, 0)

# Others
dratini = Pokemon("Dratini", 20, 13, 11, 11, 5, 0)
magikarp = Pokemon("Magikarp", 18, 8, 9, 10, 5, 0)
sandshrew = Pokemon("Sandshrew", 20, 12, 13, 10, 5, 0)
vulpix = Pokemon("Vulpix", 19, 11, 10, 12, 5, 0)

all_pokemon = [bulbasaur, charmander, squirtle,
    pidgey, rattata, caterpie, weedle,
    pikachu, eevee,
    zubat, geodude, onix,
    abra, gastly,
    machop,
    dratini, magikarp, sandshrew, vulpix]

trainer = input("Enter trainer name: ")
print(f"Hello {trainer}")

print("Choose your starter: Bulbasaur, Charmander, Squirtle")
starter = input("Enter name of pokemon here: ")

player_pokemon = []

for pokemon in all_pokemon:
    if pokemon.name.lower() == starter.lower():
        player_pokemon.append(pokemon)
        all_pokemon.remove(pokemon)
        break

user_money = 400
gym_badges = 0
seen = 0
caught = 0

inventory = {
    "Pokeball": 3,
    "Ultra Ball": 0,
    "Master Ball": 0,
    "Potion": 1,
    "Super Potion": 0
}

def level_up(pokemon):
    if pokemon.xp >= 100:
        pokemon.level += 1
        pokemon.xp -= 100
        pokemon.max_hp += 2
        pokemon.attack += 1
        pokemon.defense += 1
        pokemon.current_hp = pokemon.max_hp
        print(f"{pokemon.name} levelled up to to level {pokemon.level}")

def shop():
    global user_money
    print("Welcome to the Poke-shop!")
    print(f"Current Balance: {user_money}")
    print("Items: ")
    print("Pokeball = $200")
    print('Ultra Ball = $400')
    print('Master Ball = $650')
    print('Potion = $300')
    print('Super Potion = $600')
    item = input("Enter item: ")
    quantity = int(input('Enter quantity: '))
    price = 0
    if item == 'Pokeball':
        price = 200 * quantity
        if user_money >= price:
            inventory['Pokeball'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Ultra Ball':
        price = 400 * quantity
        if user_money >= price:
            inventory['Ultra Ball'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Master Ball':
        price = 650 * quantity
        if user_money >= price:
            inventory['Master Ball'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Potion':
        price = 300 * quantity
        if user_money >= price:
            inventory['Potion'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Super Potion':
        price = 600 * quantity
        if user_money >= price:
            inventory['Super Potion'] += quantity
        else:
            print('You do not have enough money')
            return
    print(f"Price: {price}")
    user_money -= price
    print(f"New balance: {user_money}")
    print('Thank you for your purchase, we hope to see you soon')

def catch(health, name):
    global user_money
    global caught
    number = random.randint(1, 10)
    if health > 55:
        if number > 3:
            player_pokemon.append(name)
            all_pokemon.remove(name)
            print(f"You have succesfully caught: {name}")
            caught += 1
            user_money += 750
            print(f"You got 750 cash")
            name.show_stats()
            return True
    elif health > 25:
        if number > 2:
            player_pokemon.append(name)
            all_pokemon.remove(name)
            print(f"You have succesfully caught: {name}")
            caught += 1
            user_money += 750
            print(f"You got 750 cash")
            name.show_stats()
            return True
    elif health > 0:
        if number > 1:
            player_pokemon.append(name)
            all_pokemon.remove(name)
            print(f"You have succesfully caught: {name}")
            caught += 1
            user_money += 750
            print(f"You got 750 cash")
            name.show_stats()
            return True

    print(f"{name} broke free!")
    return False

def switch_pokemon(current_pokemon):
    n = 0
    for pokemon in player_pokemon:
        print(f"{n}. {pokemon.name}: {pokemon.current_hp}/{pokemon.max_hp}HP")
        n += 1
    choice = int(input("Enter index number of pokemon you want to switch to: "))

    if 0 <= choice < len(player_pokemon):
        new_pokemon = player_pokemon[choice]

        if new_pokemon.is_fainted():
            print("That Pokémon has fainted!")
            return current_pokemon

        print(f"You switched to {new_pokemon.name}!")
        return new_pokemon

    else:
        print("Invalid choice.")
        return current_pokemon



def battle(user_pokemon, wild):
    global user_money
    global seen
    seen += 1
    user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
    wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)
    option = 0
    while user_pokemon.current_hp > 0 and wild.current_hp > 0 and option != 4:
        print("\nChoose an option: ")
        print("1. Attack")
        print("2. Catch")
        print("3. Heal")
        print("4. Run")
        print("5. Switch Pokemon")
        option = int(input("Enter option number: "))

        if option == 1:
            if user_pokemon.speed >= wild.speed:
                wild.take_damage(user_damage)
                print(f"{user_pokemon.name} did {user_damage} damage to {wild.name}")
                print(f"{wild.name} has {wild.current_hp} health")
                if wild.current_hp <= 0:
                    print(f"{wild.name} fainted")
                    exp = random.randint(30, 50)
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
                    user_money += 750
                    print(f"You got 750 cash")
                    level_up(user_pokemon)
                    return 2

                user_pokemon.take_damage(wild_damage)
                print(f"{wild.name} did {wild_damage} damage to {user_pokemon.name}")
                print(f"{user_pokemon.name} has {user_pokemon.current_hp} health")
                if user_pokemon.current_hp <= 0:
                    print(f"{user_pokemon.name} fainted")
                    user_money += 250
                    print(f"You got 250 cash")
                    return 1
            else:
                user_pokemon.take_damage(wild_damage)
                print(f"{wild.name} did {wild_damage} damage to {user_pokemon.name}")
                print(f"{user_pokemon.name} has {user_pokemon.current_hp} health")
                if user_pokemon.current_hp <= 0:
                    print(f"{user_pokemon.name} fainted")
                    user_money += 250
                    print(f"You got 250 cash")
                    return 1

                wild.take_damage(user_damage)
                print(f"{user_pokemon.name} did {user_damage} damage to {wild.name}")
                print(f"{wild.name} has {wild.current_hp} health")
                if wild.current_hp <= 0:
                    print(f"{wild.name} fainted")
                    exp = random.randint(30, 50)
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
                    user_money += 750
                    print(f"You got 750 cash")
                    level_up(user_pokemon)
                    return 2


        elif option == 2:
                print("Inventory: ")
                print(inventory)
                item = input("Enter item: ")
                number = random.randint(1, 10)
                health_percent = wild.current_hp / wild.max_hp * 100
                if item == 'Pokeball':
                    if inventory["Pokeball"] > 0:
                        inventory["Pokeball"] -= 1
                        if number > 3:
                            if catch(health_percent, wild):
                                return
                    else:
                        print("You don't have any!")

                elif item == 'Ultra Ball':
                    if inventory["Ultra Ball"] > 0:
                        inventory["Ultra Ball"] -= 1
                        if number > 2:
                            if catch(health_percent, wild):
                                return
                    else:
                        print("You don't have any!")

                elif item == 'Master Ball':
                    if inventory["Master Ball"] > 0:
                        inventory["Master Ball"] -= 1
                        if catch(health_percent, wild):
                            return

                    else:
                        print("You don't have any!")

        elif option == 3:
            print("Inventory: ")
            print(inventory)
            item = input("Enter item: ")
            if item == 'Potion':
                if inventory['Potion'] > 0:
                    inventory['Potion'] -= 1
                    user_pokemon.current_hp = min(user_pokemon.max_hp, user_pokemon.current_hp + 20)
                else:
                    print("You don't have any")
            elif item == 'Super Potion':
                if inventory['Super Potion'] > 0:
                    inventory['Super Potion'] -= 1
                    user_pokemon.current_hp = min(user_pokemon.max_hp, user_pokemon.current_hp + 50)
                else:
                    print("You don't have any")

        elif option == 4:
            print("You got away safely")

        elif option == 5:
            user_pokemon = switch_pokemon(user_pokemon)
            user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
            wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)

def gym_battle(user_pokemon, wild):
    global user_money
    global seen
    seen += 1
    user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
    wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)
    option = 0
    while user_pokemon.current_hp > 0 and wild.current_hp > 0 and option != 4:
        user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
        wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)
        print("\nChoose an option: ")
        print("1. Attack")
        print("2. Switch Pokemon")
        print("3. Heal")
        print("4. Run")
        option = int(input("Enter option number: "))

        if option == 1:
            if user_pokemon.speed >= wild.speed:
                wild.take_damage(user_damage)
                print(f"{user_pokemon.name} did {user_damage} damage to {wild.name}")
                print(f"{wild.name} has {wild.current_hp} health")
                if wild.current_hp <= 0:
                    print(f"{wild.name} fainted")
                    exp = random.randint(30, 50)
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
                    user_money += 750
                    print(f"You got 750 cash")
                    level_up(user_pokemon)
                    return 2

                user_pokemon.take_damage(wild_damage)
                print(f"{wild.name} did {wild_damage} damage to {user_pokemon.name}")
                print(f"{user_pokemon.name} has {user_pokemon.current_hp} health")
                if user_pokemon.current_hp <= 0:
                    print(f"{user_pokemon.name} fainted")
                    user_money += 250
                    print(f"You got 250 cash")
                    return 1
            else:
                user_pokemon.take_damage(wild_damage)
                print(f"{wild.name} did {wild_damage} damage to {user_pokemon.name}")
                print(f"{user_pokemon.name} has {user_pokemon.current_hp} health")
                if user_pokemon.current_hp <= 0:
                    print(f"{user_pokemon.name} fainted")
                    user_money += 250
                    print(f"You got 250 cash")
                    return 1

                wild.take_damage(user_damage)
                print(f"{user_pokemon.name} did {user_damage} damage to {wild.name}")
                print(f"{wild.name} has {wild.current_hp} health")
                if wild.current_hp <= 0:
                    print(f"{wild.name} fainted")
                    exp = random.randint(30, 50)
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
                    user_money += 750
                    print(f"You got 750 cash")
                    level_up(user_pokemon)
                    return 2

        elif option == 2:
            user_pokemon = switch_pokemon(user_pokemon)
            user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
            wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)

        elif option == 3:
            print("Inventory: ")
            print(inventory)
            item = input("Enter item: ")
            if item == 'Potion':
                if inventory['Potion'] > 0:
                    inventory['Potion'] -= 1
                    user_pokemon.current_hp = min(user_pokemon.max_hp, user_pokemon.current_hp + 20)
                else:
                    print("You don't have any")
            elif item == 'Super Potion':
                if inventory['Super Potion'] > 0:
                    inventory['Super Potion'] -= 1
                    user_pokemon.current_hp = min(user_pokemon.max_hp, user_pokemon.current_hp + 50)
                else:
                    print("You don't have any")

        elif option == 4:
            print("You got away safely")




def wild_encounter():
    number = random.randint(0, len(all_pokemon) - 1)
    wild = all_pokemon[number]
    wild.current_hp = wild.max_hp
    print(f"A wild {wild} has appeared!")
    print("Choose your pokemon to fight it!")
    for pokemon in player_pokemon:
        print(f"\n{pokemon.name}")
        print(f"{pokemon.current_hp}/{pokemon.max_hp} HP")
    name = input("Enter Pokémon name: ")

    for pokemon in player_pokemon:
        if pokemon.name.lower() == name.lower():
            user_pokemon = pokemon
            break
    else:
        print("You don't have that Pokémon.")
        return

    battle(user_pokemon, wild)

def heal_all(pokemons):
    for pokemon in pokemons:
        pokemon.current_hp = pokemon.max_hp
    print("All pokemon have been revived")

def gym():
    global gym_badge
    win_count = 0
    for n in range(3):
        number = random.randint(0, len(all_pokemon) - 1)
        enemy = all_pokemon[number]
        enemy.current_hp = enemy.max_hp

        print("Choose your pokemon to fight!")
        for pokemon in player_pokemon:
            print(f"\n{pokemon.name}")
            print(f"{pokemon.current_hp}/{pokemon.max_hp} HP")

        name = input("Enter Pokémon name: ")

        for pokemon in player_pokemon:
            if pokemon.name.lower() == name.lower():
                if pokemon.current_hp > 0:
                    user_pokemon = pokemon
                    break
                else:
                    print("Pick a pokemon with some hp remaining")
        else:
            print("You don't have that Pokémon.")
            return

        if gym_battle(user_pokemon, enemy) == 2:
            win_count += 1

    if win_count >= 3:
        print("You have passed the gym!")
        print("You recieved a gym badge")
        gym_badges += 1

    else:
        print("Unlucky, maybe next time you will win a gym badge")




n = 1

while True:
    print(f"\nRoute: {n}")
    print("Options:")
    print("1. Catch/battle pokemons in the wild")
    print("2. Go to Pokemon Centre to heal pokemon")
    print("3. Go to Poke-Shop")
    print("4. Carry on to next place (beware - a gym will always follow after a route)")
    print("5. View pokemon stats")
    print("6. achievements")
    option = int(input("Enter number of option: "))
    if option == 1:
        wild_encounter()
    elif option == 2:
        heal_all(player_pokemon)
    elif option == 3:
        shop()
    elif option == 4:
        gym()
        n += 1
    elif option == 5:
        print("Choose pokemon: ")

        for pokemon in player_pokemon:
            print(f"\n{pokemon.name}")

        name = input("Enter pokemon name: ")

        for pokemon in player_pokemon:
            if pokemon.name.lower() == name.lower():
                user_pokemon = pokemon
                break
        else:
            print("You don't have that Pokémon.")

        user_pokemon.show_stats()

    elif option == 6:
        print(f"Name: {trainer}")
        print(f"Gym badges: {gym_badges}")
        print(f"Pokemon seen: {seen}")
        print(f"Pokemon caught: {caught}")









