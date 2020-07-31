package contest;

import java.io.*;
import java.util.*;
import java.lang.Object.*;

public class CCCs120 {
	static class point {
		int time = 0;
		int location = 0;

		public point(int x, int y) {
			this.time = x;
			this.location = y;

		}

		public int getTime() {
			return this.time;
		}

		public int getLocation() {
			return this.location;
		}
	}

	static void merge(point[] ar, int l, int m, int r) {
		int n1 = m - l + 1;
		int n2 = r - m;
		point L[] = new point[n1];
		point R[] = new point[n2];
		for (int i = 0; i < n1; ++i)
			L[i] = ar[l + i];
		for (int j = 0; j < n2; ++j)
			R[j] = ar[m + 1 + j];
		int i = 0, j = 0;
		int k = l;
		while (i < n1 && j < n2) {
			int time1 = L[i].getTime();
			int time2 = R[j].getTime();
			if (time1 <= time2) {
				ar[k] = L[i];
				i++;
			} else {
				ar[k] = R[j];
				j++;
			}
			k++;
		}
		while (i < n1) {
			ar[k] = L[i];
			i++;
			k++;
		}
		while (j < n2) {
			ar[k] = R[j];
			j++;
			k++;
		}}
	static void sort (point ar [], int l, int r) {
		if (l<r) {
			int middle = (r+l)/2;
			sort(ar,l,middle);
			sort (ar,middle+1,r);
			merge(ar,l,middle,r);
		}}

	public static void main (String [] args) throws IOException{
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		int tests = Integer.parseInt(br.readLine());
		point [] points = new point [tests];
		
		for(int i = 0; i<tests;i++) {
			String [] point = br.readLine().split(" ");
			points[i] = new point(Integer.parseInt(point[0]),Integer.parseInt(point[1])) ;
			
		
		}
		sort (points, 0, tests-1);
//		for (point x:points) {
//			System.out.print(x.getTime());
//		}
		int latestt = -1;
		int latests = 0;
		double fastest = 0;
		int time = 0;
		int distance = 0;
		double speed = 0;
		for (point y: points) {
			time = y.getTime();
			distance = y.getLocation();
			//System.out.println(time + " " + distance);
			if (latestt != -1) {
				
				speed = Math.abs((double)(distance-latests)/(time-latestt));
				
				//System.out.println(speed);
				latests = distance;
				latestt = time;
				if(speed>fastest) {
					fastest = speed;
				}
				
			}else {
				latestt = time;
				latests = distance;
			}
		}
		System.out.println(fastest);
	}
}
