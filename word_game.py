from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')
# Pause for 10 seconds
time.sleep(10)
# Clear the screen by printing 20 newlines
for i in range(20):
    print()

# Initialize the number of holy stones and the number of soldiers
holy_stones = 1000
archers = 0
Axeman = 0
max_archers = holy_stones // 100
remaining_holy_stones = holy_stones % 100
max_axeman = remaining_holy_stones // 120
# Print the results
print(f"With {holy_stones} holy stones, you can purchase {max_archers} archers and {max_axeman} axe soldiers.")

# Initialize the number of forests and the soldiers available
num_forests = 7
soldiers = ["Archer", "Axe Soldier", "Mage"]

# Iterate over the forests
i = 1
while i <= num_forests:
    # Print the current forest and the available soldiers
    print(f"Forest {i}:")
    print("----------")
    print("Monsters:")
    print("----------")
    if i == 1:
        print("Archer")
    elif i == 2:
        print("Axeman")
    elif i == 3:
        print("Archer")
    elif i == 4:
        print("Axeman")
    elif i == 5:
        print("Archer")
    elif i == 6:
        print("Axeman")
    elif i == 7:
        print("Archer")
    print("\nAvailable soldiers:")
    for soldier in soldiers:
        print(soldier)

    # Prompt the user to choose a soldier
    chosen_soldier = input("\nChoose a soldier to send: ")

    # Check if the chosen soldier is available
    if chosen_soldier in soldiers:
        # Remove the chosen soldier from the list of available soldiers
        soldiers.remove(chosen_soldier)

        # Print a message indicating that the soldier has been sent
        print(f"\n{chosen_soldier} has been sent to forest {i}!")

        # Move on to the next forest
        i += 1
    else:
        # Print an error message if the chosen soldier is not available
        print("\nInvalid soldier! Please choose another.")

# Print a message indicating that all forests have been cleared
print("\nAll forests have been cleared!")

# Initialize the number of forests and the soldiers available
num_forests = 7
soldiers = ["Archer", "Axe Soldier", "Mage"]

# Iterate over the forests
i = 1
while i <= num_forests:
    # Print the current forest and the available soldiers
    print(f"Forest {i}:")
    print("----------")
    print("Monsters:")
    print("----------")
    if i == 1:
        print("Goblin")
        monster_hp = 10
    elif i == 2:
        print("Orc")
        monster_hp = 20
    elif i == 3:
        print("Troll")
        monster_hp = 30
    elif i == 4:
        print("Dragon")
        monster_hp = 40
    elif i == 5:
        print("Wyvern")
        monster_hp = 50
    elif i == 6:
        print("Hydra")
        monster_hp = 60
    elif i == 7:
        print("Gorgon")
        monster_hp = 70

    print("\nAvailable soldiers:")
    for soldier in soldiers:
        print(soldier)

    # Prompt the user to choose a soldier
    chosen_soldier = input("\nChoose a soldier to send: ")

    # Check if the chosen soldier is available
    if chosen_soldier in soldiers:
        # Remove the chosen soldier from the list of available soldiers
        soldiers.remove(chosen_soldier)

        # Initialize the soldier's hit points
        if chosen_soldier == "Archer":
            soldier_hp = 15
        elif chosen_soldier == "Axe Soldier":
            soldier_hp = 20
        elif chosen_soldier == "Mage":
            soldier_hp = 10

        # Fight the monster until either the soldier or the monster is defeated
        while soldier_hp > 0 and monster_hp > 0:
            # Attack the monster
            monster_hp -= 5
            print(f"{chosen_soldier} attacks the monster and deals 5 damage!")

            # Check if the monster is defeated
            if monster_hp <= 0:
                print(f"{chosen_soldier} has defeated the monster!")
                break

            # Have the monster attack the soldier
            soldier_hp -= 3
            print(f"The monster attacks {chosen_soldier} and deals 3 damage!")

            # Check if the soldier is defeated
            if soldier_hp <= 0:
                print(f"{chosen_soldier} has been defeated!")

        # Check if the player has run out of soldiers
        if len(soldiers) == 0:
            print("You have run out of soldiers! Game over.")
            break

        # Move on to the next forest if the monster has been defeated
        if monster_hp <= 0:
            break