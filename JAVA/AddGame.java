package for_;

import java.util.Scanner;

public class AddGame {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int i, sum, a, b, dab;
		
		for(i=1; i<=5; i++) {
			sum += i;
			System.out.println("[" + i + "]" +
		}
		
		a = (int)(Math.random() * 90 + 10); //10 ~ 99
		b = (int)(Math.random() * 90 + 10); //10 ~ 99
		
		System.out.println(a + " + " + b + " = ");
		dab = scan.nextInt();
				
		if(dab == a+b) System.out.println("참 잘했어요");
		else System.out.println("틀렸습니다");
		

	}

}

/*
[문제] 덧셈 문제
- 2자리 숫자( 10 ~ 99 까지의 난수 발생)만 제공한다
- 총 5문제를 제공한다
- 1문제당 20점씩 처리

[실행 결과]
a    b

[1] 87 + 56 = 
참 잘했어요
틀렸습니다

[2] 87 + 56 = 
참 잘했어요
틀렸습니다

[3] 87 + 56 = 
참 잘했어요
틀렸습니다

[4] 87 + 56 = 
참 잘했어요
틀렸습니다

[5] 87 + 56 = 
참 잘했어요
틀렸습니다

당신은 총 x문자를 맞추어서 점수 xx점 입니다.
count / count * 20


*/