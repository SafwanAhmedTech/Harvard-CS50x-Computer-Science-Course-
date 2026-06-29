Pokémon Adventure (Python)

Video Demo: (https://youtu.be/iQ98YQGAFpA)

Description:

Pokémon Adventure is a text-based Pokémon game written entirely in Python. The goal of the project was to recreate the core mechanics of the Pokémon games while keeping the gameplay simple enough to be played in the terminal. Throughout the game, the player explores different routes, encounters wild Pokémon, catches new team members, battles opponents, earns money, purchases items, levels up their Pokémon, and attempts to earn Gym Badges by defeating a series of gym battles.

The project is built around object-oriented programming using a custom `Pokemon` class. Every Pokémon is represented as an object with its own statistics, including its name, maximum HP, current HP, attack, defense, speed, level, and experience points (XP). The class also contains methods that allow Pokémon to display their statistics, take damage during battle, determine whether they have fainted, and display their name when printed. Using a class made it much easier to create many different Pokémon while reusing the same code for all of them.

At the beginning of the game, the player is asked to enter a trainer name and choose one of three starter Pokémon: Bulbasaur, Charmander, or Squirtle. The selected Pokémon is added to the player's team and removed from the list of available wild Pokémon. The player also begins with a small amount of money and a starter inventory containing Poké Balls and healing items.

One of the main features of the game is the battle system. During wild encounters, a random Pokémon is selected from the remaining available Pokémon. The player chooses which Pokémon from their team to send into battle. Each turn, the player can choose to attack, attempt to catch the wild Pokémon, heal using an item, run away, or switch to another Pokémon in their party. Damage is calculated using each Pokémon's attack and defense statistics with a small amount of randomness so battles are less predictable. The Pokémon with the higher speed attacks first, making speed an important statistic during battles.

Catching Pokémon is another important mechanic. The chance of successfully catching a Pokémon depends on how much health the wild Pokémon has remaining. Lower health makes catching more likely, encouraging the player to weaken opponents before throwing a Poké Ball. Successfully catching a Pokémon adds it to the player's team, removes it from the pool of wild Pokémon, increases the number of Pokémon caught, and rewards the player with money.

Winning battles rewards the player's Pokémon with experience points. When a Pokémon reaches 100 XP, it levels up, increasing its maximum HP, attack, and defense while restoring its health to full. This creates a sense of progression throughout the game and encourages players to continue battling stronger opponents.

The game also includes a shop system where players can spend money on Poké Balls, Ultra Balls, Master Balls, Potions, and Super Potions. The shop checks whether the player has enough money before completing a purchase and updates both the player's inventory and remaining balance. Healing items can then be used during battles to restore HP to injured Pokémon.

Another feature is the Pokémon Centre. At any time outside of battle, the player can visit the Pokémon Centre to fully restore every Pokémon in their team. This allows players to prepare for more difficult encounters without permanently losing progress due to fainted Pokémon.

To provide a greater challenge, the game includes Gym Battles. Each gym consists of three consecutive battles against randomly selected Pokémon. Unlike wild battles, Pokémon cannot be caught during gym fights. Winning all three battles rewards the player with a Gym Badge. Gym battles encourage players to build a stronger team instead of relying on only one Pokémon.

The game also keeps track of several achievements, including the player's trainer name, the number of Gym Badges earned, the number of Pokémon seen, and the number of Pokémon caught. This gives players additional goals beyond simply winning battles.

The project consists primarily of one Python source file that contains the game logic. Inside this file are several functions that each perform a specific task. The `battle()` function handles wild Pokémon battles, while `gym_battle()` performs similar logic for gym encounters without allowing Pokémon to be caught. The `catch()` function calculates whether a capture attempt succeeds. The `switch_pokemon()` function allows players to change their active Pokémon during battle. The `shop()` function manages purchases and inventory updates, while `heal_all()` restores every Pokémon in the player's party. The `gym()` function manages a sequence of three gym battles, and `wild_encounter()` creates random encounters with wild Pokémon. Separating the game into multiple functions helped keep the code organized and easier to understand.

While developing the project, I considered combining the wild battle and gym battle systems into a single function because they share much of the same logic. However, I decided to keep them separate because gym battles have different rules, such as preventing the player from catching Pokémon. This made the code slightly longer but also made the behaviour of each battle type easier to understand while I was developing the project.

If I continue developing this project in the future, I would like to add additional Pokémon, Pokémon types with strengths and weaknesses, multiple moves for each Pokémon instead of a single attack, evolution, save and load functionality, trainer battles, and a complete Pokédex. These additions would make the game much closer to the official Pokémon games while allowing me to continue improving my Python programming skills.

Overall, this project allowed me to apply many concepts learned throughout CS50, including object-oriented programming, functions, loops, conditionals, lists, dictionaries, random number generation, and user input. It also gave me experience designing a larger program by breaking it into smaller reusable components. I enjoyed recreating a simplified version of Pokémon and learned a great deal about structuring larger Python programs during its development.
