import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.StringTokenizer;

public class 프로세서연결하기 {
	
	static int[] dx = {-1, 0, 0, 1};
	static int[] dy = {0, -1, 1, 0};
	
	static int result = Integer.MAX_VALUE;
	static int coreCount = 0;

	static List<Core> coreList;
	
	static class Core {
		int x, y;
		public Core(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			int n = Integer.parseInt(br.readLine());
		
			int[][] map = new int[n+2][n+2];
			for (int i = 1; i <= n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if (map[i][j] == 1) {
						if (i == 1 || j == 1 || i == n || j == n)	continue;
						coreList.add(new Core(i, j));
					}
				}
			}
			
			
			
		}
	}
	
	private static void go(int[][] map, int idx, int count, int coreCnt) {
		if (idx == coreList.size()) {
			if (coreCount == coreCnt) {
				result = Math.min(result, count);
			} else if (coreCount < coreCnt) {
				result = count;
				coreCount = coreCnt;
			}
		}
		
		
		
	}
	
	private static void move(int[][] map, int x, int y, int d) {
		
		
		
	}
	
}
