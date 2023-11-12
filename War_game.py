import threading
import random
import time

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, other):
        while True:
            time.sleep(random.randint(1, 5))
            if self.health <= 0:
                print(f'{other.name} одержал победу!\n')
                break
            if other.health <= 0:
                break
            other.health -= 25
            print(f'{self.name} ударил, у {other.name} осталось {other.health} очков здоровья')

warrior1 = Warrior('Антон')
warrior2 = Warrior('Тельман')

# создаем и запускаем два потока, каждый из которых представляет собой воина, атакующего другого
thread1 = threading.Thread(target=warrior1.attack, args=(warrior2,))
thread2 = threading.Thread(target=warrior2.attack, args=(warrior1,))

thread1.start()
thread2.start()
