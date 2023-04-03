import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static int n, m, result = 0, count = 0;
	static int[][] map;
	
	static class Info {
		int x, y;
		Info(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		air(0, 0);
		
		melt();
		System.out.println(result);
		System.out.println(count);
		
	}
	
	private static void air(int x, int y) {
		if (0 > x || x >= n || 0 > y || y >= m)	return;
		if (map[x][y] == 0) {
			map[x][y] = -1;
			for (int i = 0; i < 4; i++) {
				air(x+dx[i], y+dy[i]);
			}
		}
	}
	
	private static void melt() {
		Queue<Info> queue = new ArrayDeque<>();
		
		int flag = 0;
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1) {
					flag = 1;
					cnt++;
					for (int d = 0; d < 4; d++) {
						if (map[i+dx[d]][j+dy[d]] == -1) {
							queue.add(new Info(i, j));
							break;
						}
					}
				}
			}
		}
		
		while(!queue.isEmpty()) {
			Info info = queue.poll();
			int x = info.x;
			int y = info.y;
			map[x][y] = 0;
			air(x, y);
		}
		
		if (flag == 1) {
			result++;
			count = cnt;
			melt();
		}
	}
}