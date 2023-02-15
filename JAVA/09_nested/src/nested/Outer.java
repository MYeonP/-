package nested;

public class Outer {
	private String name;
	
	public void output() {
		Inner in = new Inner();
		System.out.println("이름 = " + name + "\t나이 = " + in.age);
	}
	
	class Inner {	//Outer$Inner.class : 중첩 클래스!
		private int age;
		
		public void disp() {
			System.out.println("이름 = " + Outer.this.name + "\t나이 = " + this.age);
		}
	}

	public static void main(String[] args) {
		Outer ou = new Outer();
		ou.name = "홍길동";
		System.out.println("이름 = " + ou.name);
		System.out.println();
		
		Outer.Inner in2 = ou.new Inner();
		in2.age = 25;
		in2.disp();
		System.out.println();
		
		Outer.Inner in3 = ou.new Inner();
		in3.age = 30;
		in3.disp();
		System.out.println();
		
		Outer.Inner in4 = new Outer().new Inner();
		//in4.name = "코난";
		in4.age = 35;
		in4.disp();
		

	}

}
