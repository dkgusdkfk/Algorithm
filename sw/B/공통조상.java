package lab2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 공통조상 {
	
	static int ans, V, E, A, B;
	static Node[] nodes;
	static ArrayList<Integer> ancestorA, ancestorB;
	
	static class Node {
		List<Integer> children;
		int parents;
		
		Node() {
			this.children = new ArrayList<>();
			this.parents = 0;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			
			nodes = new Node[V+1];
			ancestorA = new ArrayList<>();
			ancestorB = new ArrayList<>();
			
			for (int i = 0; i < V+1; i++) {
				nodes[i] = new Node();
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				int p = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				nodes[p].children.add(c);
				nodes[c].parents = p;
			}
			
			traverse(A, ancestorA);
			traverse(B, ancestorB);
			
			for (int i = 0; i < V; i++) {
				if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
				ans = ancestorA.get(i);
			}
			

			sb.append(ans).append(" ").append(dfs(ans)).append("\n");
		}
		System.out.println(sb);
	}
	
	private static void traverse(int idx, ArrayList<Integer> ancestor) {
		int parent = nodes[idx].parents;
		if (parent != 0) {
			traverse(parent, ancestor);
		}
		ancestor.add(idx);
	}
	
	private static int dfs(int idx) {
		int res = 1;
		for (int child : nodes[idx].children) {
			res += dfs(child);
		}
		return res;
	}
}
