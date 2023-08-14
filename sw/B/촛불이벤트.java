package lab5;

import java.util.Scanner;

public class 촛불이벤트 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int TC = sc.nextInt();
		for (int tc = 1; tc <= TC; tc++) {
			sb.append("#" + tc + " ");
			
			long L = 1;
			long R = 10000000000L;
			long n = sc.nextLong();
			
			while (L <= R) {
				long mid = (L + R) / 2;
				long k = mid * (mid + 1) /2;
				if (k < n) {
					L = mid + 1;
				} else if (k > n) {
					R = mid - 1;
				} else {	// k == n
					sb.append(mid);
					break;
				}
			}
			if (L > R) {
				sb.append(-1);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
