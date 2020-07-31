package contest;
import java.io.*;
public class Party {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int length = Integer.parseInt(br.readLine());
		int rounds =Integer.parseInt(br.readLine());
		int [] multiples = new int [rounds];
		for (int i = 0; i<rounds; i++) {
			multiples[i] = Integer.parseInt(br.readLine());
		}
		boolean [] number = new boolean [length];
		int count = 1;
		for (int x = 0; x<multiples.length;x++) {
			for (int y = 0; y<number.length;y++) {
				if (number[y] == false) {
					if (count == multiples[x]) {
						number[y] = true;
						count = 1;
					}else {
						count++;
					}
				}
			}
		}
		for(int z = 0; z<number.length;z++) {
			if (number[z] == false) {
				System.out.println(z+1);
			}
		}
	}
}
