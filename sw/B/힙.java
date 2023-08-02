package lab3;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class 힙 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			sb.append("#" + t + " ");
			PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
			
			int n = sc.nextInt();
			for (int i = 0; i < n; i++) {
				switch (sc.nextInt()) {
				case 1:
					int x = sc.nextInt();
					priorityQueue.add(x);
					break;
				case 2:
					if (priorityQueue.isEmpty())
						sb.append(-1);
					else
						sb.append(priorityQueue.poll());
					sb.append(" ");
					break;
				}
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
