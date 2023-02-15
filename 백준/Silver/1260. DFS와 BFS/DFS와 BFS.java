import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static boolean[] visited;
	static int[][] graph;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		sb = new StringBuilder();
		
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		graph = new int[n+1][n+1];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			graph[x][y] = 1;
			graph[y][x] = 1;
		}
		
		visited = new boolean[n+1];
		dfs(v);
		sb.append("\n");
		visited = new boolean[n+1];
		bfs(v);
		System.out.println(sb);
	}
	
	public static void dfs(int cur) {
		visited[cur] = true;
		sb.append(cur).append(" ");
		for (int i = 1; i <= n; i++) {
			if (graph[cur][i] == 1 && !visited[i]) {
				dfs(i);
			}
		}
	}
	
	public static void bfs(int cur) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(cur);
		visited[cur] = true;
		while (!queue.isEmpty()) {
			cur = queue.poll();
			sb.append(cur).append(" ");
			for (int i = 1; i <= n; i++) {
				if (graph[cur][i] == 1 && !visited[i]) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		}
	}
}