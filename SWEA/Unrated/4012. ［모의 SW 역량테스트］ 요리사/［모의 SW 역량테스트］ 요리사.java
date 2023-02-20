import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int[][] s;
	static boolean[] isSelected;
	static int result;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			N = Integer.parseInt(br.readLine());

			s = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					s[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			isSelected = new boolean[N];
			result = Integer.MAX_VALUE;
			combination(0, 0);
			sb.append(result).append("\n");
		}
		System.out.println(sb);

	}

	public static void combination(int cnt, int start) {
		if (cnt == N / 2) {
			int a = 0;
			int b = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (isSelected[i] && isSelected[j]) {
						a += s[i][j];
					} else if (!isSelected[i] && !isSelected[j]) {
						b += s[i][j];
					}
				}
			}
			result = Math.min(result, Math.abs(a - b));

			return;
		}
		for (int i = start; i < N; i++) {
			isSelected[i] = true;
			combination(cnt + 1, i + 1);
			isSelected[i] = false;
		}
	}
}