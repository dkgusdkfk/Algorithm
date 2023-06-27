package lab1;

import java.util.Scanner;

public class 새로운불면증치료법 {
	static boolean[] checkList;
	
	public static void main(String[] args) {
		StringBuilder sb = new StringBuilder();
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		int N, n;
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			checkList = new boolean[10];
			N = sc.nextInt();
			int k = 0;
			do {
				n = N*++k;
				while(n > 0) {
					checkList[n%10] = true;
					n /= 10;
				}
			} while(!check());
			sb.append(N*k).append("\n");
		}
		System.out.println(sb);
	}
	
	private static boolean check() {
		for (int i = 0; i < 10; i++) {
			if (!checkList[i])	return false;
		}
		return true;
	}
}
