package entities;

import java.util.ArrayList;
import utils.Angle;
import utils.Vector;

public class BaseEntity {

    private static final ArrayList<BaseEntity> allEntities = new ArrayList<>();

    protected double stamina;
    protected double staminaRegen;
    protected double staminaMax;

    protected double health;
    protected double healthRegen;
    protected double healthMax;

    protected double punchCooldown;
    protected double punchDamage;
    protected double punchRange;
    protected double punchStaminaCost;
    protected double punchAngle;
    protected double punchMissChance;

    protected double speedMax;

    protected Vector position;
    protected Angle angle;

    protected Vector size;



    protected BaseEntity() {
        this.stamina = 0;
        this.staminaRegen = 0;
        this.staminaMax = 0;
        this.health = 0;
        this.healthRegen = 0;
        this.healthMax = 0;
        this.punchCooldown = 0;
        this.punchDamage = 0;
        this.punchRange = 0;
        this.punchStaminaCost = 0;
        this.punchAngle = 0;
        this.punchMissChance = 0;
        this.speedMax = 0;
        this.position = new Vector(0, 0);
        this.angle = new Angle(0);
        this.size = new Vector(0, 0);

        addEntity();
    }

    /**
     * Get the list of all entities.
     * @return ArrayList<BaseEntity> - the list of all entities
     */
    public static ArrayList<BaseEntity> getAllEntities() {
        return allEntities;
    }

    /**
     * Clear the list of all entities.
     */
    public static void clearAllEntities() {
        allEntities.clear();
    }

    /**
     * Remove this entity from the list of all entities.
     */
    public void removeEntity() {
        allEntities.remove(this);
    }

    /**
     * Add this entity to the list of all entities.
     */
    private void addEntity() {
        allEntities.add(this);
    }

    

    /**
     * Set the stamina for the entity.
     * @param stamina - the max stamina for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withStamina(double stamina) {
        this.staminaMax = stamina;
        this.stamina = this.staminaMax;
        return this;
    }

    /** 
     * Set the stamina regeneration for the entity.
     * @param staminaRegen - the stamina regeneration rate for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withStaminaRegen(double staminaRegen) {
        this.staminaRegen = staminaRegen;
        return this;
    }

    /** 
     * Set the health for the entity.
     * @param health - the max health for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withHealth(double health) {
        this.healthMax = health;
        this.health = this.healthMax;
        return this;
    }

    /** 
     * Set the health regeneration for the entity.
     * @param healthRegen - the health regeneration rate for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withHealthRegen(double healthRegen) {
        this.healthRegen = healthRegen;
        return this;
    }

    /** 
     * Set the punch damage for the entity.
     * @param punchDamage - the punch damage for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPunchDamage(double punchDamage) {
        this.punchDamage = punchDamage;
        return this;
    }

    /** 
     * Set the punch range for the entity.
     * @param punchRange - the punch range for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPunchRange(double punchRange) {
        this.punchRange = punchRange;
        return this;
    }

    /** 
     * Set the punch stamina cost for the entity.
     * @param punchStaminaCost - the punch stamina cost for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPunchStaminaCost(double punchStaminaCost) {
        this.punchStaminaCost = punchStaminaCost;
        return this;
    }

    /** 
     * Set the punch angle for the entity.
     * @param punchAngle - the punch angle for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPunchAngle(double punchAngle) {
        this.punchAngle = punchAngle;
        return this;
    }

    /** 
     * Set the punch miss chance for the entity.
     * @param punchMissChance - the punch miss chance for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPunchMissChance(double punchMissChance) {
        this.punchMissChance = punchMissChance;
        return this;
    }

    /** 
     * Set the max speed for the entity.
     * @param speedMax - the max speed for the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withSpeedMax(double speedMax) {
        this.speedMax = speedMax;
        return this;
    }

    /** 
     * Set the position of the entity.
     * @param position - the position of the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withPosition(Vector position) {
        this.position = position;
        return this;
    }

    /** 
     * Set the angle of the entity.
     * @param angle - the angle of the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withAngle(Angle angle) {
        this.angle = angle;
        return this;
    }

    /** 
     * Set the size of the entity.
     * @param size - the size of the entity
     * @return BaseEntity - the entity itself
     */
    protected BaseEntity withSize(Vector size) {
        this.size = size;
        return this;
    }



