import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
	static int L, C;
	static char[] result;
	static char[] chars;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		L = sc.nextInt();
		C = sc.nextInt();
		
		chars = new char[C];
		for (int i = 0; i < C; i++) {
			chars[i] = sc.next().charAt(0);
		}
		Arrays.sort(chars);
		
		result = new char[L];
		combination(0, 0);
		
	}
	
	private static void combination(int cnt, int start) {
		if (cnt == L) {
			if (check(result))
				System.out.println(result);
			return;
		}
		for (int i = start; i < C; i++) {
			result[cnt] = chars[i];
			combination(cnt+1, i+1);
		}
	}
	
	private static boolean check(char[] word) {
		
		int cnt = 0;
		for (char c : word) {
			if ("aeiou".contains(String.valueOf(c))) {
				cnt++;
			}
		}
		if (cnt >= 1 && L-cnt >=2)
			return true;
		
		return false;
	}
}