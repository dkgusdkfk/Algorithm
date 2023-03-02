import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] graph;
	static Info shark;
	static int size = 2;
	static int time = 0;
	static int eat = 0;

	static int[] dx = { -1, 0, 0, 1 };
	static int[] dy = { 0, -1, 1, 0 };

	static class Info implements Comparable<Info> {
		int x;
		int y;
		int t;

		public Info(int x, int y, int t) {
			super();
			this.x = x;
			this.y = y;
			this.t = t;
		}

		@Override
		public int compareTo(Info o) {
			if (this.t == o.t) {
				if (this.x == o.x) {
					return this.y - o.y;
				} else {
					return this.x - o.x;
				}
			} else {
				return this.t - o.t;
			}
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		graph = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 9) {
					shark = new Info(i, j, 0);
					graph[i][j] = 0;
				}
			}
		}

		while (bfs())
			;
		System.out.println(time);

	}

	private static boolean bfs() {
		boolean[][] visited = new boolean[N][N];
		Queue<Info> queue = new ArrayDeque<>();
		queue.add(shark);
		visited[shark.x][shark.y] = true;
		ArrayList<Info> temp = new ArrayList<>();
		while (!queue.isEmpty()) {
			Info info = queue.poll();
			int x = info.x;
			int y = info.y;
			int t = info.t;
			for (int i = 0; i < 4; i++) {
				int mx = x + dx[i];
				int my = y + dy[i];
				if (!(0 <= mx && mx < N && 0 <= my && my < N) || visited[mx][my])
					continue;
				if (graph[mx][my] == 0) {
					visited[mx][my] = true;
					queue.add(new Info(mx, my, t + 1));
					continue;
				}
				if (graph[mx][my] < size) {
					visited[mx][my] = true;
					temp.add(new Info(mx, my, t + 1));
				} else if (graph[mx][my] == size) {
					queue.add(new Info(mx, my, t + 1));
					visited[mx][my] = true;
				}
			}
		}
		if (temp.size() == 0)
			return false;
		Collections.sort(temp);
		Info info = temp.get(0);
		graph[info.x][info.y] = 0;
		eat++;
		if (eat >= size) {
			eat -= size;
			size++;
		}
		time += info.t;
		info.t = 0;
		shark = info;
		return true;
	}
}