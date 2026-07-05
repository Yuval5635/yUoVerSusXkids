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

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getDistance() {
        return distance;
    }

    public Angle getAngle() {
        return angle;
    }

    public void setX(double x) {
        this.x = x;
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    public void setY(double y) {
        this.y = y;
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    public void setDistance(double distance) {
        this.distance = distance;
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    public void setAngle(Angle angle) {
        this.angle = angle;
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }

    public void add(Vector other) {
        this.x += other.getX();
        this.y += other.getY();
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    public void subtract(Vector other) {
        this.x -= other.getX();
        this.y -= other.getY();
        this.distance = Math.hypot(x, y);
        this.angle.setAngle(Math.atan2(y, x));
    }

    public void multiply(double scalar) {
        this.x *= scalar;
        this.y *= scalar;
        this.distance = Math.hypot(x, y);
    }

    public void divide(double scalar) {
        this.x /= scalar;
        this.y /= scalar;
        this.distance = Math.hypot(x, y);
    }

    public void rotate(Angle delta) {
        this.angle.rotate(delta);
        this.x = distance * Math.cos(angle.getAngle());
        this.y = distance * Math.sin(angle.getAngle());
    }
}
