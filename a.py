# 일반 유닛

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격 유닛

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 치유 유닛

class MedicUnit(Unit):
    def __init__(self, name, hp, speed, heal):
        Unit.__init__(self, name, hp, speed)
        self.heal = heal
    
    def healing(self, target):
        target.hp += self.heal
        print(f"{target.name} : 체력이 {self.heal}만큼 회복되었습니다. [체력 : {target.hp}]")

# 비행 유닛

class FlyUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

# 공중 공격 유닛

class FlyableAttackUnit(AttackUnit, FlyUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyUnit.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 유닛

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
firebat = AttackUnit("파이어뱃", 50, 5, 16)
firebat.attack("1시")
firebat.damaged(25)
medic = MedicUnit("메딕", 40, 5, 10)
medic.healing(firebat)
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "1시")
firebat.move("1시")
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
battlecruiser.move("9시")
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
game_over()