import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

	static Integer[] parents;
	static boolean[] isSelected;
	static int N;
	static int[] p;
	static int[][] arr;
	static int result = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		parents = new Integer[N];
		isSelected = new boolean[N];

		p = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		arr = new int[N][];
		for (int i = 0; i < N; i++) {
			arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		subset(0);
		System.out.println(result == Integer.MAX_VALUE ? -1 : result);
	}

	static void makeSet(int v) {
		for (int i = 0; i < v; i++) {
			parents[i] = i;
		}
	}

	static int findSet(int v) {
		if (v == parents[v])
			return v;
		return parents[v] = findSet(parents[v]);
	}

	static void union(int a, int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);

		if (aRoot < bRoot)
			parents[bRoot] = aRoot;
		else
			parents[aRoot] = bRoot;
	}

	public static void subset(int cnt) {
		if (cnt == N) {
			makeSet(N);
			for (int i = 0; i < N; i++) {
				if (isSelected[i]) {
					for (int j = 1, size = arr[i][0]; j <= size; j++) {
						if (isSelected[arr[i][j] - 1])
							union(i, arr[i][j] - 1);
					}
				} else {
					for (int j = 1, size = arr[i][0]; j <= size; j++) {
						if (!isSelected[arr[i][j] - 1])
							union(i, arr[i][j] - 1);
					}
				}
			}
			check();
			return;
		}
		isSelected[cnt] = true;
		subset(cnt + 1);
		isSelected[cnt] = false;
		subset(cnt + 1);
	}

	private static void check() {
//		Set<Integer> set = new HashSet<>(Arrays.asList(parents));
		Set<Integer> set = new HashSet<>();
		for (int i = 0; i<N; i++) {
			set.add(findSet(i));
		}

		if (set.size() == 2) {
			int a = 0, b = 0;
			int flag = parents[0];
			for (int i = 0; i < N; i++) {
				if (parents[i] == flag)
					a += p[i];
				else
					b += p[i];
			}
			result = Math.min(result, Math.abs(a - b));
		}
	}
}