import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static ArrayList<ArrayList<QueueNode>> graph = new ArrayList<>();
	static int[] distance;
	
	static class QueueNode implements Comparable<QueueNode> {

	    private int index;
	    private int distance;

	    public QueueNode(int index, int distance) {
	        this.index = index;
	        this.distance = distance;
	    }

	    @Override
	    public int compareTo(QueueNode other) {
	        if (this.distance < other.distance) {
	            return -1;
	        }
	        return 1;
	    }
	}
	
	public static void main(String[] args) throws IOException {
		final int INF = Integer.MAX_VALUE;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		int start = Integer.parseInt(br.readLine());

		for (int i = 0; i <= V; i++) {
            graph.add(new ArrayList<QueueNode>());
        }
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			graph.get(a).add(new QueueNode(b, c));
		}

		distance = new int[V + 1];
		Arrays.fill(distance, INF);
		
		dijkstra(start);
		for (int i = 1; i <= V; i++) {
			System.out.println(distance[i] != INF? distance[i] : "INF");
		}
	}
	
	private static void dijkstra(int start) {
        PriorityQueue<QueueNode> queue = new PriorityQueue<>();

        queue.offer(new QueueNode(start, 0));
        distance[start] = 0;

        while(!queue.isEmpty()) {
            QueueNode node = queue.poll();

            int dist = node.distance;
            int now = node.index;

            if (distance[now] < dist) {
                continue;
            }

            for (int i = 0; i < graph.get(now).size(); i++) {
                int cost = distance[now] + graph.get(now).get(i).distance;

                if (cost < distance[graph.get(now).get(i).index]) {
                	distance[graph.get(now).get(i).index] = cost;
                    queue.offer(new QueueNode(graph.get(now).get(i).index, cost));
                }
            }
        }
	}
}