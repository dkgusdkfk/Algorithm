import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N = 10;
	static int[] cnt = new int[6];
	static int[][] map;
	static int result = Integer.MAX_VALUE;
	static int count;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 1)
					count++;
			}
		}
		
		solution(0, 0, 0);
		
		System.out.println(result == Integer.MAX_VALUE? -1 : result);
	}
	
	private static void solution(int x, int y, int d) {
		if (count == 0) {
			result = Math.min(result, d);
		}
		if (y == N) {
			y = 0;
			x++;
		}
		if (x == N)
			return;
		if (map[x][y] == 0)	{
			solution(x, y+1, d);
			return;
		}
		for (int i = 5; i > 0 ; i--) {
			if (check(x, y, i)) {
				go(x, y, i);
				cnt[i]++;
				count -= i*i;
				solution(x, y+1, d+1);
				count += i*i;
				cnt[i]--;
				back(x, y, i);
			}
		}
	}
	
	private static boolean check(int r, int c, int k) {
		if (cnt[k] >= 5)	return false;
		for (int i = 0; i < k; i++) {
			int nr = r + i;
			for (int j = 0; j < k; j++) {
				int nc = c + j;
				if (nr < 0 || nr >= N || nc < 0 || nc >= N || map[nr][nc] == 0)	return false;
			}
		}
		return true;
	}
	
	private static void go(int r, int c, int k) {
		for (int i = 0; i < k; i++) {
			int nr = r + i;
			for (int j = 0; j < k; j++) {
				int nc = c + j;
				map[nr][nc] = 0;
			}
		}
	}
	
	private static void back(int r, int c, int k) {
		for (int i = 0; i < k; i++) {
			int nr = r + i;
			for (int j = 0; j < k; j++) {
				int nc = c + j;
				map[nr][nc] = 1;
			}
		}
	}
}