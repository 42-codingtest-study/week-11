import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ11576 {

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stBase = new StringTokenizer(br.readLine());

        int fromBase = Integer.parseInt(stBase.nextToken());
        int toBase = Integer.parseInt(stBase.nextToken());
        int numLength = Integer.parseInt(br.readLine());

        int decNum = fromBasetoDecimal(br, fromBase, numLength);
        Stack<Integer> stack = DecimalToBase(toBase, decNum);

        printResult(stack);
    }

    private static void printResult(Stack<Integer> stack) {
        StringBuilder sb = new StringBuilder();

        while (!stack.isEmpty()) {
            sb.append(stack.pop()).append(" ");
        }

        System.out.println(sb);
    }

    private static Stack<Integer> DecimalToBase(int toBase, int decNum) {
        Stack<Integer> stack = new Stack<>();

        while (decNum != 0) {
            stack.add(decNum % toBase);
            decNum /= toBase;
        }
        return stack;
    }

    private static int fromBasetoDecimal(BufferedReader br, int fromBase, int numLength)
        throws IOException {
        StringTokenizer stNum = new StringTokenizer(br.readLine());
        int decNum = 0;

        for (int i = numLength - 1; i >= 0; i--){
            decNum += Integer.parseInt(stNum.nextToken()) * (int)Math.pow(fromBase, i);
        }
        return decNum;
    }

    public static void main(String[] args) throws IOException {
        new BOJ11576().solution();
    }

}
