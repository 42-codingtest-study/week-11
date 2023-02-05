import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * [최소공배수 구하기]
 * 유클리드 호제법을 통해 최대공약수를 구한다
 * 최대공약수를 통해 최소공배수를 구한다 (a * b) / gcd
 */

public class BOJ13241 {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Integer.parseInt(st.nextToken());
        long b = Integer.parseInt(st.nextToken());

        long gcd;
        long lcd;

        if (a > b)
            gcd = getGcd(a, b);
        else
            gcd = getGcd(b, a);

        lcd = (a * b) / gcd;    // 최소공배수
        System.out.println(lcd);
    }

    private long getGcd(long num1, long num2){
        long tmp;
        while (num2 != 0) {
            tmp = num2;
            num2 = num1 % num2;
            num1 = tmp;
        }
        return num1;
    }

    public static void main(String[] args) throws IOException {
        new BOJ13241().solution();
    }
}
