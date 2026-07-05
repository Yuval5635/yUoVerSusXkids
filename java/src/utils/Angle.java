package utils;

public class Angle {

    public static final Angle PI = new Angle(Math.PI);
    public static final Angle ZERO = new Angle(0);


    /** 
     * Convert degrees to radians.
     * @param degrees - the angle in degrees
     * @return double - the angle in radians
     */
    public static double toRadians(double degrees) {
        return degrees * (Math.PI / 180);
    }

    /** 
     * Convert radians to degrees.
     * @param radians - the angle in radians
     * @return double - the angle in degrees
     */
    public static double toDegrees(double radians) {
        return radians * (180 / Math.PI);
    }

    /** 
     * Normalize an angle to be within the range of 0 to 2π.
     * @param angle - the angle to normalize
     * @return double - the normalized angle
     */
    public static double normalize(double angle) {
        return angle % Math.PI;
    }



    private double angle;

    public Angle(double angle) {
        this.angle = normalize(angle);
    }

    /** 
     * Get the angle in radians.
     * @return double - the angle in radians
     */
    public double getAngle() {
        return this.angle;
    }

    /** 
     * Set the angle in radians.
     * @param angle - the new angle in radians
     */
    public void setAngle(double angle) {
        this.angle = normalize(angle);
    }

    /** 
     * Rotate the angle by a given amount.
     * @param delta - the amount to rotate by
     */
    public void rotate(double delta) {
        this.angle = normalize(this.angle + delta);
    }

    /** 
     * Rotate the angle by a given angle.
     * @param delta - the angle to rotate by
     */
    public void rotate(Angle delta) {
        this.angle = normalize(this.angle + delta.getAngle());
    }

    /** 
     * Scale the angle by a given factor.
     * @param factor - the factor to scale by
     */
    public void times(double factor) {
        this.angle = normalize(this.angle * factor);
    }

    /** 
     * Divide the angle by a given factor.
     * @param factor - the factor to divide by
     */
    public void divide(double factor) {
        this.angle = normalize(this.angle / factor);
    }

    /** 
     * Return a string representation of the angle.
     * @return String - the string representation of the angle
     */
    @Override
    public String toString() {
        return this.getClass().getSimpleName() + " [angle=" + angle + "]";
    }
}
