package operator;

public class Operator05 {

	public static void main(String[] args) {
		boolean a = 25 > 36;
		System.out.println("a = " + a);
		System.out.println("!a = " + !a);
		System.out.println();
		
		String b = "apple";	//literal 생성 가능
		String c = new String("apple");
		
		String result = b == c ? "같다" : "다르다"; // 주소 비교
		System.out.println("b == c : " + result); 
		System.out.println("b != c : " + (b != c ? "참" : "거짓")); //부정
		System.out.println();
		
		String result2 = b.equals(c) ? "같다" : "다르다"; // 문자열 비교
		System.out.println("b.equals(c) : " + result2);
		System.out.println("!b.equals(c) : " + ((!b.equals(c) ? "참" : "거짓"))); // 함수는 부정 느낌표 맨 앞으로
		System.out.println();
		
		
	}

}
