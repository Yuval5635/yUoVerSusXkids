import random as rd
import pygame
import Utils.PygameUtils as pgUtils
import Constants as Const
import Utils.Vector as Vector

class Player:

    def punch(self, enemies):
        if self.stats["punch_cooldown"] <= 0 and self.stats["stamina"] >= self.less_stats["punch_cost"]:
            self.stats["punch_cooldown"] = (6.0 - (5.0 * (self.stats["stamina"] / 100.0)))
            #print("Player12: punching")
            self.stats["stamina"] -= self.less_stats["punch_cost"]
            for enemy in enemies:
                if (enemy.pos - self.pos).distance <= self.more_stats["range"] and abs((enemy.pos - self.pos).angle - self.stats["direction"]) <= self.more_stats["range_angle"]:
                    enemy.take_damage(self.more_stats["damage"])
                    #print(Player17: , max(enemy.stats["health"], 0))

    def __init__(self):
        self.stats = {
            "stamina": 0,
            "health": 0,  # same as max_health initially
            "punch_cooldown": 0.0,  # seconds
            "direction": 0
        }
        self.less_stats = {
            "punch_cost": 20,  # stamina
            "miss_chance": 50  # percentage
        }
        self.more_stats = {
            "max_health": 10,
            "stamina_regeneration": 2,  # stamina per second
            "health_regeneration": 0.1,  # health per second when stamina is full
            "max_stamina": 20,
            "range": 20,  # pixels
            "range_angle": 45,  # degrees
            "max_speed": 20,  # pixels per second
            "damage": 10,
            "growth": 1  # percentage
        }
        self.level = self.less_stats | self.more_stats
        for key in self.level:
            self.level[key] = 0
        self.stats["health"] = self.more_stats["max_health"]
        self.pos = Vector.Vector(Const.WINDOW_WIDTH / 3, Const.WINDOW_HEIGHT / 2) #pixels
        self.budget = 0

    def take_damage(self, damage=5):
        self.stats["health"] -= damage

    def move(self, enemies):
        distance = (self.more_stats["max_speed"] * self.stats["stamina"]) / (self.more_stats["max_stamina"] * Const.FPS)
        #movement = (D-A, S-W)
        movement = Vector.Vector(int(pgUtils.PygameUtils.is_key_held(pygame.K_d)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_a)), int(pgUtils.PygameUtils.is_key_held(pygame.K_s)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_w)))
        if bool(movement):
            movement.set_distance(distance)
            self.stats["direction"] = movement.angle
            self.pos += movement
        if pgUtils.PygameUtils.is_key_pressed(pygame.K_SPACE):
            self.punch(enemies)

    def update(self, enemies):
        self.stats["punch_cooldown"] -= 1/Const.FPS
        self.stats["stamina"] += self.more_stats["stamina_regeneration"]/Const.FPS
        if self.stats["stamina"] > self.more_stats["max_stamina"]:
            self.stats["stamina"] = self.more_stats["max_stamina"]
            self.stats["health"] = min(self.stats["health"] + self.more_stats["health_regeneration"]/Const.FPS, self.more_stats["max_health"])
        self.move(enemies)

    def randomize_stats(self):
        for _ in range(self.budget):
            if rd.randint(0, len(self.less_stats) + len(self.more_stats)) < len(self.less_stats):
                keys = list(self.less_stats.keys())
                stat = rd.choice(keys)
                self.level[stat] += 1
                self.less_stats[stat] -= self.less_stats[stat] * (self.more_stats["growth"] / 100)
            else:
                keys = list(self.more_stats.keys())
                stat = rd.choice(keys)
                self.level[stat] += 1
                self.more_stats[stat] += self.more_stats[stat] * (self.more_stats["growth"] / 100)

    def __str__(self):
        name = "max health: " + str(self.more_stats["max_health"])
        name += " health: " + str(self.stats["health"])
        name += " stamina: " + str(self.stats["stamina"])
        name += " stamina regeneration: " + str(self.more_stats["stamina_regeneration"])
        name += " punch cost: " + str(self.less_stats["punch_cost"])
        name += " health regeneration: " + str(self.more_stats["health_regeneration"])
        name += " max stamina: " + str(self.more_stats["max_stamina"])
        name += " pos: " + str(self.pos)
        name += " range: " + str(self.more_stats["range"])
        name += " range angle: " + str(self.more_stats["range_angle"])
        name += " direction: " + str(self.stats["direction"])
        name += " punch cooldown: " + str(self.stats["punch_cooldown"])
        return name

    def level_up(self, other):
        max_key = "punch_cost"
        for key in self.level:
            if other.level[key] > other.level[max_key]:
                max_key = key
        self.level[max_key] += 1
        if max_key in self.less_stats:
            self.less_stats[max_key] -= self.less_stats[max_key] * (self.more_stats["growth"] / 100)
        else:
            self.more_stats[max_key] += self.more_stats[max_key] * (self.more_stats["growth"] / 100)
        #print("Player108: " + str(self.level))
        #print("Player109: " + str(self.less_stats | self.more_stats))
        #print("Player110: " + str(other.level))