package basic;

class Test {
	int a = 10;
	static int b = 20;
	static String str;
	
}
// ----------------------
public class Variable02 {	// class : 객체형
	int a; // 전역 변수 필드(Field), 초기화된 값
	double b; // 필드
	static int c;

	public static void main(String[] args) {
		int a = 5;	// 지역 변수(local variable), 초기엔 garbage 값. 32bit
		System.out.println("지역변수 a = " + a);
		
		Variable02 v = new Variable02(); //메모리 생성
		// Variable02라는 클래스를 메모리에 잡아주세요!
		
		System.out.println("객체 = " + v);	
		System.out.println("필드 a = " + v.a);
		//System.out.println("필드 a = " + Variable02().a); 축약ver.
		// 메모리 생성 및 v. 안 해주면 지역변수만 나옴(지역 변수 영역 내에 있기 때문)
		
		System.out.println("필드 b = " + v.b);
		System.out.println("필드 c = " + c);
		
		Test t = new Test();
		// Test라는 클래스를 메모리에 잡아주세요!
		
		System.out.println("Test 클래스 a = " + t.a);
		System.out.println("Test 클래스 b = " + t.b);
		System.out.println("Test 클래스 str = " + t.str);

	}

}
