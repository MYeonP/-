package com.zoo.safari;

import com.zoo.Zoo;

public class Safari {

	public static void main(String[] args) {
		Zoo z = new Zoo();
		z.tiger();
		// z.giraffe();
		// z.elephant();
		// z.lion(); -> 패키지가 다르면 public 외에 아무것도 못 봄!
		System.out.println();
		
		Safari s = new Safari();
		s.tiger();
		s.giraffe();
		s.elephant();
		s.lion();

	}

}
