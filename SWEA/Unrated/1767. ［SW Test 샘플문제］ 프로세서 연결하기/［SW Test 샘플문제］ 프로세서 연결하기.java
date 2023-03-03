import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	static int N;
	static List<Core> core;

	static int result = Integer.MAX_VALUE;
	static int coreCount;


	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	private static class Core {
		int r;
		int c;
		public Core(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");

			N = Integer.parseInt(br.readLine().trim());

			int[][] map = new int[N][N];
			core = new ArrayList<>();
			result = 0;
			coreCount = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if (map[i][j] == 1) {
						if (i == 0 || i == N-1 || j == 0 || j == N-1)	continue;
						core.add(new Core(i, j));
					}
				}
			}

			go(map, 0, 0, 0);
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}

	private static void go(int[][] map, int idx, int count, int coreCnt) {
		if (idx == core.size())	{
			if (coreCount == coreCnt) {
				result = Math.min(result, count);
			} else if (coreCount < coreCnt) {
				result = count;
				coreCount = coreCnt;
			}
			return;
		}


		Core c = core.get(idx);
		int x = c.r;
		int y = c.c;

		for (int d = 0; d < 4; d++) {
			if (check(map, x, y, d)) {

				go(map, idx+1, count + move(map, x, y, d), coreCnt + 1);

				remove(map, x, y, d);
			}
		}
		go(map, idx+1, count, coreCnt);
	}
	
	private static int move(int[][] map, int x, int y, int d) {
		int tmpCnt = 0;
		while (0 < x && x < N-1 && 0 < y && y < N-1) {
			x += dx[d];
			y += dy[d];
			map[x][y] = 1;
			tmpCnt++;
		}
		return tmpCnt++;
	}
	
	private static void remove(int[][] map, int x, int y, int d) {
		while (0 < x && x < N-1 && 0 < y && y < N-1) {
			x += dx[d];
			y += dy[d];
			map[x][y] = 0;
		}
	}

	private static boolean check(int[][] map, int x ,int y, int d) {
		while (0 < x && x < N-1 && 0 < y && y < N-1) {
			x += dx[d];
			y += dy[d];
			if (map[x][y] != 0)	return false;
		}
		return true;
	}
}