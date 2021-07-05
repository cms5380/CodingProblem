import java.util.*;

class Main {
    public static int solution(int[] leak, int L, int N) {
        Arrays.sort(leak);
        int ans = 0;

        for(int i = 0 ; i < N ; i++){
            int nxt = i+1;

            while(nxt < N && Math.abs(leak[i] - leak[nxt]) <= L - 1){
                nxt++;
            }
            ans++;
            i = nxt-1;

        }

        return ans;
    }



    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int L = input.nextInt();
        int[] leak = new int[N];

        for(int i = 0; i < N; i++){
            leak[i] = input.nextInt();
        }

        System.out.println(solution(leak, L, N));

    }
}

