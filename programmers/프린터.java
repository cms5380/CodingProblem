import java.util.*;

public class main {
    static class Docu{
        int priority;
        int index;

        public Docu(int priority, int index){
            this.priority = priority;
            this.index = index;
        }
    }
    public static int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Docu> q = new LinkedList<>();

        for(int i=0;i <priorities.length; i++){
            q.offer(new Docu(priorities[i], i));
        }

        Arrays.sort(priorities);

        for(int i = priorities.length - 1; i >= 0; i--){
            while(priorities[i] != q.peek().priority){
                Docu docu = q.poll();
                q.offer(docu);
            }

            answer++;

            if(q.poll().index == location) break;

        }

        return answer;
    }



    public static void main(String[] args){
        System.out.println(solution(new int[]{1, 1, 9, 1, 1, 1}, 0));

    }
}
