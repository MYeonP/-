package inheritance;

public class Super extends Object { // 모든 클래스에는 extends Object가 적용! 다만 빠져 있었다!
	protected double weight, height;
	
	Super(){
		System.out.println("Super 기본 생성자");
	} // 이렇게 하면 SubMain의 에러 해결
	
	Super(double weight, double height) {
		this.weight = weight;
		this.height = height;
	}

	public void disp() {
		System.out.println("몸무게 = " + weight);
		System.out.println("키 = " + height);
	}

	

}
