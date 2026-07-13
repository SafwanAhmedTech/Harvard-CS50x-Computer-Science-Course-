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

#new pokemon added

# Grass
oddish = Pokemon("Oddish", 17, 10, 10, 8, 4, 0)
bellsprout = Pokemon("Bellsprout", 17, 11, 9, 9, 4, 0)
paras = Pokemon("Paras", 18, 11, 10, 8, 4, 0)

# Bug
metapod = Pokemon("Metapod", 18, 7, 14, 5, 3, 0)
kakuna = Pokemon("Kakuna", 17, 8, 13, 6, 3, 0)
butterfree = Pokemon("Butterfree", 21, 14, 11, 12, 6, 0)
beedrill = Pokemon("Beedrill", 22, 15, 10, 13, 6, 0)

# Flying
spearow = Pokemon("Spearow", 17, 12, 9, 14, 4, 0)
fearow = Pokemon("Fearow", 24, 17, 12, 17, 8, 0)

# Normal
meowth = Pokemon("Meowth", 18, 11, 9, 16, 5, 0)
snorlax = Pokemon("Snorlax", 40, 18, 18, 6, 12, 0)
tauros = Pokemon("Tauros", 26, 17, 13, 16, 8, 0)

psyduck = Pokemon("Psyduck", 19, 12, 11, 11, 5, 0)
goldeen = Pokemon("Goldeen", 18, 11, 10, 12, 5, 0)
poliwag = Pokemon("Poliwag", 18, 11, 10, 14, 5, 0)
tentacool = Pokemon("Tentacool", 20, 12, 12, 13, 5, 0)
lapras = Pokemon("Lapras", 32, 17, 16, 10, 10, 0)

magnemite = Pokemon("Magnemite", 20, 13, 14, 10, 6, 0)
voltorb = Pokemon("Voltorb", 18, 12, 10, 18, 5, 0)
electabuzz = Pokemon("Electabuzz", 28, 18, 14, 18, 10, 0)

growlithe = Pokemon("Growlithe", 22, 15, 12, 14, 7, 0)
ponyta = Pokemon("Ponyta", 21, 15, 11, 17, 7, 0)
arcanine = Pokemon("Arcanine", 34, 22, 18, 20, 15, 0)

diglett = Pokemon("Diglett", 17, 13, 8, 18, 5, 0)
graveler = Pokemon("Graveler", 30, 18, 20, 7, 10, 0)
rhyhorn = Pokemon("Rhyhorn", 31, 19, 19, 8, 10, 0)

dragonair = Pokemon("Dragonair", 30, 19, 16, 17, 12, 0)
dragonite = Pokemon("Dragonite", 42, 26, 22, 20, 20, 0)

scyther = Pokemon("Scyther", 29, 20, 15, 21, 12, 0)
kangaskhan = Pokemon("Kangaskhan", 34, 20, 18, 15, 12, 0)
chansey = Pokemon("Chansey", 45, 10, 12, 9, 10, 0)

dialga = Pokemon("Dialga", 85, 44, 40, 32, 55, 0)
palkia = Pokemon("Palkia", 84, 45, 38, 34, 55, 0)
giratina = Pokemon("Giratina", 90, 46, 42, 30, 60, 0)

arceus = Pokemon("Arceus", 110, 55, 55, 45, 100, 0)

# Grass
exeggcute = Pokemon("Exeggcute", 22, 13, 13, 8, 6, 0)
exeggutor = Pokemon("Exeggutor", 40, 25, 20, 10, 15, 0)
tangela = Pokemon("Tangela", 30, 18, 22, 12, 10, 0)

# Fire
flareon = Pokemon("Flareon", 38, 30, 18, 18, 15, 0)
magmar = Pokemon("Magmar", 35, 25, 18, 22, 14, 0)
ninetales = Pokemon("Ninetales", 36, 24, 21, 24, 15, 0)

# Water
staryu = Pokemon("Staryu", 24, 16, 15, 20, 7, 0)
starmie = Pokemon("Starmie", 40, 27, 22, 30, 16, 0)
slowpoke = Pokemon("Slowpoke", 35, 15, 20, 8, 8, 0)
slowbro = Pokemon("Slowbro", 48, 24, 28, 10, 16, 0)

