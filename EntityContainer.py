import Player
import Enemy

class EntityContainer:
    def __init__(self):
        self.player = Player.Player()
        self.level = 1
        self.enemies = []
        self.is_player_alive = True
        
    def start_level(self):
        self.enemies = []
        for i in range(self.level):
            self.enemies.append(Enemy.Enemy())

    def set_level(self, level):
        self.level = level

    def update(self):
        self.player.update(self.enemies)

        for enemy in self.enemies:
            if enemy.changeable_stats["health"] <= 0:
                self.player.level_up(enemy)
                self.enemies.remove(enemy)
                print("EntityContainer26: ", str(self.player))
            else:
                enemy.update(self.player)

        self.is_player_alive = self.player.stats["health"] > 0

    def is_enemies_dead(self):
        if len(self.enemies) == 0:
            return True
        return False