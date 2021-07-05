import java.util.*;

class Main {
    public static int solution(int N) {
        int num = 0;
        int answer = 1;
        if(N < 10)
            num = N*10;

        int a = N/10;
        int b = N%10;

        num = b*10 + (a+b)%10;

        while(num != N){
            a = num/10;
            b = num%10;

            num = b*10 + (a+b)%10;
            answer++;

        }
        return answer;
    }



    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();

        System.out.println(solution(N));

    }
}

