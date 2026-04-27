import Player
import random as rd
import Utils.Vector as Vector
import Constants as Const


class Enemy(Player.Player):

    def __init__(self, player):
        super().__init__()
        self.pos = self.spawn(player)
        self.more_stats["max_speed"] = 10
        self.more_stats["range"] = 10
        self.more_stats["damage"] = 5
        self.budget = 15

        self.randomize_stats()

        #print(Enemy22: ", self.more_stats)
    @staticmethod
    def spawn(player):
        pos = Vector.Vector(rd.randint(0, Const.WINDOW_WIDTH), rd.randint(0, Const.WINDOW_HEIGHT))
        while (pos - player.pos).distance < 50:
            pos = Vector.Vector(Const.WINDOW_WIDTH, Const.WINDOW_HEIGHT)
        return pos

    def take_damage(self, damage=10):
        self.stats["health"] -= damage

    def punch(self, player):
        if self.stats["punch_cooldown"] <= 0 and self.stats["stamina"] >= self.less_stats["punch_cost"]:
            self.stats["punch_cooldown"] = (6 - 5 * (self.stats["stamina"] / 100))
            self.stats["stamina"] -= self.less_stats["punch_cost"]
            player.take_damage(self.more_stats["damage"])
            print("Enemy32:  Punching", player.stats["health"])

    def update(self, player):
        self.stats["punch_cooldown"] -= 1/Const.FPS
        self.stats["stamina"] += self.more_stats["stamina_regeneration"]/Const.FPS
        if self.stats["stamina"] > self.more_stats["max_stamina"]:
            self.stats["stamina"] = self.more_stats["max_stamina"]
            self.stats["health"] = min(self.stats["health"] + self.more_stats["health_regeneration"]/Const.FPS, self.more_stats["max_health"])

        movement = Vector.Vector.from_polar(min(self.more_stats["max_speed"], (player.pos - self.pos).distance) / Const.FPS, (player.pos - self.pos).angle)
        if bool(movement):
            self.pos = self.pos + movement

        if (player.pos - self.pos).distance <= self.more_stats["range"]:
            self.punch(player)