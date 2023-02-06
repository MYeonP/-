package operator;

public class Boxing {

	public static void main(String[] args) {
		int a = 25;
		double b = (double)a / 3; // Casting, 강제형 변환 / 자동형 변환
		
		String c = "25";
		
		//int d = (int)c; //error (기본형)객체형
		int d = Integer.parseInt(c);
		
		int e = 5;
		Integer f = e; //JDK 5.0, AutoBoxing (기본형 -> 객체형)
	   // 객체형     = 기본형
		//Integer f = new Integer(e); //JDK 5.0 이전에 사용
		
		Integer g = 5;
		int h = g; // JDK 5.0, unAutoBoxing (객체형 -> 기본형)
		//int h = g.intValue(); //JDK 5.0 이전에 사용
		

	}

}
