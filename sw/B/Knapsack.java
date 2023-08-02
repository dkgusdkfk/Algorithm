package lab3;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Knapsack {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			sb.append("#" + t + " ");
			
			String[] input = br.readLine().split(" ");
			int n = Integer.parseInt(input[0]);
			int k = Integer.parseInt(input[1]);
			
			int[] w = new int[n+1];
			int[] v = new int[n+1];
			for (int i = 1; i <= n; i++) {
				input = br.readLine().split(" ");
				w[i] = Integer.parseInt(input[0]);
				v[i] = Integer.parseInt(input[1]);
			}
			
			int[][] dp = new int[n+1][k+1];
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= k; j++) {
					if(w[i] > j) {
						dp[i][j] = dp[i-1][j];
					} else {
						dp[i][j] = Math.max(dp[i-1][j-w[i]] + v[i], dp[i-1][j]);
					}
				}
			}
			sb.append(dp[n][k]).append("\n");
		}
		System.out.println(sb);
	}
}
