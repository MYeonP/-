package basic;

import java.util.Arrays;
import java.util.Random;
//import 된 내역들은 이 곳에 표시

public class MethodTest02 {

	public static void main(String[] args) {
		// 난수 : 컴퓨터가 불규칙적으로 발생하는 수
		// 		0 <= 난수 < 1 (0보다 같거나 크고 1보다는 작다) 

		double a = Math.random();
		System.out.println("난수 = " + a);
		
		Random r = new Random();
		// 자바의 default 패키지는 java.lang에 있다
		// 따라서 java.lang에 없는 함수는 import를 시켜줘야 함
		double b = r.nextDouble();
		System.out.println("난수 = " + b);
		
		int[] ar = new int[5]; // 정수형 변수_배열
		ar[0] = 25;
		ar[1] = 13;
		ar[2] = 45;
		ar[3] = 30;
		ar[4] = 15;
		System.out.println(ar[0] + "," + ar[1] + ","+ ar[2] + ","+ ar[3] + "," + ar[4]);
		
		Arrays.sort(ar);	//넘길 자료가 없어서 변수 지정 x
		System.out.println(ar[0] + "," + ar[1] + ","+ ar[2] + ","+ ar[3] + "," + ar[4]);
		// 정렬 -> 오름차순
		
		
	}

}
