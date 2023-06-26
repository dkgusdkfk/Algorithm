import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			int n = Integer.parseInt(br.readLine());
			int m = Integer.parseInt(br.readLine());
			
			int[][] arr = new int[n][n];
			for (int i = 0; i < n; i++) {
				arr[i][i] = 2;
			}
			
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken())-1;
				int b = Integer.parseInt(st.nextToken())-1;
				arr[a][b] = 1;
				arr[b][a] = -1;
			}
			
			for (int k = 0; k < n; k++) {
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						if (arr[i][k] == arr[k][j] && arr[i][k] != 0) {
							arr[i][j] = arr[i][k];
							arr[j][i] = -arr[i][k];
						}
					}
				}
			}
			
			int result = 0;
			for (int[] ar : arr) {
				int i;
				for (i = 0; i < n; i++) {
					if (ar[i] == 0)
						break;
				}
				if (i == n)
					result++;
			}
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}
}