import random
my_hp = 1000
my_power = 200
enemy_hp = 1000
enemy_power = 200
while True:
    my_hp = my_hp - enemy_power
    enemy_hp = enemy_hp - my_power
    if my_hp == 0:
        print('i lose')
        break
    elif enemy_hp == 0:
        print('you lose')
        break