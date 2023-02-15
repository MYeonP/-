package collection;

class GenericTest<T> {	// 데이터형 Type
	private T a;

	public T getA() {
		return a;
	}

	public void setA(T a) {
		this.a = a;
	}
}

//===================================
public class GenericMain {

	public static void main(String[] args) {
		GenericTest<String> aa = new GenericTest<String>();
		aa.setA("홍길동");
		System.out.println("이름 = " + aa.getA());
		
		//aa.setA(25);
		GenericTest<Integer> bb = new GenericTest<Integer>();	
		// 기본형이 안 된다(int 불가). 반드시 클래스형으로!
		bb.setA(25);
		System.out.println("나이 = " + bb.getA());
		
		

	}

}
