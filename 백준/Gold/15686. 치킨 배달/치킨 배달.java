import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static int[] cList;
	static List<int[]> house;
	static List<int[]> store;
	static int result = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		house = new ArrayList<int[]>();
		store = new ArrayList<int[]>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int k = Integer.parseInt(st.nextToken());
				if (k == 1) {
					house.add(new int[] { i, j });
				} else if (k == 2) { 
					store.add(new int[] { i, j });
				}
			}
		}
		cList = new int[M];
		combi(0, 0);
		System.out.println(result);
	}

	public static void combi(int cnt, int start) {
		if (cnt == M) {
			solution();
			return;
		}
		for (int i = start, size = store.size(); i < size; i++) {
			cList[cnt] = i;
			combi(cnt + 1, i + 1);
		}
	}

	public static void solution() {
		int sum = 0;
		for (int i = 0, size = house.size(); i < size; i++) {
			int[] h = house.get(i);
			int hsum = Integer.MAX_VALUE;
			for (int j = 0 ; j < M; j++) {
				int[] s = store.get(cList[j]);
				hsum = Math.min(hsum, Math.abs(h[0] - s[0]) + Math.abs(h[1] - s[1]));
			}
			sum += hsum;
		}
		result = Math.min(result, sum);
	}
}