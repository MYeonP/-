package for_;

import java.util.Scanner;

public class AddGame {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a, b, dab, count=0;
		
		for(int i=1; i<=5; i++) {
			a = (int)(Math.random() * 90 + 10); //10 ~ 99
			b = (int)(Math.random() * 90 + 10); //10 ~ 99
			
// 과제	
			for(int j=1; j<=2; j++) {// 틀리면 기회
				System.out.println("[" + i + "]" + a + "+" + b + "=");
				dab = scan.nextInt();
				
				if(dab == a+b) {
					System.out.println("참 잘했어요");
					count++;
					break; // for j를 벗어나라
				}
				else
					if(j == 1) System.out.println("틀렸습니다");
					else if(j == 2) System.out.println("틀렸습니다. 정답은 " + (a + b));
			} // for j
			
			System.out.println("[" + i + "] " + a + " + " + b + " = ");
			dab = scan.nextInt();
					
			if(dab == a+b) {
				System.out.println("참 잘했어요"); 
				count++;
			}
			else System.out.println("틀렸습니다");
		}//for
		System.out.println();
		System.out.println("당신은 총 " + count + "문제를 맞추어서 점수 " + count*20 + "점 입니다.");

	}

}

/*
[문제] 덧셈 문제
- 2자리 숫자( 10 ~ 99 까지의 난수 발생)만 제공한다
- 총 5문제를 제공한다
- 1문제당 20점씩 처리
- 틀리면 1번 더 기회를 준다

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

당신은 총 x문제를 맞추어서 점수 xx점 입니다.
count / count * 20


*/