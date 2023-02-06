package for_;

import java.util.Scanner;

public class For02 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("원하는 단을 입력 : ");
		int dan = scan.nextInt();
		
		for(int i=1; i <= 9; i++) {
			System.out.println(dan + "*" + i + "=" + dan*i);
			
		}//for
		
		

		// 선생님 방법 _ 무식한 방법으로!
		//System.out.println(dan + "*" + 1 + "=" + dan*1);
		//System.out.println(dan + "*" + 2 + "=" + dan*2);
		//System.out.println(dan + "*" + 3 + "=" + dan*3);
		//System.out.println(dan + "*" + 4 + "=" + dan*4);
		//System.out.println(dan + "*" + 5 + "=" + dan*5);
		//System.out.println(dan + "*" + 6 + "=" + dan*6);
		//System.out.println(dan + "*" + 7 + "=" + dan*7);
		//System.out.println(dan + "*" + 8 + "=" + dan*8);
		//System.out.println(dan + "*" + 9 + "=" + dan*9);

	}

}

/*
[문제] 구구단

원하는 단을 입력 : 2

*/