package inheritance;

public class SubMain extends Super {
	private String name;
	private int age;
	
	SubMain(){
		System.out.println("SubMain 기본 생성자");
	}
	
	SubMain(String name, int age, double weight, double height) {
		this.name = name;
		this.age = age;
		super.weight = weight; // 부모인 Super의 값이므로 super.weight 혹은 this.weight로 작성 가능
		this.height = height;
	}
	public void output() {
		System.out.println("이름 = " + name);
		System.out.println("나이 = " + age);
		this.disp();
	}
	

	public static void main(String[] args) {
		SubMain aa = new SubMain("홍길동", 25, 73.5, 182.6);
		aa.disp(); //부모 메소드 호출
		System.out.println("-----------------------");
		aa.output();
		System.out.println("======================");
		
		Super bb = new SubMain("코난", 13, 53.5, 156.6);
		// bb.output(); => error!
		bb.disp();
		

	}

}


// 자식 클래스는 메모리 생성할 때 자기 것만 안 만든다
// - 부모 클래스 생성 후 자식(본인) 클래스를 생성함 