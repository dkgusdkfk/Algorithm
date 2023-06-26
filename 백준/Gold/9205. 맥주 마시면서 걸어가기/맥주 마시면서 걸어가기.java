import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	
    static int n;
    static Pos arr[];    
	
    static class Pos {
        int x, y;
        boolean check = false;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static boolean bfs() {
    	Queue<Pos> q = new ArrayDeque<>();
        q.add(arr[0]);
        while (!q.isEmpty()) {
            int x = q.peek().x, y = q.poll().y;
            for (int i=0;i< arr.length;i++) {
                int nx = arr[i].x, ny = arr[i].y;
                int dist = Math.abs(nx - x) + Math.abs(ny - y);
                if (dist > 1000 || arr[i].check) continue;
                if (nx == arr[n+1].x && ny == arr[n+1].y) return true;
                q.add(new Pos(nx, ny));
                arr[i].check = true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	
    	int T = Integer.parseInt(br.readLine());
    	for (int t = 0; t < T; t++) {
    		n = Integer.parseInt(br.readLine());
            arr = new Pos[n + 2];

            st = new StringTokenizer(br.readLine());
            arr[0] = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            for (int i = 1; i < n+1; i++) {
                st = new StringTokenizer(br.readLine());
                arr[i] = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            st = new StringTokenizer(br.readLine());
            arr[n+1] = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            
            if (bfs()) System.out.println("happy");
            else System.out.println("sad");
		}
    }
}