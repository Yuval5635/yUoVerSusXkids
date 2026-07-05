package entities;

public class Enemy extends BaseEntity {
    public Enemy(double health, double stamina, double speed, double x, double y) {
        super();
        this.withHealth(health)
            .withStamina(stamina)
            .withSpeedMax(speed);
    }
}
