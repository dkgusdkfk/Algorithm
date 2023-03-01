import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	
	static int T = 10;
	static List<List<Integer>> arr;
	
	static class Info {
		int idx;
		int count;
		public Info(int idx, int count) {
			super();
			this.idx = idx;
			this.count = count;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = null;
		
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			arr = new ArrayList<>();
			for (int i = 0; i <= 100; i++) {
				arr.add(new ArrayList<>());
			}
			
			st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine(), " ");
			for (int i = 0; i < n/2; i++) {
				arr.get(Integer.parseInt(st.nextToken())).add(Integer.parseInt(st.nextToken()));
				
			}
			
			sb.append(bfs(s)).append("\n");
		}
		System.out.println(sb);
	}
	
	private static int bfs(int start) {
		int[] visited = new int[101];
		
		Queue<Info> queue = new ArrayDeque<>();
		queue.add(new Info(start, 1));
		visited[start] = 1;
		while(!queue.isEmpty()) {
			Info info = queue.poll();
			for (int index : arr.get(info.idx)) {
				if (visited[index] != 0)	continue;
				queue.add(new Info(index, info.count+1));
				visited[index] = info.count+1;
			}
		}
		int max = 0;
		int result = -1;
		for (int i = 100; i > 0; i--) {
			if (visited[i] > max) {
				max = visited[i];
				result = i;
			}
		}
		return result;
	}
}