import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 영준이의진짜BFS {
	
	static int ans;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[] arr = new int[n+1];
			
			st = new StringTokenizer(br.readLine());
			for (int i = 2; i <= n; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				check(arr[i]);
			}
		}
	}
	
	private static void check(int c) {
		
	}
}
