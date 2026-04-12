import pygame
import Utils.PygameUtils as pgUtils
import Constants as Const
import Utils.Vector as Vector

class Player:

    def punch(self, enemies):
        if self.punch_cooldown <= 0 and self.stamina >= self.punch_cost:
            self.punch_cooldown = (6 - 5 * (self.stamina / 100))
            print("Player11: PUNCHING", self.punch_cooldown)
            self.stamina -= self.punch_cost
            print("Player13: ", self)
            for enemy in enemies:
                print("Player15: ", enemy)
                if (enemy.pos - self.pos).distance <= self.range and abs((enemy.pos - self.pos).angle - self.direction) <= self.range_angle:
                    enemy.take_damage()

    def __init__(self):
        self.max_health = 10
        self.health = self.max_health
        self.stamina = 0
        self.stamina_regeneration = 2 #stamina per second
        self.punch_cost = 20 #stamina
        self.health_regeneration = 0.1 #health per second when stamina is full
        self.max_stamina = 20
        self.pos = Vector.Vector(Const.WINDOW_WIDTH / 3, Const.WINDOW_HEIGHT / 2) #pixels
        self.range = 15 #pixels
        self.range_angle = 45 #degrees
        self.direction = 0
        self.punch_cooldown = 0 #seconds
        self.max_speed = 20 #pixel per second
        self.miss_chance = 0 #precentage

    def take_damage(self, damage=5):
        self.health -= damage

    def move(self, enemies):
        distance = (self.max_speed * self.stamina) / (self.max_stamina * Const.FPS)
        #movement = (D-A, S-W)
        movement = Vector.Vector(int(pgUtils.PygameUtils.is_key_held(pygame.K_d)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_a)), int(pgUtils.PygameUtils.is_key_held(pygame.K_s)) - int(pgUtils.PygameUtils.is_key_held(pygame.K_w)))
        if bool(movement):
            movement.set_distance(distance)
            self.direction = movement.angle
            self.pos += movement
        if pgUtils.PygameUtils.is_key_pressed(pygame.K_SPACE):
            self.punch(enemies)

    def update(self, enemies):
        self.punch_cooldown -= 1/Const.FPS
        self.stamina += self.stamina_regeneration/Const.FPS
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
            self.health = min(self.health + self.health_regeneration/Const.FPS, self.max_health)
        self.move(enemies)

    def __str__(self):
        name = "max health: " + str(self.max_health)
        name += " health: " + str(self.health)
        name += " stamina: " + str(self.stamina)
        name += " stamina regeneration: " + str(self.stamina_regeneration)
        name += " punch cost: " + str(self.punch_cost)
        name += " health regeneration: " + str(self.health_regeneration)
        name += " max stamina: " + str(self.max_stamina)
        name += " pos: " + str(self.pos)
        name += " range: " + str(self.range)
        name += " range angle: " + str(self.range_angle)
        name += " direction: " + str(self.direction)
        name += " punch cooldown: " + str(self.punch_cooldown)
        return name