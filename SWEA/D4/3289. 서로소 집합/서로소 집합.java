import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static int[] parents;
	
	private static void makeSet(int v) {
		parents[v] = v;
	}
	
	private static int findSet(int v) {
		if (v == parents[v])	return v;
		return parents[v] = findSet(parents[v]);
	}
	
	private static void union(int u, int v) {
		parents[findSet(u)] = findSet(v);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			parents = new int[n+1];
			for (int i = 1; i < n; i++) {
				makeSet(i);
			}			
			
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int k = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (k == 0) {
					union(a, b);
				} else {
					if (findSet(a) == findSet(b)) {
						sb.append(1);
					} else {
						sb.append(0);
					}
				}
				
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}