package example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class flipper {
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String flips = br.readLine();
		int countH = flips.length()- flips.replace("V","" ).length();
		int countV = flips.length()- countH;
		//System.out.println(countV+ " " + countH);
		int Hdir = countH%2;
		int Vdir = countV%2;
		
		if (Hdir == 1) {
			if (Vdir == 1) {
				System.out.println("4 3");
				System.out.println("2 1");
				
			}else {
				
				System.out.println("2 1");
				System.out.println("4 3");
			}
		}else {
			if(Vdir == 1) {
				System.out.println("3 4");
				System.out.println("1 2");
				
			}else {
				System.out.println("1 2");
				System.out.println("3 4");
			}
		}
		
		}
}
