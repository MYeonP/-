package class_;

public class SungJuk { //1인분
	private String name;	// 필드, 초기값 ( = null; 로 잡혀있다)
	private int kor, eng, math, tot; // = 0;
	private double avg;
	private char grade;
	// private로 캡슐화(가리기)
	
	public void setData(String n, int k, int e, int m) { // 메소드 구현
		name = n;
		kor = k;
		eng = e;
		math = m;
	}
	
	public void calc() {
		tot = kor + eng + math;
		avg = (double)tot / 3;
		if(avg >= 90) grade = 'A';
		else if(avg >= 80) grade = 'B';
		else if(avg >= 70) grade = 'C';
		else if(avg >= 60) grade = 'D';
		else grade = 'F';
	}
		
	public String getName() {
		return name; // 반환값
	}
	
	public int getKor() {
		return kor; // 반환값
	}
	
	public int getEng() {
		return eng; // 반환값
	}
	
	public int getMath() {
		return math; // 반환값
	}
	
	public int getTot() {
		return tot; // 반환값
	}
	
	public String getAvg() {
		return String.format("%.2f",avg); // 반환값
	}
	
	public char getGrade() {
		return grade; // 반환값
	}
	
 // 메뉴판 짜기 완성!


	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