    //Getters for all the attributes

    /** 
     * Get the stamina for the entity.
     * @return double
     */
    public double getStamina() {
        return stamina;
    }

    /** 
     * Get the stamina regeneration for the entity.
     * @return double
     */
    public double getStaminaRegen() {
        return staminaRegen;
    }

    /** 
     * Get the max stamina for the entity.
     * @return double
     */
    public double getStaminaMax() {
        return staminaMax;
    }

    /** 
     * Get the health for the entity.
     * @return double
     */
    public double getHealth() {
        return health;
    }

    /** 
     * Get the health regeneration for the entity.
     * @return double
     */
    public double getHealthRegen() {
        return healthRegen;
    }

    /** 
     * Get the max health for the entity.
     * @return double
     */
    public double getHealthMax() {
        return healthMax;
    }

    /** 
     * Get the punch cooldown for the entity.
     * @return double
     */
    public double getPunchCooldown() {
        return punchCooldown;
    }

    /** 
     * Get the punch damage for the entity.
     * @return double
     */
    public double getPunchDamage() {
        return punchDamage;
    }

    /** 
     * Get the punch range for the entity.
     * @return double
     */
    public double getPunchRange() {
        return punchRange;
    }

    /** 
     * Get the punch stamina cost for the entity.
     * @return double
     */
    public double getPunchStaminaCost() {
        return punchStaminaCost;
    }

    /** 
     * Get the punch angle for the entity.
     * @return double
     */
    public double getPunchAngle() {
        return punchAngle;
    }

    /** 
     * Get the punch miss chance for the entity.
     * @return double
     */
    public double getPunchMissChance() {
        return punchMissChance;
    }

    /** 
     * Get the max speed for the entity.
     * @return double
     */
    public double getSpeedMax() {
        return speedMax;
    }

    /** 
     * Get the position of the entity.
     * @return Vector - the position of the entity
     */
    public Vector getPosition() {
        return position;
    }

    /** 
     * Get the angle of the entity.
     * @return Angle - the angle of the entity
     */
    public Angle getAngle() {
        return angle;
    }

    /** 
     * Get the size of the entity.
     * @return Vector - the size of the entity
     */
    public Vector getSize() {
        return size;
    }


    
    //Setters for all the attributes

    /** 
     * Set the stamina for the entity.
     * @param stamina - the stamina for the entity
     */
    public void setStamina(double stamina) {
        this.stamina = stamina;
    }
    
    /** 
     * Set the stamina regeneration for the entity.
     * @param staminaRegen - the stamina regeneration for the entity
     */
    public void setStaminaRegen(double staminaRegen) {
        this.staminaRegen = staminaRegen;
    }

    /** 
     * Set the max stamina for the entity.
     * @param staminaMax - the max stamina for the entity
     */
    public void setStaminaMax(double staminaMax) {
        this.staminaMax = staminaMax;
    }

    /** 
     * Set the health for the entity.
     * @param health - the health for the entity
     */
    public void setHealth(double health) {
        this.health = health;
    }

    /** 
     * Set the health regeneration for the entity.
     * @param healthRegen - the health regeneration for the entity
     */
    public void setHealthRegen(double healthRegen) {
        this.healthRegen = healthRegen;
    }

    /** 
     * Set the max health for the entity.
     * @param healthMax - the max health for the entity
     */
    public void setHealthMax(double healthMax) {
        this.healthMax = healthMax;
    }

    /** 
     * Set the punch cooldown for the entity.
     * @param punchCooldown - the punch cooldown for the entity
     */
    public void setPunchCooldown(double punchCooldown) {
        this.punchCooldown = punchCooldown;
    }

    /** 
     * Set the punch damage for the entity.
     * @param punchDamage - the punch damage for the entity
     */
    public void setPunchDamage(double punchDamage) {
        this.punchDamage = punchDamage;
    }

    /** 
     * Set the punch range for the entity.
     * @param punchRange - the punch range for the entity
     */
    public void setPunchRange(double punchRange) {
        this.punchRange = punchRange;
    }

