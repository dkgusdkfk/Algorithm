import java.util.Scanner;

public class Main {
	static int[] prime = { 2, 3, 5, 7 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		for (int i = 0; i < 4; i++) {
			solution(n - 1, prime[i]);
		}

	}

	public static boolean isPrime(int v) {
		for (int i = 2; i <= Math.sqrt(v); i++) {
			if (v % i == 0)
				return false;
		}
		return true;
	}

	public static void solution(int cnt, int num) {
		if (cnt == 0) {
			System.out.println(num);
			return;
		}

		for (int i = 1; i <= 9; i += 2) {
			int temp = num * 10 + i;
			if (isPrime(temp))
				solution(cnt - 1, temp);
		}

	}
}