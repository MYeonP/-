package for_;

import java.util.Scanner;

public class Game {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int coin = 0, user = 1, answer = 0;
		int com = 0;
		
		while (true) {
			System.out.println("insert coin : ");
			coin = scan.nextInt();
			
			for(int in=coin; in >=300;) {
				
				if(in >= 300);
				System.out.println("가위(1), 바위(2), 보(3) 중 번호 입력 : ");
				user = scan.nextInt();
				com = (int)(Math.random() * 3 + 1);
				
					if(user == 1) {
						if(com == 1) {
						System.out.println("컴퓨터 : 가위 \t 나 : 가위");
						System.out.println("You Draw!");}
						
						else if(com == 2) {
						System.out.println("컴퓨터 : 바위 \t 나 : 가위");
						System.out.println("You Lose!");}
						
						else if(com == 3) {
						System.out.println("컴퓨터 : 보 \t 나 : 가위");
						System.out.println("You Win!");}
					}
					
					else if (user == 2) {
						if(com == 1) {
						System.out.println("컴퓨터 : 가위 \t 나 : 바위");
						System.out.println("You Win!");}
						
						else if(com == 2) {
						System.out.println("컴퓨터 : 바위 \t 나 : 바위");
						System.out.println("You Draw!");}
						
						else if(com == 3) {
						System.out.println("컴퓨터 : 보 \t 나 : 바위");
						System.out.println("You Lose!");}
					}
					
					else if (user ==3) {
						if(com == 1) {
						System.out.println("컴퓨터 : 가위 \t 나 : 보");
						System.out.println("You Lose!");}
						
						else if(com == 2) {
						System.out.println("컴퓨터 : 바위 \t 나 : 보");
						System.out.println("You Win!");}
						
						else if(com == 3) {
						System.out.println("컴퓨터 : 보 \t 나 : 보");
						System.out.println("You Draw!");}
					}
					
					in -= 300;
					
					
					if (in<300) {
						System.out.println("게임을 다시 하시겠습니까? '예'는 1을 '아니오'는 2를 입력하세요.");
						answer = scan.nextInt();
						}
					
					if (answer == 2) {
						break;}
					else {
						continue;}
			}
			

		}
			
		
		
	}
}

/*
[문제] 가위 바위 보 게임
- 가위(1), 바위(2), 보(3) 지정
- 컴퓨터(com)는 1 ~ 3까지 난수로 나온다
- 1게임 당 300원
- If문, For문 사용

[실행결과]
insert coin : 1000

가위(1), 바위(2), 보(3) 중 번호 입력 : 3 (user, 사용자)

결과를 보려면 Enter를 치세요 -> 해당 문구는 선택사항

컴퓨터 : 바위		나 : 보자기
You Win!! 

가위(1), 바위(2), 보(3) 중 번호 입력 : 1 (user)
컴퓨터 : 가위		나 : 가위
You Draw!!

가위(1), 바위(2), 보(3) 중 번호 입력 : 3 (user)
컴퓨터 : 가위		나 : 보자기
You Lose!!

*/