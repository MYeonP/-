package operator;

public class Comp {

	public static void main(String[] args) {
		char ch = 'B';
		// char ch = 'e';
		
		int result = ch>='A' && ch<='Z' ? ch+32 : ch-32;
										// 숫자와 더해지며 int형으로 변환 된 	
		
		System.out.println(ch + " → " + (char)result);
		
		
		
		// char ch = 'e';
		// ch가 대문자 입니까? 소문자 변환 : 대문자 변환;
		
		

	}

}

/*

[문제] 변수의 값이 대문자이면 소문자로 변환해서 출력, 소문자이면 대문자로 변환해서 출력하시오

[실행결과]
B → b
또는

e → E

*/
