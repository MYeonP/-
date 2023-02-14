package inheritance;

enum Color {
	RED, GREEN, BLUE	// 상수들의 집합체. 16라인처럼 해 줘도 되고 enum으로 정의해도 됨
}
// ==================================================
class Final {
	public final String FRUIT = "사과";
	public final String FRUIT2;
	
	public static final String ANMAL = "기린";
		// static : 시음식, 실행하자마자 메모리에 자동으로 생성. 따라서 new 해 줄 필요 없음
	public static final String ANMAL2;
	// static은 생성자에서 초기화가 안 된다
	
//	public static final int RED = 0;
//	public static final int GREEN = 1;
//	public static final int BLUE = 2;
	
	static {
		System.out.println("static 초기화 영역");
		ANMAL2 = "코끼리";
	}
	
	public Final() {
		System.out.println("기본 생성자");
		FRUIT2 = "딸기";	// 생성자로 초기값 입력 -> ctrl 스페이스바 눌러서 생성자 가져오기
	}
	
}

// =====================================================
public class FinalMain {

	public static void main(String[] args) {
		final int A = 10;	// a 변수 상수화 시키기 : final
		// A = 20; -> a의 에러가 뜬다. final 상수는 값을 변경할 수 없다
		System.out.println("A = " + A);
		
		final int B;	// B의 초기값을 안 줬음
		B = 30;	// 그래서 한 번의 기회를 주어서 값을 입력할 수 있음
		// B = 40; -> 두번째엔 에러 뜸
		System.out.println("B = " + B);
		
//		Final f = new Final();
//		System.out.println("FRUIT = " + f.FRUIT);
//		System.out.println("FRUIT2 = " + f.FRUIT2);
		
		System.out.println("ANIMAL = " + Final.ANMAL);
		System.out.println("ANIMAL2 = " + Final.ANMAL2);
		System.out.println();
		
		System.out.println("빨강 = " + Color.RED); // 빨강 = RED
		System.out.println("빨강 = " + Color.RED.ordinal()); // 빨강 = 0
		
		for(Color data : Color.values()) {
			System.out.println(data + "\t" + data.ordinal() );
		}

	}

}
