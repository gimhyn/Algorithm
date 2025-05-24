import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();

        if (a.matches("\\d+")) {
            int num = Integer.parseInt(a);
            System.out.println((int) Character.forDigit(num, 10));
        } else {
            System.out.println((int) a.charAt(0));
        }
    }
}