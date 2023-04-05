import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int d = sc.nextInt();
		int k = sc.nextInt();
		int c = sc.nextInt();
		
		int[] arr = new int[N];
		for (int n = 0; n < N; n++) {
			arr[n] = sc.nextInt();
		}
		
		int[] check = new int[d+1];
		int count = 0;
		for (int i = 0; i < k; i++) {
			if (check[arr[i]]++ == 0)
				count++;
		}
		
		int result = count;
		if (check[c] == 0)
			result++;
		
		for (int i = k; i < k+N; i++) {
			if (check[arr[i-k]]-- == 1)
				count--;
			if (check[arr[i%N]]++ == 0)
				count++;
			if (check[c] == 0)
				result = Math.max(result, count+1);
			else
				result = Math.max(result, count);
		}
		
		System.out.println(result);
	}
}