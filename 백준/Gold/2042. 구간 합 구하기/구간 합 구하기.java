import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N;
	static long[] tree;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		tree = new long[N+1];
		long[] nums = new long[N+1];
		for (int i = 1; i <= N; i++) {
			nums[i] = Long.parseLong(br.readLine());
			update(i, nums[i]);
		}
		
		for (int i = 0; i < M+K; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			long c = Long.parseLong(st.nextToken());
			
			if (a == 1) {
				update(b, c - nums[b]);
				nums[b] = c;
			} else if (a == 2) {
				sb.append(sum((int) c) - sum(b-1)).append("\n");
			}
		}
		System.out.println(sb);
	}
	
	public static void update(int i, long num) {
		while (i<=N) {
			tree[i] += num;
			i += (i & -i);		// 다음 위치에 데이터를 update  =>  index+k
		}
	}
	
	public static long sum(int i) {
		long ans = 0;
		while (i > 0) {
			ans += tree[i];
			i -= (i & -i);		// 이전 구간의 합이 있는 위치로 이동	이전 구간합이 있는 위치 => index-k
		}
		return ans;
	}
}