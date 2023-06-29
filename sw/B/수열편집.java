package lab1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class 수열편집 {
	static StringTokenizer st;
	static List<Integer> list;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc + " ");
			
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			
			list = new LinkedList<>();
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				char advice = st.nextToken().charAt(0);
				func(advice);
			}
			if (list.size() > L)
				sb.append(list.get(L));
			else
				sb.append(-1);
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	private static void func(char advice) {
		int idx = Integer.parseInt(st.nextToken());
		if (list.size() <= idx) return;
		
		switch(advice) {
		case 'I':
			int num = Integer.parseInt(st.nextToken());
			list.add(idx, num);
			break;
		case 'D':
			list.remove(idx);
			break;
		case 'C':
			num = Integer.parseInt(st.nextToken());
			list.set(idx, num);
		}
	}
}
