package example;
import java.io.*;
import java.util.*;
public class CCC16s1 {
	
	static boolean mapCheck(HashMap <String, Integer> mapA,HashMap <String, Integer> mapB ) {
		if (mapA.keySet().containsAll(mapB.keySet())) {
			for (String x : mapB.keySet()) {
				if (mapA.get(x) >= mapB.get(x)) {
					
				}else {
					return false;
				}
			}
			return true;
		}else {
			return false;
		}
			
	}

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		String [] word1 = br.readLine().split("");
		String [] word2 = br.readLine().split("");
		HashMap <String, Integer> letters1 = new HashMap<>();
		HashMap <String, Integer> letters2 = new HashMap<>();
		String letter1 = "";
		String letter2 = "";
		boolean result = true;
		if (word1.length == word2.length) {
			for (int i = 0; i<word1.length ; i++) {
				letter1 = word1[i];
				if (letters1.containsKey(letter1)) {
					int temp = letters1.get(letter1);
					letters1.replace(letter1, temp+1);
				}else {
					letters1.put(letter1, 1);
				}
				letter2 = word2[i];
				if (!letter2.equals("*")) {
					if (letters2.containsKey(letter2)) {
						int temp2 = letters2.get(letter2);
						letters2.replace(letter2, temp2+1);
					}else {
						letters2.put(letter2, 1);
					}
				}
					
			}
		}else {
			result = false;
		}
		//System.out.println(letters1);
		//System.out.println(letters2);
		
		
		if (result == false) {
			System.out.println("N");
		}else {
			boolean result2 = mapCheck(letters1, letters2);
			if (result2 == true) {
				System.out.println("A");
			}else {
				System.out.println("N");
			}
		}
	}

}
