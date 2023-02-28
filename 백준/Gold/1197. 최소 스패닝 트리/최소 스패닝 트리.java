import java.util.Arrays;
import java.util.Scanner;

/** 크루스칼 알고리즘
 * 시간 복잡도
 * 1. makeSet		=> O(V)
 * 2. Edge 정렬		=> O(ElogE)
 * 3. union			=> O(E)
 *
 * O(V+ElogE+E) ==> O(ElogE)	PQ : O(VlogE)	간선이 적으면 크루스칼 간선이 많으면 프림(간적크간많프)
 */
public class Main {
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
	
	static int V, E;
	static Edge[] edgeList;
	static int[] parents;
	
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
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		V = sc.nextInt();
		E = sc.nextInt();
		
		edgeList = new Edge[E];
		
		for (int i = 0; i < E; i++) {
			edgeList[i] = new Edge(sc.nextInt()-1, sc.nextInt()-1, sc.nextInt());
		}
		
		Arrays.sort(edgeList);
		
		makeSet();
		int result = 0, count = 0;
		
		for (Edge edge : edgeList) {
			if (union(edge.from, edge.to)) {
				result += edge.weight;
				if(++count == V-1)	break;
			}
		}
		System.out.println(result);
	}
}