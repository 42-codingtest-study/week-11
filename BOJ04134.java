import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

/**
 * java 의 BigInteger 를 활용해보자
 * BigInteger.isProbablePrime()
 * BigInteger.nextProbablePrime()
 */

public class BOJ04134 {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++){
            BigInteger num = new BigInteger(br.readLine());
            if (num.isProbablePrime(10)) {
                System.out.println(num);
            } else {
                System.out.println(num.nextProbablePrime());
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new BOJ04134().solution();
    }
}
