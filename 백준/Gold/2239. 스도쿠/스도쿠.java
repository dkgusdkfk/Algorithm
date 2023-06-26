import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {
	
	static int[][] board;
	static List<int[]> arr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		board = new int[9][9];
		arr = new LinkedList<>();
		for (int i = 0; i < 9; i++) {
			String str = br.readLine();
			for (int j = 0; j < 9; j++) {
				board[i][j] = str.charAt(j) - '0';
				if (board[i][j] == 0)
					arr.add(new int[] {i, j});
			}
		}
		solution(0);
	}
	
	private static void solution(int cnt) {
		if (cnt == arr.size()) {
			for (int[] b : board) {
				for (int k : b) {
					sb.append(k);
				}
				sb.append('\n');
			}
			System.out.println(sb);
			System.exit(0);
			return;
		}
		
		int[] a = arr.get(cnt);
		for (int i = 1; i <= 9 ; i++) {
			if (!check(a[0], a[1], i))	continue;
			board[a[0]][a[1]] = i;
			solution(cnt + 1);
			board[a[0]][a[1]] = 0;
		}
	}
	
	private static boolean check(int r, int c, int k) {
		for (int i = 0; i < 9; i++) {
			if (board[r][i] == k)
				return false;
			if (board[i][c] == k)
				return false;
		}
		for (int i = r/3*3, e1 = r/3*3+3; i < e1; i++) {
			for (int j = c/3*3, e2 = c/3*3+3; j < e2; j++) {
				if (board[i][j] == k)
					return false;
			}
		}
		return true;
	}
}