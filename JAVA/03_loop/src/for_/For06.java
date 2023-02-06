package for_;

import java.util.Scanner;

public class For06 {

	public static void main(String[] args) {

		int number=0;
		
		while (true) {
		Scanner scan = new Scanner(System.in);
		System.out.println("1 ~ 10 사이의 숫자 입력 : ");
		number = scan.nextInt();
		
		
		if(number<1 || number>10) {
			continue;
			}
		else {
            int facto = 1;
            for (int i = 1; i <= number; i++) {   // for (int i=input; i>=1; i--)
                facto *= i;
            }
            System.out.println(number + "! = " + facto);
            System.out.println("--------------------");

		}


	}
	}
}

/*
[문제] 팩토리얼을 구하시오 (for)
- 입력되는 숫자는 1 ~ 10 사이만 입력한다.

[실행결과]
숫자 입력 : 3
3! = 6 (1*2*3)
---------------------

숫자 입력 : 5
5! = 120 (1*2*3*4*5)

*/