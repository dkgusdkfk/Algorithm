import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Collections;
import java.util.Deque;
import java.util.Set;
import java.util.TreeSet;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			String[] nk = br.readLine().split(" ");
			int N = Integer.parseInt(nk[0]);
			int K = Integer.parseInt(nk[1]);
			char[] num = br.readLine().toCharArray();
			Deque<Character> deque = new ArrayDeque<Character>();
			for (char n : num) {
				deque.add(n);
			}
			
			int l = N / 4;
			Set<String> set = new TreeSet<>(Collections.reverseOrder());
			int j = 1;
			StringBuilder sbr = new StringBuilder();
			for (int i = 0; i < l; i++) {				
				for (Character c : deque) {
					sbr.append(c);
					if (j%l == 0) {
						set.add(sbr.toString());
						sbr = new StringBuilder();
					}
					j++;
				}
				deque.addFirst(deque.pollLast());
			}
			String[] arr = set.toArray(new String[set.size()]);
			sb.append(Integer.parseInt(arr[K-1], 16)).append("\n");
		}
		System.out.println(sb);
	}
}