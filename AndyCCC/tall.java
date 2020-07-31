package contest;
import java.io.*;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
public class tall {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		
		HashMap<Integer, LinkedList<Integer>> map = new HashMap<>();
		String [] data = br.readLine().split(" ");
		int people = Integer.parseInt(data[0]);
		int compare =Integer.parseInt(data[1]);
		for (int i = 0;i<compare; i++) {
			String [] comparasions = br.readLine().split(" ");
			int p = Integer.parseInt(comparasions[0]);
			int q=Integer.parseInt(comparasions[1]);
			if (map.containsKey(p)) {
				map.get(p).add(q);
			}else {
				LinkedList<Integer> temp = new LinkedList <> ();
				temp.add(q);
				map.put(p,temp);
			}
		}
		String finale = br.readLine();
		int shor = Integer.parseInt(finale.split(" ")[1]);
		//System.out.println(shor);
		int tall = Integer.parseInt(finale.split(" ")[0]);
		//System.out.println(tall);
		String result1 = BFS(map,shor, tall,people);
		String result2 = "";
		if (result1 == "no") {
			result2 = BFS(map,tall, shor,people);
		}
		if (result1.equals("yes")) {
			System.out.println("yes");
		}
		else if (result2.equals( "yes")) {
			System.out.println("no");
		}else {
			System.out.println("unknown");
		}
		
		
	}
	public static String BFS(HashMap<Integer, LinkedList<Integer>> map, int shorter, int taller, int people) {
		boolean [] visited = new boolean [people+1]; 
		LinkedList<Integer> queue= new LinkedList<Integer>();
		queue.add(shorter);
		visited [shorter] = true;
		
		while(queue.size() != 0) {
			int p = queue.poll();
			//System.out.println(map.get(p));
			if (map.get(p) == null) {
				
			}else {
				for (int t: map.get(p)){
				
					if (queue.contains(t) == true || visited[t] == true) {
						//System.out.println("visited");
					}else {
						if (t == taller) {
							return ("yes"); 
						}else {
							queue.add(t);
					}
				}
			}
		}
			}
		return ("no");
	}

}
