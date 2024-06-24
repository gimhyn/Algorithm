
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int [] scores = new int[N];
		// 0 <= score <= 100 , N <= 1000
		
		int max = Integer.MIN_VALUE;
		for (int i=0; i < N; i++) {
			scores[i] = scanner.nextInt();
			if (max < scores[i]) {
				max = scores[i];
			}
			
		}
		
		double sum = 0;
		scanner.close();
		for (int i=0; i < N; i++) {
			double newScore = (double)scores[i]/max*100;
			sum += newScore;
		}
		
		double res = sum / N;
		System.out.println(res);
	}
}
