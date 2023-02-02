package operator;

import java.util.Scanner;

public class Operator01 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("점수 입력 : ");
		int score = scan.nextInt(); 
		
		// 조건 참 or 거짓
		
		String result = score>=80 && score<=100 ? "합격" : "불합격";
		System.out.println(result);
		
		System.out.println(score>=80 && score<=100 ? "합격" : "불합격");
	}

}
