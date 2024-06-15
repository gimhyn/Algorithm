import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Scanner 객체를 생성하여 입력을 받을 준비를 합니다.
        Scanner scanner = new Scanner(System.in);
        
        // 정수 A와 B를 입력받습니다.
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        
        // 입력받은 두 정수의 합을 출력합니다.
        System.out.println(A + B);
        
        // Scanner 객체를 닫아줍니다.
        scanner.close();
    }
}
