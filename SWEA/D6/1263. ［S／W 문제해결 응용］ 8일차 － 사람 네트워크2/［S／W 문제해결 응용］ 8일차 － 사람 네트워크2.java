import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		final int INF = 99999;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int[][] map = new int[n][n];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if (i!=j && map[i][j] == 0) {
						map[i][j] = INF;
					}
				}
			}
			
			for (int k = 0; k < n; k++) {
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (map[i][j] > map[i][k] + map[k][j]) {
							map[i][j] = map[i][k] + map[k][j];
						}
					}
				}
			}
			
			int result = Integer.MAX_VALUE;
			for (int i = 0; i < n; i++) {
				int res = 0;
				for (int j = 0; j < n; j++) {
					res += map[i][j];
				}
				result = Math.min(result, res);
			}
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}
}