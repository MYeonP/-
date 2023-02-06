package basic;

public class Calc {

	public static void main(String[] args) {
		// int a = 320, b = 258;로 처리 가능
		
		int a;
		a = 320;
		
		int b;
		b = 258;
		
		double result = (double)a/b;
		
		System.out.println(a + "+" + b + "="  + (a+b));
		System.out.println(a + "-" + b + "="  + (a-b));
		System.out.println(a + "*" + b + "="  + (a*b));
		System.out.println(a + "/" + b + "="  + String.format("%.2f", result));
	}
	// String.format : format은 바로 써도 되는 static으로 볼 수 있음

}


// 1줄 주석

/*
[문제] 320(a), 258(b)을 변수에 저장하여 합(sum), 차(sub), 곱(mull), 몫(div)을 구하시오.
단, 소수 이하 둘째자리까지 출력

[실행결과]
320 + 258 = xxx
320 - 258 = xxx
320 * 258 = xxx
320 / 258 = x.xx


*/