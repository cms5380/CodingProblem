import java.util.*;
public class Main {
    public static void solution(String str){
        PriorityQueue<String> pq = new PriorityQueue<>();

        for(int i = 0; i < str.length(); i++){
            pq.add(str.substring(i));
        }

        while(!pq.isEmpty()){
            System.out.println(pq.peek());
            pq.poll();
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        solution(s);
    }
}
