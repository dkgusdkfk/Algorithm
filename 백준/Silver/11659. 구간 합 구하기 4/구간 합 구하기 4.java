import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder stringBuilder = new StringBuilder();
		String[] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);

		int[] numbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		int[] sumList = new int[n + 1];
		for (int k = 1; k <= n; k++) {
			sumList[k] = sumList[k - 1] + numbers[k - 1];
		}

		for (int k = 0; k < m; k++) {
			input = br.readLine().split(" ");
			int i = Integer.parseInt(input[0]);
			int j = Integer.parseInt(input[1]);
			stringBuilder.append(sumList[j] - sumList[i - 1]).append("\n");
		}

		System.out.println(stringBuilder);
	}
}
