import java.util.*;

public class main {
    public static int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        for(int i = 1; i < prices.length; i++){
            while(!stack.isEmpty() && prices[i] < prices[stack.peek()]){
                int tmp = stack.pop();
                answer[tmp] = i - tmp;
            }
            stack.push(i);
        }
        while(!stack.isEmpty()){
            int tmp = stack.pop();
            answer[tmp] = prices.length - tmp - 1;
        }
        return answer;
    }



    public static void main(String[] args){
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3, 2, 3})));

    }
}
