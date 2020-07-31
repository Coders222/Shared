package contest;
import java.io.*;
public class ccc17s1 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tests = Integer.parseInt(br.readLine());
		String [] t1 = br.readLine().split(" ");
		String [] t2 = br.readLine().split(" ");
		int total1 = 0;
		int total2 = 0;
		int highest = 0;
		for(int i = 0; i<tests; i++) {
			total1 = total1+Integer.parseInt(t1[i]);
			total2 = total2+Integer.parseInt(t2[i]);
			if (total1== total2) {
				highest = i+1;
			}
		}
		System.out.println(highest);
	}
	

}
