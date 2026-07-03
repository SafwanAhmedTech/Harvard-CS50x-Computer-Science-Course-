while True:
    try:
        change = float(input("Change owed: "))
        if change > 0:
            break
    except ValueError:
        pass

change = round(change * 100)

coins = 0

coins += change // 25
change %= 25

coins += change // 10
change %= 10

coins += change // 5
change %= 5

coins += change

print(coins)
