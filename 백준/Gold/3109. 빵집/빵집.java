import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int R, C;
	static char[][] arr;
	static int[] dx = {-1, 0, 1};
	static int[] dy = {1, 1, 1};
	static int result;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		arr = new char[R][C];
		for (int i = 0; i < R; i++) {
			arr[i] = br.readLine().toCharArray();
		}
		
		for (int i = 0; i < R; i++) {
			solution(i, 0);
		}
		
		System.out.println(result);
	}

	private static boolean solution(int r, int c) {
		if (c == C-1) {
			result++;
			return true;
		}
		for (int i = 0; i < 3; i++) {
			int mx = r + dx[i];
			int my = c + dy[i];
			if (!(0<=mx && mx <R && 0 <= my && my<C))	continue;
			if (arr[mx][my] == 'x')	continue;

			arr[mx][my] = 'x';
			if (solution(mx, my))
				return true;
		}
		return false;
	}
	
}