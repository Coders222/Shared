package example;
import java.io.*;
public class CCC13S2 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		int max = Integer.parseInt(br.readLine());
		int num = Integer.parseInt(br.readLine());
		int totalweight = 0;
		int [] trains = new int [num];
		boolean end = true;
		int temp = 0;
		for (int i = 0; i<num; i++) {
			
			int newTrain = Integer.parseInt(br.readLine());
			trains[i] = newTrain;
			if (i<4) {
				totalweight = totalweight+newTrain;
				
			}else {
				totalweight = totalweight + newTrain - trains[i-4];
			}
			temp = i+1;
			//System.out.println(i+ " " + totalweight);
			if (totalweight > max){
				System.out.println(i);
				end = false;
				break;
				
			}else {
				continue;
				}
			
			
			}
		if (end == true) {
			System.out.println(temp);
		}
	}

}
