import random as rd
import pygame as pg
import Utils.PygameUtils as pgUtils
import Constants as Const
import Utils.Vector as Vector

class Player:

    def reset(self):
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
        self.pos = Vector.Vector(Const.WINDOW_WIDTH / 3, Const.WINDOW_HEIGHT / 2)  # pixels
        self.budget = 0

    def punch(self, enemies):
        if self.stats["punch_cooldown"] <= 0 and self.stats["stamina"] >= self.less_stats["punch_cost"]:
            self.stats["punch_cooldown"] = (6.0 - (5.0 * (self.stats["stamina"] / 100.0)))
            #print("Player12: punching")
            self.stats["stamina"] -= self.less_stats["punch_cost"]
            for enemy in enemies:
                if (enemy.pos - self.pos).distance <= self.more_stats["range"] and abs((enemy.pos - self.pos).angle - self.stats["direction"]) <= self.more_stats["range_angle"]:
                    if rd.random() > (self.less_stats["miss_chance"] / 100.0):
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
        self.stats_name = list((self.more_stats | self.less_stats).keys())
        self.current_stat_index = 0

    def take_damage(self, damage=5):
        self.stats["health"] -= damage

    def move(self, enemies):
        distance = (self.more_stats["max_speed"] * self.stats["stamina"]) / (self.more_stats["max_stamina"] * Const.FPS)
        #movement = (D-A, S-W)
        movement = Vector.Vector(int(pgUtils.PygameUtils.is_key_held(pg.K_d)) - int(pgUtils.PygameUtils.is_key_held(pg.K_a)), int(pgUtils.PygameUtils.is_key_held(pg.K_s)) - int(pgUtils.PygameUtils.is_key_held(pg.K_w)))
        if bool(movement):
            movement.set_distance(distance)
            self.stats["direction"] = movement.angle
            self.pos += movement
        if pgUtils.PygameUtils.is_key_pressed(pg.K_SPACE):
            self.punch(enemies)

    def update(self, enemies):
        self.stats["punch_cooldown"] -= 1/Const.FPS
        self.stats["stamina"] += self.more_stats["stamina_regeneration"]/Const.FPS
        if self.stats["stamina"] > self.more_stats["max_stamina"]:
            self.stats["stamina"] = self.more_stats["max_stamina"]
            self.stats["health"] = min(self.stats["health"] + self.more_stats["health_regeneration"]/Const.FPS, self.more_stats["max_health"])
        self.move(enemies)
        self.add_point()
        if pgUtils.PygameUtils.is_key_pressed(pg.K_e):
            self.current_stat_index = (self.current_stat_index + 1) % len(self.stats_name)

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

    def level_up(self):
        self.budget += 1

    def add_point(self):
        if pgUtils.PygameUtils.is_key_pressed(pg.K_q):
            self.level[self.stats_name[self.current_stat_index]] += 1
            if self.stats_name[self.current_stat_index] in self.less_stats:
                self.less_stats[self.stats_name[self.current_stat_index]] -= self.less_stats[self.stats_name[self.current_stat_index]] * (self.more_stats["growth"] / 100)
            else:
                self.more_stats[self.stats_name[self.current_stat_index]] += self.more_stats[self.stats_name[self.current_stat_index]] * (self.more_stats["growth"] / 100)