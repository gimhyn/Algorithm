import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int tc = 0; tc < T; tc++) {
            int R = sc.nextInt();
            // nextLine(): 개행문자까지 가져옴. next(): 개행문자 무시
            String str = sc.next();
//            String: 불변 매번 새 객체 생성. Stringbuilder: mutable
            StringBuilder res = new StringBuilder();
            for (int i=0; i < str.length(); i++) {
                for (int j=0; j < R; j++) {
                    res.append(str.charAt(i));
                }
            }
            System.out.println(res.toString());
        }
    }
}