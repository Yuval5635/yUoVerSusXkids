package utils;

public class Vector {
    private double x;
    private double y;
    private double distance;
    private Angle angle;

    public Vector(double x, double y) {
        this.x = x;
        this.y = y;
        this.distance = Math.hypot(x, y);
        this.angle = new Angle(Math.atan2(y, x));
    }

    public Vector(double distance, Angle angle) {
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
        this.distance = distance;
        this.angle = angle;
    }

    /** 
     * Get the x component of the vector.
     * @return double - the x component of the vector
     */
    public double getX() {
        return x;
    }

    /** 
     * Get the y component of the vector.
     * @return double - the y component of the vector
     */
    public double getY() {
        return y;
    }

    /** 
     * Get the distance of the vector.
     * @return double - the distance of the vector
     */
    public double getDistance() {
        return distance;
    }

    /** 
     * Get the angle of the vector.
     * @return Angle - the angle of the vector
     */
    public Angle getAngle() {
        return angle;
    }

    /** 
     * Set the x component of the vector.
     * @param x - the new x component of the vector
     */
    public void setX(double x) {
        this.x = x;
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    /** 
     * Set the y component of the vector.
     * @param y - the new y component of the vector
     */
    public void setY(double y) {
        this.y = y;
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    /** 
     * Set the distance of the vector.
     * @param distance - the new distance of the vector
     */
    public void setDistance(double distance) {
        this.distance = distance;
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    /** 
     * Set the angle of the vector.
     * @param angle - the new angle of the vector
     */
    public void setAngle(Angle angle) {
        this.angle = angle;
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    /** 
     * Set the angle of the vector.
     * @param angle - the new angle of the vector
     */
    public void setAngle(double angle) {
        this.angle.setAngle(angle);
        this.x = distance * Math.cos(this.angle.getAngle());
        this.y = distance * Math.sin(this.angle.getAngle());
    }

    /** 
     * Add another vector to this vector.
     * @param other - the vector to add
     */
    public void add(Vector other) {
        this.x += other.getX();
        this.y += other.getY();
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    /** 
     * Subtract another vector from this vector.
     * @param other - the vector to subtract
     */
    public void subtract(Vector other) {
        this.x -= other.getX();
        this.y -= other.getY();
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    /** 
     * Multiply the vector by a scalar.
     * @param scalar - the scalar to multiply the vector by
     */
    public void multiply(double scalar) {
        this.x *= scalar;
        this.y *= scalar;
        this.distance = Math.hypot(x, y);
    }

    /** 
     * Divide the vector by a scalar.
     * @param scalar - the scalar to divide the vector by
     */
    public void divide(double scalar) {
        this.x /= scalar;
        this.y /= scalar;
        this.distance = Math.hypot(x, y);
    }

    /** 
     * Rotate the vector by a certain angle.
     * @param delta - the angle to rotate the vector by
     */
    public void rotate(Angle delta) {
        this.angle.rotate(delta);
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    /**
     * Rotate the vector by a certain angle.
     * @param delta - the angle to rotate the vector by
     */
    public void rotate(double delta) {
        this.angle.rotate(delta);
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    /**
     * Return a string representation of the vector.
     * @return String - the string representation of the vector
     */
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + " [x=" + x + ", y=" + y + "]";
    }
}
