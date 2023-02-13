package ch04.sec02;

public class IfExample {

	public static void main(String[] args) {
		int score = 93;
		
		if(score >= 90) {
			System.out.println("점수가 90보다 큽니다");
			System.out.println("등급은 A입니다");
		} // if 1 종료
		
		if(score<90) 
			System.out.println("점수가 90보다 작습니다");
			System.out.println("등급은 B입니다");
			// 15번이 무조건 실행 되는 이유 : 
			// 13라인 if의 중괄호 블럭이 없어서, if문이 14라인 까지만 영향을 미친다

	}

}
