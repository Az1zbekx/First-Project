import random

print("1 dan 1000 oraliqdagi istalgan son kiriting")

x = random.randint(1, 1000)

while True:

    y = int(input())

    if y > x:
        print("Siz katta son kiritdingiz")
    elif y < x:
        print("Siz kichik son kiritdingiz")
    else:
        print("Siz sonni topdingiz")
        break
