package example;
import java.io.*;
import java.util.HashMap;
import java.util.HashSet;

public class Partners {
	public static void main (String []args ) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		boolean good = true;
		int num = Integer.parseInt(br.readLine());
		String [] p1 = br.readLine().split(" ");
		String [] p2 = br.readLine().split(" ");
		
		
		for (int i = 0; i<p1.length; i++) {
			String part1 = p1[i];
			String part2 = p2[i];
			if (part1 == part2) {
				good = false;
				break;
			}
			for(int l = 0; l<p1.length; l++){
				if (p1[l].equals(part2)&& !p2[l].equals(part1)) {
					good = false;
				}
				
			}
		}
		if (good == true) {
			System.out.println("good");
		}else {
			System.out.println("bad");
		}
	}
}
