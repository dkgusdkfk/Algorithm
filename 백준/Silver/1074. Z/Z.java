import java.util.Scanner;

public class Main {
	private static int r, c, N;
	private static int cnt = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		r = sc.nextInt();
		c = sc.nextInt();
		solution(0, 0, 1<<N);

		System.out.println(cnt);

	}

	private static void solution(int x, int y, int n) {
		if (x == r && y == c)
			return;
		int half = n / 2;
		if ((x + half) <= r && r < (x + n)) {
			x += half;
			cnt += half * half * 2;
		}
		if ((y + half) <= c && c < (y + n)) {
			y += half;
			cnt += half * half;
		}
		solution(x, y, half);
	}
}