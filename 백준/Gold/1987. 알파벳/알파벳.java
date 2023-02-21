import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int R, C;
	static boolean[] a;
	static String[] arr;
	static int max;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		R = Integer.parseInt(s[0]);
		C = Integer.parseInt(s[1]);
		
		arr = new String[R];
		for (int i = 0; i < R; i++) {
			arr[i] = br.readLine();
		}
		
		a = new boolean[26];
		dfs(0,0,0);
		System.out.println(max);
		
	}
	
	private static void dfs(int r, int c, int cnt) {
		if (!(0 <= r && r < R && 0 <= c && c < C))	return;
		int idx = arr[r].charAt(c)-'A';
		if (a[idx])	{
			max = Math.max(max, cnt);
			return;
		}
		cnt++;
		a[idx] = true;
		dfs(r, c+1, cnt);
		dfs(r+1, c, cnt);
		dfs(r, c-1, cnt);
		dfs(r-1, c, cnt);
		a[idx] = false;
	}
}