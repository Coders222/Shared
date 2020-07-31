
package example;

import java.io.*;

import java.util.*;
public class ccc01s3 {
	public static HashMap<String, LinkedList<String>> map = new HashMap<>();
	static boolean end = false;
	public static int disRoad;
	public static void main (String[]args) throws IOException{
		graph();
		
	}
	
	public static void graph () throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		LinkedList <String> roads = new LinkedList <String> ();
		while (end == false) {
			
			String in = br.readLine();
			String [] s = in.split("");
			if (s[0].contains("*")) {
				end = true;
			}else {
				roads.add(in);
				String a = s[0];
				String b = s[1];
				if (map.containsKey(a) == true) {
					map.get(a).add(b);
				}
				else {
					LinkedList<String> temp = new LinkedList<>();
					temp.add(b);
					map.put(a, temp);
				}
				if (map.containsKey(b) == true) {
					map.get(b).add(a);
				}
				else {
					LinkedList<String> temp = new LinkedList<>();
					temp.add(a);
					map.put(b, temp);
				}
				
				
			}
		}
		//System.out.println(map.get("A"));
		
//		System.out.println(map);
		solve(map, roads);
		
	}
	public static void solve (HashMap <String, LinkedList<String>>map,LinkedList<String> roads) {
		int count = 0;
		for(String dis : roads) {
			
			HashMap <String, LinkedList<String>> temp2 = map; //creates new map to edit as temp for DFS
			String []points = dis.split("");
			String c = points[0];
			String x = points[1];
			
			temp2.get(c).remove(x);
			
			temp2.get(x).remove(c);
//			System.out.println(x+c +" " + temp2);
			String result = DFS(temp2, c+x);
			temp2.get(c).add(x);
			temp2.get(x).add(c);
			if(result.equals("no")){
				
			}else {
				count++; 
				System.out.println(result);
			}
			//removes the road that we are testing to see if it disconnects A and B
			}
		System.out.println("There are " + count + " disconnecting roads.");
		
	}
			
			//runs DFS to see if we can still access B
			
		
		
	
	public static String DFS (HashMap<String, LinkedList<String>> nmap, String disroad ) {
		HashMap<String, Integer> visited = new HashMap<>(); 
		LinkedList<String> queue= new LinkedList<String>();
		
		for(String l : nmap.keySet()) {
			visited.put(l, 0);
		}
		visited.replace("A", 1);
		queue.add("A");
		
		while (queue.size() != 0) 
		{
			String p = queue.poll();
			visited.put(p, 1);
			Iterator <String> i = nmap.get(p).listIterator();
			while (i.hasNext()) {
				String t = i.next();
				if (queue.contains(t)||visited.get(t) == 1) {
					
				}else {
					
	//				System.out.println(t);
	//				System.out.println(visited.get(t));
//					if (disroad.equals("EC")) {
//						System.out.println(p + "-" +t);
//						System.out.println(nmap.get("G"));
//						System.out.println(queue);
//						System.out.println(queue.contains(t));
//						System.out.println(nmap.get("A"));
//					}
					if (t.equals("B")){
						queue.removeAll(queue);
						visited.replace("B", 1);
						break;
					}
					if (visited.get(t) != 1) {
	//					System.out.println(t + " " + visited.get(t));
						queue.add(t);
						
					}
			
		}
			
			}
		
		
	}
		if(visited.get("B").equals(0)) {
			return (disroad);
		}else {
			return ("no");
		}
	
	
	}
}



