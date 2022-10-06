from random import randint
from time import time


def choose_option():
    print("\n[1] - перша задача")
    print("[2] - друга задача")
    print("[3] - третя задача")
    print("[q] - вихід\n")
    a = input()
    if a == "q":
        exit()
    return int(a)


def first():
    i = 8
    while i <= 4096:
        print(f"\nЯкщо довжина ключа дорівнює {i} біт - то простір ключів дорівнює {2**i}")
        i *= 2
    print()


def second():
    i = 8
    keys = {}
    while i <= 4096:
        keys[i] = randint(0, 2 ** i)
        print(f"\nЗгенерований ключ ({i} біт) - {hex(keys[i])}")
        i *= 2
    print()
    return keys

def third(keys):
    for key in keys:
        start_time = time()
        i = 0
        while i != keys[key]:
            i += 1
        print(f"\n{i} = {hex(keys[key])}, знайдено за {int((time() - start_time)*1000)} мс")


while 1:
    r = choose_option()
    if r == 1:
        first()
    elif r == 2:
        keys = second()
    else:
        try:
            third(keys)
        except:
            print("\nНеобхідно спочатку згенерувати ключі (опція [2])\n")
