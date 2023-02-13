import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int n = Integer.parseInt(bf.readLine());

		Stack<Integer> stack = new Stack<>();
		int[] arr = new int[n];
		StringTokenizer st = new StringTokenizer(bf.readLine());
		for (int i = 0; i < n; i++) {
			int result = 0;
			arr[i] = Integer.parseInt(st.nextToken());
			while (!stack.isEmpty()) {
				int idx = stack.pop();
				if (arr[idx] > arr[i]) {
					stack.add(idx);
					result = idx + 1;
					break;
				}
			}
			stack.add(i);
			sb.append(result).append(" ");
		}
		System.out.println(sb);
	}
}