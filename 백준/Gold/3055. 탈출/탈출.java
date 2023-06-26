import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Main {

	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int R, C, result = 0;
	static char[][] map;
	static boolean[][] visited;
	static Queue<Info> queue2;

	static class Info {
		int x, y;

		Info(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] input = br.readLine().split(" ");
		R = Integer.parseInt(input[0]);
		C = Integer.parseInt(input[1]);

		Queue<Info> queue = new ArrayDeque<>();
		queue2 = new ArrayDeque<>();

		visited = new boolean[R + 2][C + 2];

		map = new char[R + 2][C + 2];
		for (int i = 1; i <= R; i++) {
			String str = br.readLine();
			for (int j = 1; j <= C; j++) {
				map[i][j] = str.charAt(j - 1);
				if (map[i][j] == 'S') {
					map[i][j] = '.';
					visited[i][j] = true;
					queue.add(new Info(i, j));
				} else if (map[i][j] == '*') {
					queue2.add(new Info(i, j));
				}
			}
		}

		while (queue.size() != 0) {
			result++;
			int s = queue.size();
			int qSize = queue2.size();
			while (qSize-- > 0) {
				water();
			}

			while (s-- > 0) {
				int x = queue.peek().x;
				int y = queue.poll().y;
				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];
					if (visited[nx][ny])	continue;
					visited[nx][ny] = true;
					if (map[nx][ny] == 'D') {
						System.out.println(result);
						System.exit(0);
					}
					if (map[nx][ny] == '.') {
						queue.add(new Info(nx, ny));
					}
				}
			}
		}
		System.out.println("KAKTUS");
	}

	private static void water() {
		int x = queue2.peek().x, y = queue2.poll().y;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (map[nx][ny] == '.') {
				map[nx][ny] = '*';
				queue2.add(new Info(nx, ny));
			}
		}
	}
}