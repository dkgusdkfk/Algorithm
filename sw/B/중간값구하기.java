package lab3;

import java.util.PriorityQueue;
import java.util.Scanner;

public class 중간값구하기 {
	
	private static final int MOD = 20171109;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		int T = sc.nextInt();
		for (int t = 1; t <= T; t++) {
			sb.append("#" + t + " ");
			
			PriorityQueue<Integer> minH = new PriorityQueue<>((i1, i2) -> i1 - i2);
			PriorityQueue<Integer> maxH = new PriorityQueue<>((i1, i2) -> i2 - i1);
			
			int n = sc.nextInt();
			int a = sc.nextInt();
			
			minH.add(a);
			int answer = 0;
			for (int i = 0; i < n; i++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				
				if (x > y) {
					minH.add(x);
					maxH.add(y);
				} else {
					minH.add(y);
					maxH.add(x);
				}
				
				while (minH.peek() < maxH.peek()) {
					int minVal = minH.poll();
					int maxVal = maxH.poll();
					minH.add(maxVal);
					maxH.add(minVal);
				}
				
				answer = (minH.peek() + answer) % MOD;
			}
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
