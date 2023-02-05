import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 일반적인 최대공약수 구하는 문제와는 다르다
 *
 * 500000000000000000 500000000000000002 의 경우
 * 시간 초과가 발생한다
 *
 * [해결]
 * A와 B에 최대공약수를 구하고 결과 수만큼 1에 1자리만큼 추가한다
 *
 * 여러 케이스를 확인하며 규칙을 구하는 문제
 *
 * [시간 초과]
 * 생각보다 print()가 느리다는 걸 알게되었다 -> sb 후 println
 */
public class BOJ01850 {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long test =  a > b ? getGcd(a, b) : getGcd(b, a);

        System.out.println(getResult(test));
    }

    private static StringBuilder getResult(long length) {
        StringBuilder sb = new StringBuilder();
        while (length-- != 0) {
            sb.append("1");
        }
        return sb;
    }

    private static long getGcd(long num1, long num2){
        return num2 != 0 ? getGcd(num2, num1 % num2) : num1;
    }

    public static void main(String[] args) throws IOException {
        new BOJ01850().solution();
    }
}
