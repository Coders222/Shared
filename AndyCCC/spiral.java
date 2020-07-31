package contest;

import java.io.*;
import java.math.*;
public class spiral {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in)) ;
		int start = Integer.parseInt(br.readLine());
		int end = Integer.parseInt(br.readLine());
		int length = end - start+1;
		int direction = 1;
		int dim = (int) Math.ceil(Math.sqrt(length));
		
		
		int[][] spiral = new int [dim][dim];
		int x = 0;
		if (dim%2 == 0) {
			x = (int)((dim/2)-1);
		}else {
			x = (int) (Math.floor(dim/2));
		}
		
		
		int y = x;
		int count = 0;
		int count2 = 0;
		int multiplier = 1;
		for (int i = 0; i<length;i++) {
			//System.out.println(x+" " + y + " " + i+ " " + length);
			
			if (direction == 1) {
				spiral [y][x] = start +i;
				y++;
				
			}else if (direction == 2) {
				spiral [y][x] = start +i;
				x++;
				
			}else if (direction == 3) {
				spiral [y][x] = start +i;
				y--;
				
			}
			else if (direction == 4) {
				spiral [y][x] = start +i;
				x--;
				
			}
			count++;
			if (count == multiplier) {
				count = 0;
				if (count2 == 1) {
					multiplier++;
					count2 = 0;
				}else {
					count2++;
				}
				
				if (direction == 4) {
					direction = 1;
				}else {
					direction++;
				}
			}
		}
		for (int h = 0; h<dim;h++) {
			for (int w = 0; w<dim;w++) {
				int bruh = spiral[h][w];
				if (bruh != 0) {
					if (bruh < 10) {
						System.out.print(" " + bruh+ " ");
					}else {
						System.out.print(bruh+ " ");
					}
					
				}else if (bruh == 0) {
					System.out.print("   ");
				}
			
		}
			System.out.println();
	}

}}
