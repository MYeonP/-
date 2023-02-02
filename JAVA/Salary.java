package operator;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Salary {

	public static void main(String[] args) {
		String name = "홍길동";
		String position = "부장";
		int pay = 4900000;
		int benefit = 200000;
		
		int total = pay + benefit;
		int tax = total>=5000000 ? (int)(total*0.03) : (int)(total*0.02);
		int salary = total - tax;
		
		System.out.println("이름 입력 : " + name);
		System.out.println("직급 입력 : " + position);
		System.out.println("기본급 입력 : " + pay);
		System.out.println("기본급 입력 : " + benefit);
		System.out.println();
		
		DecimalFormat df = new DecimalFormat();
		
		System.out.println("*** 홍길동 부장 월급 ***");
		System.out.println("기본급 : " + df.format(pay) + "원");
		System.out.println("수당  :   " + df.format(benefit) + "원");
		System.out.println("합계  : " + df.format(total) + "원");
		System.out.println("세금  :   " + df.format(tax) + "원");
		System.out.println("월급  : " + df.format(salary) + "원");
	}

}

/*

[문제] 월급 계산 프로그램 - 조건 연산자
이름, 직급, 기본급, 수당을 입력하여 합계, 세금, 월급을 출력하시오
단 합계가 5,000,000원 이상이면 3%
       3,000,000원 이상이면 2%
       아니면 1%
       
합계 = 기본급 + 수당
세금 = 합계 * 세율
월급 = 합계 - 세금

[실행결과]
이름 입력 : 홍길동
직급 입력 : 부장
기본급 입력 : 4900000
수당 입력 : 200000

*** 홍길동 부장 월급 ***
기본급 : 4,900,000원
수당  :   200,000원
합계  : 5,100,000원
세금  :   153,000원
월급  : 4,947,000원

*/