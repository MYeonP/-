package basic;

public class Variable01 {

	public static void main(String[] args) {
		System.out.println(Integer.MIN_VALUE + ", " + Integer.MAX_VALUE);
		System.out.println(Long.MIN_VALUE + ", " + Long.MAX_VALUE);
		System.out.println();
		
		boolean a;
		a = 25 > 36;
		
		System.out.println("a = " + a);
		
		char b;
		b = 'A'; // 65, 0100 0001
		System.out.println("b = " + b);
		
		char c;
		c = 65;
		System.out.println("c = " + c); // 문자형 함수 char이라 A로 출력 
		
		byte d = 0; // 1byte, 8bit, -128 ~ +127 초기값인 0을 주면 에러 발생하지 않음
		// d = 128; -> error
		System.out.println("d = " + d);
		
		int e;
		e = 65; // 0100 0001
		System.out.println("e = " + e);
		
		int f;
		f = 'A';
		System.out.println("f = " + f); // 정수형 함수 int라 65로 출력
		
		long g;
		g = 25L; // 25L은 long형 상수(데이터)
		System.out.println("g = " + g);
		
		float h;
		// h =43.8; // 43.8은 double형 상수
		// h = (float)43.8; // 강제형 변환	
		h = 43.8F; // 43.8은 float형 상수
		System.out.println("h = " + h);	
		
	}

}
