package operator;

import java.util.Scanner;

public class operator02 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("정수를 입력하세요 : ");
		int num = scan.nextInt(); 
		
		String result = num%2 == 0 ? "짝수" : "홀수";
						//2의 배수 입니까?
						//2로 나누면 나머지가 0입니까?
		String result2 = num%2 == 0 && num%3 == 0 ? "공배수다" : "공배수가 아니다";
						// num이 2와 3의 공배수 입니까?
						// num이 2로 나누면 나머지 0이고, 3으로 나누면 나머지 0
						// num이 2로 나누어 떨어지고, 3으로도 나누어 떨어진다
		System.out.println(result);
		System.out.println(result2);
		
		

	}

}
