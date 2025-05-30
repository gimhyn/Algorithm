import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int res = 0;

        for (int i=0; i < 5; i++) {
            int temp = scanner.nextInt();
            res += (int)(Math.pow(temp, 2));
        }

        System.out.println(res % 10);
    }
}