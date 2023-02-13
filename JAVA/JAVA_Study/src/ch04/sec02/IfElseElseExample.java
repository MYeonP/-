package ch04.sec02;

public class IfElseElseExample {

	public static void main(String[] args) {
		int score = 75;
		
		if(score>=90) {
			System.out.println("점수가 100 ~ 90 입니다.");
			System.out.println("등급은 A입니다.");
		} // if문 종료
		else if(score>=80) {
			System.out.println("점수가 80 ~ 90 입니다.");
			System.out.println("등급은 B입니다.");
		} // else if 1 : 점수가 80 이상 90 미만일 경우(80<=score<90)
		else if(score>=70) {
			System.out.println("점수가 70 ~ 80 입니다.");
			System.out.println("등급은 C입니다.");
		} // else if 2 : 점수가 70 이상 80 미만일 경우(70<=score<80)
		else { // else : 점수가 70 미만일 경우(score<70)
			System.out.println("점수가 70 미만입니다.");
			System.out.println("등급은 D입니다.");
		}

	}

}
