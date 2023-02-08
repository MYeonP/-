package class_;

public class Compute {	// 1인분
	private int x, y, sum, sub, mul;
	private double div;
	// private로 캡슐화(가리기)
	
	public void setData(int x, int y) { 
		this.x = x; // setData가 아닌 클래스의 x로 잡아주기 위해 this.를 붙인다
		this.y = y;
		// 메소드 구현
	}
	
	public void calc() {
		sum = x + y;
		sub = x - y;
		mul = x * y;
		div = (double)sum / 2;
	}
		
	public int getX() {
		return x; // 반환값 & this는 생략 가능하다
	}
	
	public int getY() {
		return y; // 반환값
	}
	
	public int getSum() {
		return sum; // 반환값
	}
	
	public int getSub() {
		return sub; // 반환값
	}
	
	public int getMul() {
		return mul; // 반환값
	}
	
	public String getDiv() {
		return String.format("%.3f",div); // 반환값
	}

	
 // 메뉴판 짜기 완성!

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
