import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int[][] arr;		// 검은 스카프 여부 배열
	static int result;		// 둘레 길이

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());	// 검은 스카프의 수

		arr = new int[100][100];	// 검은 스카프 여부 배열
		for (int n = 0; n < N; n++) {	// N개의 검은 스카프 입력
			StringTokenizer st = new StringTokenizer(br.readLine());	// 검은 스카프 입력
			int a = Integer.parseInt(st.nextToken());	// 검은색 스카프의 왼쪽 변과 흰색 천의 왼쪽 변 사이의 거리
			int b = Integer.parseInt(st.nextToken());	// 검은색 스카프의 아래쪽 변과 흰색 천의 아래쪽 변 사이의 거리
			for (int i = 0; i < 10; i++) {	// 검은 스카프 세로 길이 만큼 반복
				for (int j = 0; j < 10; j++) {	// 검은 스카프 가로 길이 만큼 반복
					arr[a + i][b + j] = 1;	// 검은 스카프가 존재하기 때문에 1로 변경
				}
			}
		}

		for (int i = 0; i < 100; i++) {		// 흰색 천 세로 길이 만큼 반복
			for (int j = 0; j < 100; j++) {	// 흰색 천 가로 길이 만큼 반복
				if (arr[i][j] == 1) {	//검은 스카프가 존재할 경우
					check(i, j);	// 둘레인지 체크
				}
			}
		}
		System.out.println(result);	// 둘레 길이 프린트
	}

	private static void check(int r, int c) {
		int[] dx = { 1, 0, -1, 0 };	// (상, 우, 하, 좌) 행 배열
		int[] dy = { 0, 1, 0, -1 };	// (상, 우, 하, 좌) 열 배열

		int cnt = 0;	// 꼭짓점인지 체크하기 위한 cnt
		for (int i = 0; i < 4; i++) {	// 상하좌우 4방향 확인
			int mx = r + dx[i];
			int my = c + dy[i];
			if (!(0 <= mx && mx < 100 && 0 <= my && my < 100)) {	// 흰색 천 밖일 경우
				cnt++;	// 둘레에 포함되므로 cnt++
			} else if (arr[mx][my] == 0) {	// 검은 스카프가 포함되지 않은 부분이 있는 경우
				cnt++;	// 둘레에 포함되므로 cnt++
			}
		}
		if (cnt == 2)	// cnt가 2인경우 꼭짓점
			result += 2;	// 꼭짓점의 경우 둘레에 2번 포함되므로 +2
		else if (cnt > 0)	// cnt > 0인 경우 둘레에 포함
			result++;	// 둘레에 추가
		return;
	}
}