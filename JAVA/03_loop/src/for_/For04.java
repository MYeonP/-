package for_;

import java.util.Scanner;

public class For04 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int mul = 1;

		System.out.println("x값 입력 : ");
		int x = scan.nextInt();
		System.out.println("y값 입력 : ");
		int y = scan.nextInt();
		
		for(int i=1; i<=y; i++) {
			mul *= x; 
		}
		
		System.out.println(x + "의 " + y + "승은 " + mul);

	}

}

/*
[문제] 제곱계산 : x의 y승
자바에서는 2ⁿ = 2 * 2 * 2 * 2 * ... 로 써줘야 함

x값 입력 : 2
y값 입력 : 5

2의 5승은 32
------------------
x값 입력 : 3
y값 입력 : 4

3의 4승은 81

*/