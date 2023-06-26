import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static int n, m;
	static int[][] map;
	static Queue<int[]> queue;
	
	static int V;
	static List<Edge> edgeList;
	static int[] parents;
	
	static class Edge implements Comparable<Edge>{
		int from, to, weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}

	}
	
	static void makeSet() {
		parents = new int[V];
		for (int i = 0; i < V; i++) {
			parents[i] = i;
		}
	}
	
	static int findSet(int a) {
		if (a==parents[a]) return a;
		return parents[a] = findSet(parents[a]);
	}
	
	static boolean union(int a, int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);
		
		if (aRoot == bRoot) return false;
		
		parents[bRoot] = aRoot;
		return true;		
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
		
		int idx = 1;
		queue = new ArrayDeque<int[]>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1) {
					dfs(i, j, ++idx);
				}
			}
		}
		
		int[][] dist = new int[idx-1][idx-1];
		for (int i = 0; i < idx-1; i++) {
			Arrays.fill(dist[i], Integer.MAX_VALUE);
		}
		while (!queue.isEmpty()) {
			int x = queue.peek()[0];
			int y = queue.poll()[1];
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				int cnt = 0;
				while (check(nx,ny) && map[nx][ny] == 0) {
					cnt++;
					nx += dx[d];
					ny += dy[d];
				}
				if (!check(nx, ny) || cnt < 2 || map[nx][ny] == map[x][y])	continue;
				int a = Math.min(map[x][y], map[nx][ny])-2;
				int b = Math.max(map[x][y], map[nx][ny])-2;
				dist[a][b] = Math.min(dist[a][b], cnt);
			}
		}
		
		edgeList = new ArrayList<>();
		V = idx -1;
		
		for (int i = 0; i < V; i++) {
			for (int j = i+1; j < V; j++) {
				if (dist[i][j] == Integer.MAX_VALUE)	continue;
				edgeList.add(new Edge(i, j, dist[i][j]));
			}
		}
		Collections.sort(edgeList);
		
		makeSet();
		int result = 0, count = 0;
		
		for (Edge edge : edgeList) {
			if (union(edge.from, edge.to)) {
				result += edge.weight;
				if(++count == V)	break;
			}
		}
		System.out.println(count != V-1? -1 : result);
	}
	
	private static boolean check(int x, int y) {
		if (x<0 || x>=n || y<0 || y>=m)	return false;
		return true;
	}
	
	private static void dfs(int x, int y, int c) {
		if (!check(x, y))	return;
		if (map[x][y] == 1) {
			queue.add(new int[] {x, y});
			map[x][y] = c;
			for (int i = 0; i < 4; i++) {
				dfs(x+dx[i], y+dy[i], c);
			}
		}
	}
}