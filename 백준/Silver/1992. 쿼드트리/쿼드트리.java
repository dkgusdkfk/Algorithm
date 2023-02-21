import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static char[][] arr;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		
		arr = new char[N][N];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			arr[i] = str.toCharArray();
		}
		cut(0, 0, N);
		System.out.println(sb);
	}
	
	static void cut(int r, int c, int size) {

		int sum = 0;
		for (int i = r, rEnd = r + size; i < rEnd; i++) {
			for (int j = c, cEnd = c + size; j < cEnd; j++) {
				sum += arr[i][j]-'0';
			}
		}

		if (sum == size * size) { // 모두 1
			sb.append(1);
		} else if (sum == 0) { // 모두 0
			sb.append(0);
		} else { // 혼합된 상황
			// 4분할
			sb.append("(");
			int half = size / 2;
			cut(r, c, half);
			cut(r, c + half, half);
			cut(r + half, c, half);
			cut(r + half, c + half, half);
			sb.append(")");
		}

	}
}