import java.util.Scanner;

public class BOJ10166 {

    static boolean View[][] = new boolean[2001][2001]; // 2 / 6 == 1 / 3

    public void solution() {
        Scanner sc = new Scanner(System.in);
        int D1 = sc.nextInt();
        int D2 = sc.nextInt();
        long ans = 0;
        for (int i = D1; i <= D2; i++) {

            for (int j = 1; j <= i; j++) {
                int gcd = GCD(i, j);
                if (View[i / gcd][j / gcd])
                    continue;
                ans++;
                View[i / gcd][j / gcd] = true;
            }
        }
        System.out.println(ans);
    }

    private int GCD(int a, int b) {
        while (b != 0) {
            int c = a % b;
            a = b;
            b = c;
        }
        return a;
    }
    public static void main(String[] args) {
        new BOJ10166().solution();
    }
}