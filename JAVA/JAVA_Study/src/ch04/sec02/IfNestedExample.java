package ch04.sec02;

public class IfNestedExample {

	public static void main(String[] args) {
		int score = (int)(Math.random()*20) + 81;
		System.out.println("점수 : " + score);
		
		String grade;
		
		if(score>=90) { // if문
			if(score>=95) { // 중첩 if문
				grade = "A+";
			}
			else {
				grade = "A";
			} // 중첩 if문
		} // if문
		else { // else문
			if(score>=85) { // 중첩 if문
				grade = "B+";
			}
			else {
				grade = "B";
			}// 중첩 if문
		} // else문
		
		System.out.println("학점 : " + grade);

	}

}
