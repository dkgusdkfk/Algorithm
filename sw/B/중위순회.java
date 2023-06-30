package lab2;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 중위순회 {
	static StringBuilder sb = new StringBuilder();
	static int N;
	static char[] arr;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#" + tc + " ");
			N = Integer.parseInt(br.readLine());
			
			arr = new char[N+1];
			
			for (int i = 1; i <= N; i++) {
				arr[i] = br.readLine().split(" ")[1].charAt(0);
			}
			dfs(1);
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	private static void dfs(int cur) {
		if (cur > N) return;
		
		dfs(cur*2);
		sb.append(arr[cur]);
		dfs(cur*2 + 1);
	}
}
