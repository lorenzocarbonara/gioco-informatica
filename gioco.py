class Entity:
    def __init__(self, x, y ,field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)
    def move(self, direction):
        if direction == "up"  and self.y > 0:
            self.y -= 1
        elif direction == "down"  and self.y < field.h - 1:
            self.y += 1
        elif direction == "left"  and self.x > 0:
            self.x -= 1
        elif direction == "right"  and self.x < field.w - 1:
            self.x += 1


class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = 10
        self.damage = damage
    

class Field:
    def __init__(self):
        self.w = 5
        self.h = 5
        self.entities = []
    
    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if y == e.y and x == e.x:
                        print('[X]', end = '')
                        break

                else:
                    print('[ ]', end = '')
            print()
            
field = Field()
m = Monster(2, 2, "Eren", 10, field)

while True:
    field.draw()
    move=input("inserire un comando di movimento tra up, right, left, down (per interrompere digitare ""stop""): ")
    if move == "stop":
        quit()
    m.move(move)