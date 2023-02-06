package while_;

import java.util.Scanner;

public class NumberGame {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int com, user, count;
		
		while(true) { //while 1
			com = (int)(Math.random() * 100 + 1); // 1 ~100
			//System.out.println(com);
			
			// x ~ y 사이의 난수를 발생시키기
			// (int)(Math.random()*100); -> 0 ~ 99까지가 끝
			// 0.5362234 => 53
			// 0.00056755 => 0
			// 0 말고 1 이상 부터 시작하게 하고 싶다 -> +1을 해 주면 됨 / (int)(Math.random()*100+1)
			// 응용 : 65~90까지 -> (int)(Math.random()* 25 + 65)
			// 나는 65 부터 시작하게 하고 싶다! (int)(Math.random()*100+65);
			
			
			System.out.println("1 ~ 100 사이의 숫자를 맞추세요");
			count = 0;
			while(true) { //while2
				System.out.print("숫자 입력 : ");
				user = scan.nextInt();
				count++; //count = count + 1
				if(user == com) break;
				
				
				if(user < com) System.out.println( user + "보다 큰 숫자입니다.");
				else if(user > com) System.out.println( user + "보다 작은 숫자입니다.");
			}// while 2
		
			System.out.println("\n 정답!" + count + "번 만에 맞추셨습니다.");
			
			System.out.println("\n 한번 더 하시겠습니까? (y/n) : ");
			//int yn = scan.nextInt(); // y or n
			String yn = scan.next();
			
			//if(yn == 'n' || yn == 'N') break; -> int yn으로 물어봤을 때
			if(yn.equals("n") || yn.equals("N")) break; //String yn으로 물어봤을 때
			
			
		} // while 1
		
		System.out.println("프로그램을 종료합니다.");
	}

}


/*
[문제] 숫자 맞추기 게임
- 컴퓨터(com)가 1 ~ 100사이의 난수를 발생하면, 난수를 맞추는 게임
- 몇 번 만에 맞추었는지 출력한다

[실행결과]
1 ~ 100 사이의 숫자를 맞추세요 (70)

숫자 입력 : 50
50보다 큰 숫자입니다.

숫자 입력 : 85
85보다 작은 숫자입니다.

숫자 입력 : 70
정답! a번만에 맞추셨습니다.

한번 더 하시겠습니까? (y/n)
y : 처음부터
n : 프로그램을 종료합니다

for문 보다는 while문이 나음

*/