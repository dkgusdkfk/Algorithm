//package hwalgo01_서울_13_백아현.com.ssafy.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int[][] arr;
	static int[][] copyArr;
	static int[] dx = { 1, 0, -1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static boolean[] isSelected;
	static int[] select;
	static int[][] c;
	static int n, m, k;
	static int result = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		arr = new int[n + 2][m + 2];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		c = new int[k][];
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			c[i] = new int[] { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken()) };
		}
		isSelected = new boolean[k];
		select = new int[k];
		permutation(0);

		System.out.println(result);
	}

	public static void permutation(int cnt) {
		if (cnt == k) {
			copyArr = new int[n + 2][m + 2];
			for (int i = 1; i <= n; i++) {
				copyArr[i] = arr[i].clone();
			}
			for (int i = 0; i < k; i++) {
				int[] value = c[select[i]];
				turn(value[0], value[1], value[2]);
			}
			int sum = Integer.MAX_VALUE;
			for (int i = 1; i <= n; i++) {
				sum = Math.min(sum, Arrays.stream(copyArr[i]).sum());
			}
			result = Math.min(result, sum);
			return;
		}
		for (int i = 0; i < k; i++) {
			if (isSelected[i])
				continue;
			select[cnt] = i;
			isSelected[i] = true;
			permutation(cnt + 1);
			isSelected[i] = false;
		}
	}

	public static void turn(int r, int c, int s) {
		int sr = r - s;
		int sc = c - s;
		int k = s * 2;
		int d = 0;
		while (k > 0) {
			int temp = copyArr[sr][sc]; // 시작 값
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < k; j++) {
					copyArr[sr][sc] = copyArr[sr + dx[d]][sc + dy[d]];
					sr += dx[d];
					sc += dy[d];
				}
				d = (d + 1) % 4;
			}
			copyArr[sr][sc + 1] = temp;
			k -= 2;
			sr++;
			sc++;
		}

	}
}