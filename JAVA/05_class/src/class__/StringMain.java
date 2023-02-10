package class__;

public class StringMain {

	public static void main(String[] args) {
		String a = "apple";		// literal 생성 가능 -> ex) a = 클@100
		String b = "apple";
		// String a와 클래스 주소가 동일하다 ex) a = 클@100 & b = 클@100
		if(a == b) System.out.println("a와 b의 참조값은 같다");
		else System.out.println("a와 b의 참조값은 다르다");
		if(a.equals(b)) System.out.println("a와 b의 문자열은 같다");
		else System.out.println("a와 b의 문자열은 다르다");
		System.out.println();
		
		String c = new String("apple");	// New 클래스 주소 생성 ex) c = 클@300
		String d = new String("apple");	//  New 클래스 주소 또 생성 ex) d = 클@500
		if(c == d) System.out.println("c와 d의 참조값은 같다");
		else System.out.println("c와 d의 참조값은 다르다");
		if(c.equals(d)) System.out.println("c와 d의 문자열은 같다");
		else System.out.println("c와 d의 문자열은 다르다");
		System.out.println();
		
		String e = "오늘 날짜는 " + 2023 + 2 + 10;
		System.out.println("e = " + e);	// e = 오늘 날짜는 2023210
		
		// 문자열은 편집이 안 된다 -> 메모리에 4번의 생성이 일어남("오늘 날짜는 ", 2023, 2, 10)
		// 맨 처음이 문자열이므로 +는 결합, 결합으로 시작되면 마지막까지 결합으로 되어 숫자끼리는 덧셈이 안 됨
		// JVM에 의해서 삭제 시 Garbage Collector로 보낸다
		// Garbage Collector가 실행되면 컴퓨터는 멈춘다
		
		System.out.println("문자열 크기 = " + e.length());
		
		for(int i=0; i<e.length(); i++) {
			System.out.println(i + " : " + e.charAt(i));
		} // for i
		
		System.out.println("부분 문자열 추출 = " + e.substring(7));
		System.out.println("부분 문자열 추출 = " + e.substring(7,11));
		
		System.out.println("대문자 변경 = " + "Hello".toUpperCase());
		System.out.println("대문자 변경 = " + "Hello".toLowerCase());
		
		System.out.println("문자열 검색 = " + e.indexOf("짜"));
		System.out.println("문자열 검색 = " + e.indexOf("날짜"));
		System.out.println("문자열 검색 = " + e.indexOf("개바부")); //-1
		
		System.out.println("문자열 치환 = " + e.replace("날짜", "일자"));
		
		
	


	}

}


