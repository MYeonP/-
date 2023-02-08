package class_;

class Person{	// 메뉴판 시작
	private String name;	// 필드, 초기값 ( = null; 로 잡혀있다)
	private int age; // = 0;
	// private로 캡슐화(가리기)
	
	public void setName(String n) { // 메소드 구현하기 : public 결과형 메소드명(인수형 인수)
		name = n;
	}
	
	public void setAge(int a) { // 메소드 구현
		age = a;
	}
	
	public void setData(String n, int a) { // 메소드 구현
		name = n;
		age = a;
	}
	public void setData() {}	//위 함수와 쌍둥이 함수(overload)
	
	public String getName() {
		return name; // 반환값
	}
	
	public int getAge() {
		return age; // 반환값
	}
	
} // 메뉴판 짜기 완성!

// ---------------
public class PersonMain {

	public static void main(String[] args) {
		Person a;	// 객체 선언
		a = new Person();	//생성
		
		System.out.println("객체 a = " + a);
		a.setName("홍길동");	//호출 - 호출한 함수는 반드시 제자리로 돌아온다.
		a.setAge(25); //호출
		
		System.out.println("이름 = " + a.getName() + "\t 나이 = "+a.getAge());
		
		Person b = new Person();
		System.out.println("객체 b = " + b);
		b.setName("코난");	//호출 - 호출한 함수는 반드시 제자리로 돌아온다.
		b.setAge(13); //호출
		
		System.out.println("이름 = " + b.getName() + "\t 나이 = "+b.getAge());
		
		Person c = new Person();
		System.out.println("객체 c = " + c);
		c.setData("둘리", 100);	//호출 - 호출한 함수는 반드시 제자리로 돌아온다.
		System.out.println("이름 = " + c.getName() + "\t 나이 = "+c.getAge());

		Person d = new Person();
		System.out.println("객체 d = " + d);
		d.setData();	//호출 - 호출한 함수는 반드시 제자리로 돌아온다.
		System.out.println("이름 = " + d.getName() + "\t 나이 = "+d.getAge());
	}

}
