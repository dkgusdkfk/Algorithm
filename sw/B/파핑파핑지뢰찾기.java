import java.util.Scanner;

public class ������������ã�� {
	
	static char[][] map;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int T = sc.nextInt();
		for (int tc = 0; tc < T; tc++) {
			sb.append("#" + tc + " ");
			
			int n = sc.nextInt();
			
			map = new char[n+2][n+2];
			for (int i = 1; i <= n; i++) {
				String input = sc.next();
				for (int j = 1; j <= n; j++) {
					map[i][j] = input.charAt(j-1);
				}
			}
		}
		
		System.out.println(sb);
	}
}
