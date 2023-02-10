package inheritance;

public class ChildMain extends Super{
	private String name;
	private int age;
	
	ChildMain(){
		System.out.println("ChildMain 기본 생성자");
	}
	
	ChildMain(String name, int age, double weight, double height) {
		super(weight, height); // 부모 생성자 선택하여 호출 가능 
		// -> 하단 super.weight = weight; & this.height = height; 대신 사용 가능
		this.name = name;
		this.age = age;
		// super.weight = weight; // 부모인 Super의 값이므로 super.weight 혹은 this.weight로 작성 가능
		// this.height = height;
	}

	public void disp() {
		System.out.println("이름 = " + name);
		System.out.println("나이 = " + age);
		super.disp();
	}
		
	public static void main(String[] args) {
		ChildMain aa = new ChildMain("홍길동", 25, 73.5, 182.6);
		aa.disp();
		System.out.println("======================");
		
		Super bb = new ChildMain("코난", 13, 53.5, 156.6);
		bb.disp();

	}

}
