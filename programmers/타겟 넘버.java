import java.util.*;
class Solution {

    int[] numbers;
    int answer;

    public void DFS(int S, int target, int dep){
        if(dep == numbers.length){
            if(S == target){
                answer++;
            }
            return;
        }


        DFS(S + numbers[dep], target, dep+1);
        DFS(S - numbers[dep],target,dep+1);
    }
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        DFS(0,target,0);
        return answer;
    }
}
