package contest;
import java.io.*;
import java.util.Arrays;
public class CCC16{
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
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		int question = Integer.parseInt(br.readLine());
		int peeps = Integer.parseInt(br.readLine());
		int [] dmoj = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); 
		int [] peg = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		sort(dmoj, 0, peeps-1);
		sort(peg, 0, peeps-1);
		int total = 0;
		
		if (question == 1) {
			for (int s = 0; s<peeps; s++) {
				total = total + Math.max(dmoj[s], peg[s]);
			}
		}else {
			for (int i = 0; i<peeps; i++) {
				//System.out.println(total);
				total = total +Math.max(dmoj[i], peg[peeps-1-i]);
			}
		}
		System.out.println(total);
	}
}
