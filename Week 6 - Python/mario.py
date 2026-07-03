while True:
    try:
        height = int(input("Height: "))

        if 1 <= height <= 8:
            break

    except ValueError:
        pass

spaces = height
shape = 0
for i in range(height):
    spaces -= 1
    shape += 1
    print(" " * (spaces), end="")
    print("#" * (shape))
