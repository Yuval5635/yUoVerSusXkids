package utils;

public class Angle {

    public static final Angle PI = new Angle(Math.PI);
    public static final Angle ZERO = new Angle(0);


    public static double toRadians(double degrees) {
        return degrees * (Math.PI / 180);
    }

    public static double toDegrees(double radians) {
        return radians * (180 / Math.PI);
    }

    public static double normalize(double angle) {
        return angle % Math.PI;
    }

    private double angle;

    public Angle(double angle) {
        this.angle = normalize(angle);
    }

    public double getAngle() {
        return this.angle;
    }

    public void setAngle(double angle) {
        this.angle = normalize(angle);
    }

    public void rotate(double delta) {
        this.angle = normalize(this.angle + delta);
    }

    public void rotate(Angle delta) {
        this.angle = normalize(this.angle + delta.getAngle());
    }

    public void times(double factor) {
        this.angle = normalize(this.angle * factor);
    }
}
