package example;
import java.io.*;
import java.util.*;
public class CCC20S3 {
	
	static void convertHash(HashMap<String, Integer> nperm, String [] needle) {
		for (String s : needle) {
			Integer value = nperm.get(s);
			if (value != null) {
				nperm.put(s, value+1);
			}else {
				nperm.put(s, 1);
			}
		}
	}
	public static void main (String [] args)throws IOException {
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		String [] needle = br.readLine().split("");
		HashMap<String, Integer> needleH = new HashMap <> ();
		String hay = br.readLine();
		int length = needle.length;
		int lengthh=  hay.length();
		convertHash(needleH, needle);
		HashMap<String, Integer> HayH = new HashMap<>();
		
		String [] haystack =hay.split("");
		HashSet <String> used = new HashSet<String>();
		int count = 0;
		
		String temp = "";
		if (lengthh< length) {
			System.out.println(0);
		}else {
			convertHash(HayH, hay.substring(0,length).split(""));
			for (int i = length; i<=hay.length();i++) {
				temp= hay.substring(i-length, i);
				//System.out.println(temp);
				if(used.contains(temp)) {
					//System.out.println("smae");
				}else {
					if (HayH.entrySet().equals(needleH.entrySet())) {
						//System.out.println(" bruh");
						used.add(temp);
						count++;
					}
				}
				//System.out.println(HayH + " " + i);
				
				if(i < hay.length()) {
					String last = haystack[i-length];
					String first = haystack[i];
					int val = HayH.get(last);
					if (val == 1) {
						HayH.remove(last);
					}else {
						HayH.replace(last, val-1);
					}	
					Integer val2 = HayH.get(first);
					if (val2 != null) {
						HayH.replace(first, val2+1);
					}else {
						HayH.put(first, 1);
					}
			}
				
				
			}
			System.out.println(count);
		}
		
		
		
	} 
}