    /** 
     * Set the punch stamina cost for the entity.
     * @param punchStaminaCost - the punch stamina cost for the entity
     */
    public void setPunchStaminaCost(double punchStaminaCost) {
        this.punchStaminaCost = punchStaminaCost;
    }

    /** 
     * Set the punch angle for the entity.
     * @param punchAngle - the punch angle for the entity
     */
    public void setPunchAngle(double punchAngle) {
        this.punchAngle = punchAngle;
    }

    /** 
     * Set the punch miss chance for the entity.
     * @param punchMissChance - the punch miss chance for the entity
     */
    public void setPunchMissChance(double punchMissChance) {
        this.punchMissChance = punchMissChance;
    }

    /** 
     * Set the max speed for the entity.
     * @param speedMax - the max speed for the entity
     */
    public void setSpeedMax(double speedMax) {
        this.speedMax = speedMax;
    }

    /** 
     * Set the position of the entity.
     * @param position - the position of the entity
     */
    public void setPosition(Vector position) {
        this.position = position;
    }

    /** 
     * Set the angle of the entity.
     * @param angle - the angle of the entity
     */
    public void setAngle(Angle angle) {
        this.angle = angle;
    }

    /** 
     * Set the size of the entity.
     * @param size - the size of the entity
     */
    public void setSize(Vector size) {
        this.size = size;
    }

    

    //Logic methods for the entity

    /** 
     * add health to the entity
     * @param health - the health to add to the entity
     */
    public void addHealth(double health) {
        setHealth(getHealth() + health);
    }

    /** 
     * add stamina to the entity
     * @param stamina - the stamina to add to the entity
     */
    public void addStamina(double stamina) {
        setStamina(getStamina() + stamina);
    }

    /**
     * Move the entity by a certain angle.
     * @param delta - the angle to move the entity by
     */
    public void move(double delta) {
        if (getHealth() <= 0) return;

        getPosition().add(new Vector(getDistance(delta), getAngle()));
    }

    /** 
     * Check if the entity is alive
     * @return boolean - true if the entity is alive, false otherwise
     */
    public boolean isAlive() {
        return getHealth() > 0;
    }

    /** 
     * Check if the entity has maximum stamina
     * @return boolean - true if the entity has maximum stamina, false otherwise
     */
    public boolean isMaxStamina() {
        return getStamina() >= getStaminaMax();
    }

    /** 
     * Take damage from the entity
     * @param damage - the damage to take
     * @throws if the damage is negative 
     */
    public void takeDamage(double damage) {
        if (getHealth() <= 0) return;

        setHealth(getHealth() - damage);
    }

    /** 
     * Regenerate stamina for the entity
     * @param deltaTime - the time delta for stamina regeneration
     * @throws if the entity is dead
     */
    public void regenerateStamina(double deltaTime) {
        if (getHealth() <= 0) return;

        addStamina(getStaminaRegen() * deltaTime);
    }

    /** 
     * Regenerate health for the entity
     * @param deltaTime - the time to regenerate health for the entity
     * @throws if the entity is dead
     * @throws if the entity is not at max stamina
     */
    public void regenerateHealth(double deltaTime) {
        if (getHealth() <= 0) return;
        if (!isMaxStamina()) return;

        addHealth(getHealthRegen() * deltaTime);
    }

    /** 
     * Get the distance the entity can move in a given time delta
     * @param deltaTime - the time delta to calculate distance for
     * @return double - the distance the entity can move in the given time delta
     */
    public double getDistance(double deltaTime) {
        return (this.speedMax / deltaTime) * (this.stamina / this.staminaMax);
    }

    /**
     * Return a string representation of the entity.
     * @return String - the string representation of the entity
     */
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + " [stamina=" + stamina + ", staminaRegen=" + staminaRegen + ", staminaMax=" + staminaMax
                + ", health=" + health + ", healthRegen=" + healthRegen + ", healthMax=" + healthMax
                + ", punchCooldown=" + punchCooldown + ", punchDamage=" + punchDamage + ", punchRange=" + punchRange
                + ", punchStaminaCost=" + punchStaminaCost + ", punchAngle=" + punchAngle + ", punchMissChance="
                + punchMissChance + ", speedMax=" + speedMax + ", position=" + position + ", size="  + size  + "]";
    }
}