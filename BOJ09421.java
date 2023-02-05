import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class BOJ09421 {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        int[] arr = new int[n + 1];
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (arr[i] == 0) {
                list.add(i);
                for (int j = i; j <= n; j += i) {
                    arr[j]++;
                }
            }
        }

        for (int i = 0; i < list.size(); i++) {
            int tmp = list.get(i);
            HashSet<Integer> set = new HashSet<>();
            while (set.add(tmp)) {
                int ssum = 0;
                while (tmp > 0) {
                    int remainer = tmp % 10;
                    ssum += remainer * remainer;
                    tmp /= 10;
                }
                if (ssum == 1) {
                    System.out.println(list.get(i));
                } else {
                    tmp = ssum;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new BOJ09421().solution();
    }
}