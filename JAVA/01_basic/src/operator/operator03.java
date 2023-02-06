package operator;

public class operator03 {

	public static void main(String[] args) {
		int a = 5;
		a += 2; // a = a+2;
		a *= 3; // a = a*2;
		a /= 5; // a = a/2;
		System.out.println("a = " + a); // a = 4

		a++;
		System.out.println("a = " + a); // a = 5
		
		int b = a++;
		System.out.println("a = " + a + " b = " + b);
		
		int c = ++a * b--;
		System.out.println("a = " + a + " b = " + b + " c = " + c);
		
		System.out.println("a++ = " + a++);
		
		System.out.println("a = " + a);

	}

}
