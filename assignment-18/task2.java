public class task2 {
    /**
     * Check if a number is positive, negative, or zero.
     * @param num the number to check
     */
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println("The number is positive");
        } else if (num < 0) {
            System.out.println("The number is negative");
        } else {
            System.out.println("The number is zero");
        }
    }

    public static void main(String[] args) {
        System.out.println("Java Output:");
        checkNumber(-5);
        checkNumber(0);
        checkNumber(7);
    }
}
