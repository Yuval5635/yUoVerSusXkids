package entities;

import utils.Vector;

public class Enemy extends BaseEntity {
    public Enemy(double health, double stamina, double speed, Vector position, Vector size) {
        super();
        this.withHealth(health)
            .withStamina(stamina)
            .withSpeedMax(speed)
            .withPosition(position)
            .withSize(size);
    }
}
