class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power
    def see_people(self, name):
        if name == 'WYZ':
            print('师弟！！！！')
        elif name == '李秋水':
            print('呸，贱人')
        elif name == '丁春秋':
            print('叛徒！我杀了你')
        else:
            print('查无此人，请重新输入')
    def fight_zms(self, enemy_hp, enemy_power):
        my_hp = self.hp/2 - enemy_power
        my_power = self.power*10
        enemy_hp = enemy_hp - my_power
        if my_hp > enemy_hp:
            print('i win!!')
        elif my_hp < enemy_hp:
            print('you win!!')
        else:
            print('draw...')
tonglao = TongLao(1000, 20)
tonglao.see_people('WYZ')
tonglao.fight_zms(900, 20)
# print(tonglao.see_people('WYZ'))
# print(tonglao.fight_zms(900, 20))