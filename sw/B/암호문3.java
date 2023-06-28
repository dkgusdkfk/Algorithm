package lab1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 암호문3 {
	
	static ArrayList<Integer> list;
	static StringTokenizer st;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#" + tc);
			
			list = new ArrayList<>();
			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			for (int i = 0; i < N; i++) {
				list.add(Integer.parseInt(st.nextToken()));
			}
			
			int Q = Integer.parseInt(br.readLine());
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < Q; i++) {
				char cmd = st.nextToken().charAt(0);
				int x = Integer.parseInt(st.nextToken());
				func(cmd, x);
			}
			
			for (int i = 0; i < 10; i++) {
				sb.append(" " + list.get(i));
			}
			sb.append("\n");
		}
		System.out.println(sb);
		br.close();
	}
	
	private static void func(char cmd, int x) {
		int y;
		switch(cmd) {
			case 'I':
				y = Integer.parseInt(st.nextToken());
				for (int i = 0, insertIdx = x; i < y; i++, insertIdx++) {
	                list.add(insertIdx, Integer.parseInt(st.nextToken()));
	            }
	            break;
	        case 'D':
	            y = Integer.parseInt(st.nextToken());
	            for(int i=0; i<y; i++)
	                list.remove(x);
	            break;
	
	        case 'A':
	            for(int i=0; i<x; i++) {
	                list.add(Integer.parseInt(st.nextToken()));
	            }
	            break;
	    }
	}
}
