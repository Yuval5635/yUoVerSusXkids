import Player
import random
import Utils.Vector as Vector
import Constants as Const


class Enemy(Player.Player):

    def __init__(self):
        super().__init__()
        self.pos = Vector.Vector(500, random.randint(50, 250))
        self.max_speed = 10

    def take_damage(self, damage=100):
        self.health -= damage

    def punch(self, player):
        if self.punch_cooldown <= 0:
            self.punch_cooldown += 5
            player.take_damage()
            print("Enemy21:  Punching", player.health)

    def update(self, player):
        self.punch_cooldown -= 1/Const.FPS
        movement = Vector.Vector.from_polar(min(self.max_speed, (player.pos - self.pos).distance) / Const.FPS, (player.pos - self.pos).angle)
        print("Enemy25: ", (player.pos - self.pos).distance, self.range)
        if bool(movement):
            self.pos = self.pos + movement

        if (player.pos - self.pos).distance <= self.range:
            self.punch(player)