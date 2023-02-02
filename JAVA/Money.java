package operator;

import java.text.DecimalFormat; // DecimalFormat 오류로 import함
import java.util.Scanner;

public class Money {

	public static void main(String[] args) {
		int money;
		
		Scanner scan = new Scanner(System.in); // 키보드로 부터 입력 받는 Scanner 클래스를 생성
		System.out.print("돈 입력 : ");
		money = scan.nextInt();
		
		
		int ths = (money / 1000);
		int hud = (money % 5000 / 100);
		int ten = (money % 5300 / 10 );
		int one = (money % 5370);
		
		DecimalFormat df = new DecimalFormat();
		
		System.out.println("현금 : " + df.format(money) + "원"); // 세 자리 마다 쉼표(,)를 찍고싶다
		// '5,378원' 으로 출력 되지만 숫자형이 아닌 문자열로 인식한다
		System.out.println("천원 : " + ths + "장");
		System.out.println("백원 : " + hud + "개");
		System.out.println("십원 : " + ten + "개");
		System.out.println("일원 : " + one + "개");

	}

}



/*
[문제] 
동전 교환기 -> 현금 5378원이 있습니다.

[실행 결과]
현금 : 5378원
천원 : 5장
백원 : 3개
십원 : 7개
일원 : 8개

*/