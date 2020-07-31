package example;
import java.io.*;
public class CCC18S1 {
	static void merge(int []ar, int l, int m, int r) {
		// Find sizes of two subarrays to be merged
		int n1 = m - l + 1;
		int n2 = r - m;

		/* Create temp arrays */
		int L[] = new int[n1];
		int  R[] = new int [n2];

		/* Copy data to temp arrays */
		for (int i = 0; i < n1; ++i)
			L[i] = ar[l + i];
		for (int j = 0; j < n2; ++j)
			R[j] = ar[m + 1 + j];

		/* Merge the temp arrays */

		// Initial indexes of first and second subarrays
		int i = 0, j = 0;

		// Initial index of merged subarry array
		int k = l;
		while (i < n1 && j < n2) {
			int time1 = L[i];
			int time2 = R[j];
			if (time1 <= time2) {
				ar[k] = L[i];
				i++;
			} else {
				ar[k] = R[j];
				j++;
			}
			k++;
		}

		/* Copy remaining elements of L[] if any */
		while (i < n1) {
			ar[k] = L[i];
			i++;
			k++;
		}

		/* Copy remaining elements of R[] if any */
		while (j < n2) {
			ar[k] = R[j];
			j++;
			k++;
		}
	}
	static void sort (int ar [], int l, int r) {
		if (l<r) {
			int middle = (r+l)/2;
			sort(ar,l,middle);
			sort (ar,middle+1,r);
			merge(ar,l,middle,r);
		}
	}
	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		int vilage = Integer.parseInt(br.readLine());
		int [] vilages = new int [vilage +1];
		for (int i = 0; i<vilage ;i++) {
			vilages[i] = Integer.parseInt(br.readLine());
			
		}
		sort(vilages, 0, vilage-1);
		
		int last = vilages[0];
		int next = vilages[2];
		
		double smallest = -1;
		for (int s = 1; s<vilage-1;s++) {
			
			
			double size = (double)Math.round((next - last)/2*10)/10;
			if (smallest == -1) {
				smallest = size;
			}
			else if (smallest > size) {
				smallest = size;
			}
			
			last = vilages [s];
			next = vilages [s+2];
			
		}
		System.out.println(String.format("%.95f", (double)Math.round(smallest*10)/10));
		System.out.println((double)Math.round(smallest*10)/10);
		
	}

}
