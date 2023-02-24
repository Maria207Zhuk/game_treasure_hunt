import random as r


class Game:
    def __init__(self, sh, v, nik):
        self.sh = sh
        self.v = v
        self.nik = nik
        self.game_x = r.randint(0, v-1)
        self.game_y = r.randint(0, v-1)

    def play(self):
        print(f"Привіт, {self.nik}!  - ({self.game_x}, {self.game_y})")
        spr = 0
        while True:
            print("в тебе є дві точки x/y, введи свої координати")
            data_x = int(input("дані координати x: "))
            data_y = int(input("дані координати y: "))
            spr += 1
            if data_x == self.game_x and data_y == self.game_y:
                print(f"Вітаємо! ви знайшли скарб за {spr} спроб!")
                break
            else:
                print(" На жаль ви ввели не правильні координати. \n Повторіть спробу")

# вступ
print("Привіт! Ти у нашій грі 'Пошук скарбів'")
nik = input("Який ваш нік?: ")
lvl = input("Який рівень обираєте (легкий, середній, складний):")
if lvl == "легкий":
    game = Game(1, 5, nik)
elif lvl == "середній":
    game = Game(1, 10, nik)
elif lvl == "складний":
    game = Game(1, 15, nik)
else:
    print("Ви ввели невірно! Введіть один варіант з яких ми вам запропонувал")
    exit()

game.play()