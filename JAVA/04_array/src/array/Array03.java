package array;

import java.util.Scanner;

public class Array03 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int size;
		int[] ar;
		int sum = 0;
		
		
		System.out.print("배열 크기 입력 : ");
		size = scan.nextInt();
		ar = new int[size];		// 배열 생성
		
		for(int i=0; i<size; i++) {
			System.out.print("ar[" + i + "] 입력 : ");
			ar[i] = scan.nextInt();
			
			sum += ar[i];
		} // for
		System.out.println();
		
		// 최대값 & 최소값
		int max = ar[0]; //배열의 첫번째 데이터를 초기값으로 갖는다 
		int min = ar[0]; // 최소값
		for(int i=1; i<ar.length; i++) {
			if(ar[i] > max) max = ar[i];
			if(ar[i] < min) min = ar[i];
		}
		
		
		for(int data : ar) {
			System.out.print(data + " ");
		}
		System.out.println();
		System.out.println("합 = " + sum);
		System.out.println("최대값 = " + max);
		System.out.println("최소값 = " + min);
		
		// System.out.print("ar[0] 입력 : ");
		// ar[0] = scan.nextInt();
		// System.out.print("ar[1] 입력 : ");
		// ar[1] = scan.nextInt();
		// System.out.print("ar[2] 입력 : ");
		// ar[2] = scan.nextInt();
		// System.out.print("ar[3] 입력 : ");
		// ar[3] = scan.nextInt();
		
		// System.out.print(ar[0] + " ");
		// System.out.print(ar[1] + " ");
		// System.out.print(ar[2] + " ");
		// System.out.print(ar[3] + " ");
		
		
		//System.out.println("배열명 ar = " + ar);


	}

}

/*
[문제] 배열의 크기를 입력받아서 배열을 생성한다.
데이터 출력하고 합, 최대값, 최소값을 구하시오.


[실행결과]
배열 크기를 입력 : 3

ar[0] 입력 : 25
ar[1] 입력 : 13
ar[2] 입력 : 57

25 13 57
합 = xxx
*/