import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		if (n == 1) System.out.println(1);
		else {
			Queue<Integer> queue = new LinkedList<Integer>();
			
			for (int i = 2; i <= n; i+=2) {
				queue.offer(i);
			}
			if (n%2!=0)
				queue.offer(queue.poll());
			while (queue.size() > 1) {
				queue.remove();
				queue.offer(queue.poll());
			}
			System.out.println(queue.poll());
		}
	}
}