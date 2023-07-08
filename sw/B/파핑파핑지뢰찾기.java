import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class 파핑파핑지뢰찾기 {

    static char[][] map;
    static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
    static int[] dy = {0, 0, -1, 1, 1, -1, -1, 1};

    static class Info {
        int x, y;

        Info(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {
            sb.append("#" + tc + " ");

            int n = sc.nextInt();

            map = new char[n + 2][n + 2];
            for (int i = 1; i <= n; i++) {
                String input = sc.next();
                for (int j = 1; j <= n; j++) {
                    map[i][j] = input.charAt(j - 1);
                }
            }

            int click_count = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (map[i][j] == '.' && isZero(i, j)) {
                        click(i, j);
                        click_count++;
                    }
                }
            }

            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (map[i][j] == '.')
                        click_count++;
                }
            }

            sb.append(click_count).append("\n");
        }
        
        System.out.println(sb);
    }

    private static void click(int r, int c) {
        Queue<Info> queue = new ArrayDeque<>();
        queue.add(new Info(r, c));

        while (!queue.isEmpty()) {
            int x = queue.peek().x;
            int y = queue.poll().y;
            map[x][y] = 'x';
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (map[nx][ny] == ' ') continue;
                if (map[nx][ny] == '.' && isZero(nx, ny)) {
                    queue.add(new Info(nx, ny));
                } else {
                    map[nx][ny] = 'x';
                }
            }
        }
    }

    private static boolean isZero(int x, int y) {
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (map[nx][ny] == '*')
                return false;
        }
        return true;
    }
}