package contest;
import java.io.*;
import java.util.*;



public class SAC22C2P4 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static StringTokenizer st;
	static int [][] dir = {{0,1}, {0,-1}, {1,0}, {-1,0}};
	public static void main(String[] args) throws IOException {
		int n = readInt(), m = readInt();
		char [][]grid = new char [n][m];
		for (int i = 0; i< n;i++) {
			grid[i] = readLine().toCharArray();
		}
		int[][] dis = new int [n][m];
		ArrayDeque<Integer> rows = new ArrayDeque();
		ArrayDeque<Integer> cols = new ArrayDeque();
		for (int k = 0; k< n;k++) Arrays.fill(dis[k], Integer.MAX_VALUE);
		rows.add(0);
		cols.add(0);
		dis[0][0] = 0;
		if (grid[0][0] == 'C')dis[0][0] = 1;
		while (!rows.isEmpty()) {
			int r = rows.poll();
			int c = cols.poll();
			for(int [] di : dir) {
				int nr = r+di[0];
				int nc = c+di[1];
				if(Math.min(nr, nc) < 0 || nr >= n || nc >= m)continue;
				int w = ((grid[nr][nc] == 'C')?1:0);
				if(dis[r][c] +w < dis[nr][nc]) {
					dis[nr][nc] = dis[r][c] +w;
					if(w == 0) {
						rows.addFirst(nr);
						cols.addFirst(nc);
					}else {
						rows.addLast(nr);
						cols.addLast(nc);
					}
				}
			}
			
		}
		System.out.println(dis[n-1][m-1]);
	}

	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens())
			st = new StringTokenizer(br.readLine().trim());
		return st.nextToken();
	}

	static long readLong() throws IOException {
		return Long.parseLong(next());
	}

	static int readInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double readDouble() throws IOException {
		return Double.parseDouble(next());
	}

	static char readCharacter() throws IOException {
		return next().charAt(0);
	}

	static String readLine() throws IOException {
		return br.readLine().trim();
	}
}


