import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		ArrayList<String> op = new ArrayList<>(Arrays.asList("+", "-", "*", "/"));

		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#" + tc + " ");
			int n = Integer.parseInt(bf.readLine());
			int result = 1;
			int i = 0;
			for (i = 0; i < n; i++) {
				String[] s = bf.readLine().split(" ");
				if (s.length == 4) {
					if (!op.contains(s[1]))
						break;
				} else if (s.length == 2) {
					if (op.contains(s[1]))
						break;
				} else
					break;
			}
			for (int j = i + 1; j < n; j++) {
				result = 0;
				bf.readLine();
			}
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}
}