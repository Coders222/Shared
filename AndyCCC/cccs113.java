package contest;
import java.io.*;
import java.util.*;
import java.util.ArrayList;
public class cccs113 {
	static int convert( int num) {
		String []s = Integer.toString(num).split("");
		HashSet <String> set = new HashSet <> ();
		for(String st : s) {
//			System.out.println(set);
//			System.out.println(st);
			;
			if (set.contains(st)) {
				
				return (-1);
			}else {
				set.add(st);
			}
			
			
		}
		return(num);
	}
	public static void main (String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine())+1;
		boolean end = false;
		while (end == false) {
			int result = convert(num);
			if (result != -1) {
				System.out.println(result);
				break;
			}else {
				num++;
			}
		}
		
 	}	
}
