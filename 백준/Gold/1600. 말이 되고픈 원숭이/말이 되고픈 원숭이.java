import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] mx = {-1, 1, 0, 0};
	static int[] my = {0, 0, -1, 1};
	static int[] hx = {-1, -2, -2, -1, 1, 2, 2, 1};
	static int[] hy = {-2, -1, 1, 2, -2, -1, 1, 2};
	
	static class Info {
		int x, y, k, c;
		Info(int x, int y, int k, int c) {
			this.x = x;
			this.y = y;
			this.k = k;
			this.c = c;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int K = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		int w = Integer.parseInt(st.nextToken());
		int h = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[h][w];
		for (int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		boolean[][][] visited = new boolean[h][w][K+1];
		
		Queue<Info> queue = new ArrayDeque<>();
		visited[0][0][K] = true;
		queue.add(new Info(0, 0, K, 0));
		while (!queue.isEmpty()) {
			Info info = queue.poll();
			int x = info.x;
			int y = info.y;
			int k = info.k;
			int c = info.c;
			if (x == h-1 && y == w-1) {
				System.out.println(c);
				System.exit(0);
			}
			for (int i = 0; i < 4; i++) {
				int nx = x + mx[i];
				int ny = y + my[i];
				if (!(0 <= nx && nx < h && 0 <= ny && ny < w) || map[nx][ny] == 1 || visited[nx][ny][k])
					continue;
				visited[nx][ny][k] = true;
				queue.add(new Info(nx, ny, k, c+1));
			}
			if (k == 0)	continue;
			for (int i = 0; i < 8; i++) {
				int nx = x + hx[i];
				int ny = y + hy[i];
				if (!(0 <= nx && nx < h && 0 <= ny && ny < w) || map[nx][ny] == 1 || visited[nx][ny][k-1])
					continue;
				visited[nx][ny][k-1] = true;
				queue.add(new Info(nx, ny, k-1, c+1));
			}
		}
		System.out.println(-1);
	}
}