package multi;

public class MultiArray02 {

	public static void main(String[] args) {
		int[][] ar = new int[10][10];
		int num = 0;
		
		// 입력
//		for(int i=0; i<ar.length; i++) {	// 100행이라 i<3 or i<ar.length
//			for(int j=0; j<ar[i].length; j++) {
//				num++;
//				ar[i][j] = num;
//			} // for j
//		} // for i
		
//		// 입력(증가 숫자를 아래로)
//		for(int i=0; i<ar.length; i++) {	// 100행이라 i<3 or i<ar.length
//		for(int j=0; j<ar[i].length; j++) {
//				num++;
//				ar[j][i] = num;
//			} // for j
//		} // for i
		
		// 입력 (100 부터 1까지)
		for(int i=ar.length-1; i>=0; i--) {	// 100행이라 i=ar.length-1
			for(int j=ar[i].length-1; j>=0; j--) {
				num++;
				ar[i][j] = num;
			} // for j
		} // for i
		
		
		
		
		// 출력
		for(int i=0; i<ar.length; i++) {	// 100행이라 i<100 or i<ar.length
			for(int j=0; j<ar[i].length; j++) {
				System.out.print(String.format("%4d", ar[i][j]));
			} // for j
			System.out.println();
		} // for i

	}

}
