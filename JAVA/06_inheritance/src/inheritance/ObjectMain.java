package inheritance;

class Test extends Object {
	
}
// ==================================================
class Sample { 
	@Override
	public String toString() {
		return getClass() + "@개바부";
	}
	
}

//==================================================

class Exam{
	private String name = "홍길동";
	@Override
	public String toString() {
		return super.toString();
	}
	
}

//==================================================
public class ObjectMain {

	public static void main(String[] args) {
		Test t = new Test();
		System.out.println("객체 t = " + t);
		System.out.println("객체 t = " + t.toString());
		System.out.println("객체 t = " + t.hashCode());
		System.out.println();
		
		Sample s = new Sample();
		System.out.println("객체 t = " + t.toString());
		System.out.println();
		
		Exam e = new Exam();
		System.out.println("객체 e = " + e.toString());
		System.out.println();
		
		String aa = "apple";
		System.out.println("객체 aa = " + aa); // 문자열
		System.out.println("객체 aa = " + aa.toString());
		System.out.println("객체 aa = " + aa.hashCode());
		System.out.println();
		
		String bb = new String("apple");
		String cc = new String("apple");
		System.out.println("bb==cc : " + (bb==cc));
		System.out.println("bb.equals(cc) : " + bb.equals(cc));
		System.out.println();
		
		Object dd = new String("apple");
		Object ee = new String("apple");
		System.out.println("dd==ee : " + (dd==ee)); // 주소 - false
		System.out.println("dd.equals(ee) : " + dd.equals(ee)); // 주소 - false
		System.out.println();
		
		Object ff = new String("apple");
		Object gg = new String("apple");
		System.out.println("ff==gg : " + (ff==gg)); // 주소 - false
		System.out.println("ff.equals(gg) : " + ff.equals(gg)); // 문자열 - false
		System.out.println();
		
	}

}

/*

class Object {
   public String toString() {}         클래스명@16진수
   public int hashCode() {}         10진수
   public boolean equals(Object ob){}   참조값 비교
}

class String
   public String toString() {}         문자열
   public int hashCode() {}         10진수 (믿으면 안된다)
                               -> 표기할 수 있는 문자열은 무한대이기 때문에 10진수로는 다 표기할 수 없다.
   public boolean equals(Object ob){}   문자열 비교
}


*/