# Electric
electrode = Pokemon("Electrode", 30, 18, 15, 35, 12, 0)
jolteon = Pokemon("Jolteon", 36, 25, 18, 34, 15, 0)

# Fighting
hitmonlee = Pokemon("Hitmonlee", 38, 30, 18, 24, 15, 0)
hitmonchan = Pokemon("Hitmonchan", 40, 27, 22, 20, 15, 0)

# Poison
grimer = Pokemon("Grimer", 26, 17, 15, 10, 6, 0)
muk = Pokemon("Muk", 44, 28, 24, 12, 15, 0)

# Ground
cubone = Pokemon("Cubone", 24, 16, 16, 12, 6, 0)
marowak = Pokemon("Marowak", 40, 28, 24, 18, 15, 0)

# Flying
farfetchd = Pokemon("Farfetch'd", 30, 20, 16, 18, 10, 0)
doduo = Pokemon("Doduo", 24, 18, 12, 20, 6, 0)
dodrio = Pokemon("Dodrio", 42, 30, 20, 30, 16, 0)

# Ice
jynx = Pokemon("Jynx", 34, 24, 16, 24, 14, 0)
dewgong = Pokemon("Dewgong", 42, 24, 24, 18, 15, 0)

# Rock
omanyte = Pokemon("Omanyte", 24, 16, 20, 12, 6, 0)
omastar = Pokemon("Omastar", 42, 28, 30, 16, 15, 0)

# Dragon
bagon = Pokemon("Bagon", 26, 18, 14, 14, 6, 0)
shelgon = Pokemon("Shelgon", 40, 24, 28, 12, 12, 0)
salamence = Pokemon("Salamence", 60, 38, 30, 32, 22, 0)

# Steel
skarmory = Pokemon("Skarmory", 42, 24, 32, 22, 15, 0)
steelix = Pokemon("Steelix", 55, 28, 40, 12, 20, 0)

# Starter Evolutions

# Bulbasaur line
ivysaur = Pokemon("Ivysaur", 30, 18, 17, 14, 16, 0)
venusaur = Pokemon("Venusaur", 48, 30, 28, 20, 36, 0)

# Charmander line
charmeleon = Pokemon("Charmeleon", 29, 19, 16, 18, 16, 0)
charizard = Pokemon("Charizard", 50, 34, 25, 30, 36, 0)

# Squirtle line
wartortle = Pokemon("Wartortle", 32, 17, 22, 15, 16, 0)
blastoise = Pokemon("Blastoise", 52, 28, 34, 20, 36, 0)

all_pokemon = [bulbasaur, charmander, squirtle,
    pidgey, rattata, caterpie, weedle,
    pikachu, eevee,
    zubat, geodude, onix,
    abra, gastly,
    machop,
    dratini, magikarp, sandshrew, vulpix]

all_pokemon.extend([
    oddish, bellsprout, paras, metapod, kakuna, butterfree, beedrill,
    spearow, fearow, meowth, snorlax, tauros,
    psyduck, goldeen, poliwag, tentacool, lapras,
    magnemite, voltorb, electabuzz,
    growlithe, ponyta, arcanine,
    diglett, graveler, rhyhorn,
    dragonair, dragonite,
    scyther, kangaskhan, chansey,
    dialga, palkia, giratina,
    arceus
])

all_pokemon.extend([
    exeggcute, exeggutor, tangela,
    flareon, magmar, ninetales,
    staryu, starmie, slowpoke, slowbro,
    electrode, jolteon,
    hitmonlee, hitmonchan,
    grimer, muk,
    cubone, marowak,
    farfetchd, doduo, dodrio,
    jynx, dewgong,
    omanyte, omastar,
    bagon, shelgon, salamence,
    skarmory, steelix
])

all_pokemon.extend([
    ivysaur, venusaur,
    charmeleon, charizard,
    wartortle, blastoise
])

