import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Queue;
import java.util.Scanner;

public class 파핑파핑지뢰찾기 {
	
	static char[][] map;
	static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
	static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
//	static int[] dx = {-1, 0, 0, 1};
//	static int[] dy = {0, -1, 1, 0};
	
	static class Info {
		int x, y;
		Info(int x, int y) {
			this.x = x;
			this.y = y;
		}
		
		@Override
		public String toString() {
			return (x + " " + y);
		}
	}
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			
			int n = sc.nextInt();
			
			map = new char[n+2][n+2];
			for (int i = 1; i <= n; i++) {
				String input = sc.next();
				for (int j = 1; j <= n; j++) {
					map[i][j] = input.charAt(j-1);
				}
			}
			
			int click = 0;
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if (map[i][j] == '.') {
						check(i, j);
						click++;
					}
				}
			}
			sb.append(click).append("\n");
		}
		System.out.println(sb);
	}
	
	private static void check(int r, int c) {
		Queue<Info> queue = new ArrayDeque<>();
		queue.add(new Info(r, c));
		
		Queue<Info> temp = new ArrayDeque<>();
		while(!queue.isEmpty()) {
			System.out.println(queue);
			int x = queue.peek().x;
			int y = queue.poll().y;
			int count = 0;
			for (int i = 0; i < 8; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (map[nx][ny] == '*') {
					count++;
				} else if (map[nx][ny] == '.') {
					temp.add(new Info(nx, ny));
				}
			}
			if (count == 0) {
				queue.addAll(temp);
			} else {
				temp.clear();
			}
			map[x][y] = (char) count;
		}
	}
}
