package com.zoo;

public class Zoo2 {

	public static void main(String[] args) {
		Zoo z = new Zoo();
		z.tiger();
		z.giraffe();
		z.elephant();
		// z.lion();  -> private void lion()는 다른 클래스에서 못 불러옴
	}

}
