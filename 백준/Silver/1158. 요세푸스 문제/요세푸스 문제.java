import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		LinkedList<Integer> li = new LinkedList<>();
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			li.add(i);
		}
		
		int idx = k-1;
		sb.append("<").append(li.get(idx));
		li.remove(idx);
		for (int i = 1; i < n; i++) {
			idx = (idx+k-1)%li.size();
			sb.append(", ").append(li.get(idx));
			li.remove(idx);
		}
		sb.append(">");
		System.out.println(sb);
	}
}