print('Welcome to Pokemon Adventure!')

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
    while pokemon.xp >= 100:
        pokemon.level += 1
        pokemon.xp -= 100
        pokemon.max_hp += 2
        pokemon.attack += 1
        pokemon.defense += 1
        pokemon.current_hp = pokemon.max_hp

        print(f"{pokemon.name} levelled up to level {pokemon.level}!")

def shop():
    line()
    global user_money
    print("Welcome to the Poke-shop!")
    print(f"Current Balance: {user_money}")
    print("Items: ")
    print("Pokeball = $200")
    print('Ultra Ball = $700')
    print('Master Ball = $1500')
    print('Potion = $500')
    print('Super Potion = $1000')
    item = input("Enter item: ").lower().title().strip()
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
        price = 700 * quantity
        if user_money >= price:
            inventory['Ultra Ball'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Master Ball':
        price = 1500 * quantity
        if user_money >= price:
            inventory['Master Ball'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Potion':
        price = 500 * quantity
        if user_money >= price:
            inventory['Potion'] += quantity
        else:
            print('You do not have enough money')
            return
    elif item == 'Super Potion':
        price = 1000 * quantity
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
    line()
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
    line()
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
        line()
        print("Choose an option: ")
        print("1. Attack")
        print("2. Catch")
        print("3. Heal")
        print("4. Run")
        print("5. Switch Pokemon")
        print()
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
                    exp = 10
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
                    user_money += 250
                    print(f"You got 250 cash")
                    return 1
            else:
                user_pokemon.take_damage(wild_damage)
                print(f"{wild.name} did {wild_damage} damage to {user_pokemon.name}")
                print(f"{user_pokemon.name} has {user_pokemon.current_hp} health")
                if user_pokemon.current_hp <= 0:
                    print(f"{user_pokemon.name} fainted")
                    exp = 10
                    user_pokemon.xp += exp
                    print(f"{user_pokemon.name} got {exp} xp")
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
                item = input("Enter item: ").lower().title()
                number = random.randint(1, 10)
                health_percent = wild.current_hp / wild.max_hp * 100
                if item == 'Pokeball':
                    if inventory["Pokeball"] > 0:
                        inventory["Pokeball"] -= 1
                        if number > 3:
                            if catch(health_percent, wild):
                                return
                        else:
                            print(f'{wild.name} broke free!')
                    else:
                        print("You don't have any!")

                elif item == 'Ultra Ball':
                    if inventory["Ultra Ball"] > 0:
                        inventory["Ultra Ball"] -= 1
                        if number > 2:
                            if catch(health_percent, wild):
                                return
                        else:
                            print(f'{wild.name} broke free!')
                    else:
                        print("You don't have any!")

                elif item == 'Master Ball':
                    if inventory["Master Ball"] > 0:
                        inventory["Master Ball"] -= 1
                        if catch(health_percent, wild):
                            return

                    else:
                        print("You don't have any!")
                else:
                    print("You don't have that item!")

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
    line()
    global user_money
    global seen
    seen += 1
    user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
    wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)
    option = 0
    print('Gym rules: ')
    print('1. 1 pokemon per battle')
    print('2. You will play 3 battles')
    print('3. To get a gym badge you must win all three battles.')
    print('4. You will verse a random unknown pokemon at each battle')
    print('5. Once your pokemon dies, you will automatically lose the battle and you cannot switch a pokemon back in to continue that battle')
    print()
    print('The gym battles begin!')
    while user_pokemon.current_hp > 0 and wild.current_hp > 0 and option != 4:
        user_damage = max(1, user_pokemon.attack - wild.defense * 0.5)
        wild_damage = max(1, wild.attack - user_pokemon.defense * 0.5)
        print("\nChoose an option: ")
        print("1. Attack")
        print("2. Switch Pokemon")
        print("3. Heal")
        print("4. Run")
        print()
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
    line()
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
    line()
    global gym_badges
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

def line():
    print()
    print('-----------------------------------------------------------------------------------------------------------------------------------------------')
    print()

while True:
    line()
    print(f"Route: {n}")
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









