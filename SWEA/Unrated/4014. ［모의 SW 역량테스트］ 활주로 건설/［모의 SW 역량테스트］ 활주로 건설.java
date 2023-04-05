import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());

			int[][] map = new int[n + 2 * x][n + 2 * x];
			for (int i = x; i < n + x; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = x; j < n + x; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int count = 0;

			// 가로
			for (int i = x; i < n + x; i++) {
				boolean[] visited = new boolean[n + 2 * x];
				int j;
				for (j = x; j < n + x - 1; j++) {
					if (Math.abs(map[i][j] - map[i][j + 1]) > 1)
						break;
					if (map[i][j] - map[i][j + 1] == 1 && map[i][j + 1] != 0) {
						int k;
						for (k = 1; k < x; k++) {
							if (map[i][j + k] != map[i][j + k + 1])
								break;
						}
						if (k != x)
							break;
						for (k = 1; k < x; k++) {
							visited[j + k + 1] = true;
						}
					} else if (map[i][j] - map[i][j + 1] == -1) {
						int k;
						if (visited[j])
							break;
						for (k = 1; k < x; k++) {
							if (map[i][j - k] != map[i][j - k + 1] || visited[j - k])
								break;
						}
						if (k != x)
							break;
						for (k = 1; k < x; k++) {
							visited[j - k] = true;
						}
					}
				}
				if (j == n + x - 1)
					count++;
			}

			// 세로
			for (int j = x; j < n + x; j++) {
				boolean[] visited = new boolean[n + 2 * x];
				int i;
				for (i = x; i < n + x - 1; i++) {
					if (Math.abs(map[i][j] - map[i + 1][j]) > 1)
						break;
					if (map[i][j] - map[i + 1][j] == 1 && map[i + 1][j] != 0) {
						int k;
						for (k = 1; k < x; k++) {
							if (map[i + k][j] != map[i + k + 1][j])
								break;
						}
						if (k != x)
							break;
						for (k = 1; k < x; k++) {
							visited[i + k + 1] = true;
						}
					} else if (map[i][j] - map[i + 1][j] == -1) {
						int k;
						if (visited[i])
							break;
						for (k = 1; k < x; k++) {
							if (map[i - k][j] != map[i - k + 1][j] || visited[i - k])
								break;
						}
						if (k != x)
							break;
						for (k = 1; k < x; k++) {
							visited[i - k] = true;
						}
					}
				}
				if (i == n + x - 1)
					count++;
			}

			sb.append(count).append("\n");
		}
		System.out.println(sb);
	}
}