package example;
import java.io.*;
import java.util.LinkedList;
public class CCC19s2 {
	
	static void prime (boolean [] notPrime, int n) {
		for (int p = 2; p*p <= n; p++) {
			if (notPrime[p] == false) {
				for (int i = p*p; i<=n; i += p) {
					notPrime[i] = true;
				}
			}
		}
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tests = Integer.parseInt(br.readLine());
		int []num = new int [tests];
		int highest = 0;
		int temp = 0;
		for(int i = 0; i<tests; i++) {
			temp = Integer.parseInt(br.readLine())*2;
			num[i] = temp;
			if (temp>highest) {
				highest = temp;
			}
		}
		boolean []notPrime = new boolean [highest+1];
		boolean temp3 = false;
		int temp4 = 0;
		prime(notPrime, highest);
		LinkedList <Integer> list = new LinkedList<>();
		for (int l = 2; l<highest; l++) {
			boolean temp2 = notPrime[l];
			if (temp2 == false) {
				list.add(l);
				if (temp3 == false) {
					temp4 = num[0]-l;
					if (notPrime[temp4] == false) {
						System.out.println(l + " " + temp4);
						temp3 = true;
					}
				}
			}
		}
		for (int z = 1; z < tests; z++) {
			for (int y : list) {
				temp4 = num[z] - y;
				if (notPrime[temp4] == false) {
					System.out.println(y + " " + temp4);
					break;
				}
			}
		}
		
	}

}
