package contest;
import java.io.*;
import java.util.*;
public class s313 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tests = Integer.parseInt(br.readLine());
		List <int []> data = new ArrayList<int[]>();
		
		for (int i = 0; i<tests; i++) {
			int cars = Integer.parseInt(br.readLine());
			int [] temp = new int [cars];
			
			for(int l = 0; l<cars;l++) {
				temp[l] = Integer.parseInt(br.readLine());
		}
			data.add(temp);
		
			
		}
		for (int i = 0; i<tests; i++) {
			//System.out.println("---------------- oof -----------");
			Stack <Integer> mtn = new Stack<>();
			Stack <Integer> branch = new Stack<>();
			int [] start = data.get(i);
			for (int s : start) {
				mtn.push(s);
			}
			
			boolean work = true;
			//System.out.println(mtn);
			int lake = 1;
			boolean move = false;
			///System.out.println(mtn.size() + " " + branch.size());
			while(mtn.size() > 0 ||branch.size() > 0) {
				///System.out.println("loop");
				move = false;
				if (mtn.size() == 0 && branch.size() != 0&&branch.peek() != lake){
					work = false;
					break;
				}
				if (mtn.size()>0) {
					//System.out.println(mtn+ " mtn");
					if (mtn.peek() == lake) {
						lake = mtn.pop()+1;
						//System.out.println(lake-1 + " mtn to lake");
						move = true;
				}
				}
				if (branch.size() > 0) {
					//System.out.println(branch + " branch");
					if (branch.peek() == lake) {
						lake = branch.pop()+1;
					//	System.out.println(lake-1 + " branch to lake");
						move = true;
				}
			}
				
				
				if (mtn.size() > 0&&branch.size() <1&&mtn.peek()!=lake&&move == false) {
					//System.out.println(mtn.peek()+ " mtn to branch");
					branch.push(mtn.pop());
					move = true;
						
				}
				else if (mtn.size()>0 && branch.size()>0&&mtn.peek()!= lake&& branch.peek()!=0&&move == false) {
					//System.out.println(mtn.peek()+ " mtn to branch");
					branch.push(mtn.pop());
					move = true;
				}
					
			}
			if (work == true) {
				System.out.println("Y");
			}else {
				System.out.println("N");
			}
		}
	}

}
