package com.apple;

import com.zoo.Zoo;	// Zoo를 호출해주기 위해 Zoo 클래스 임포트 해 줌

public class Apple {

	public static void main(String[] args) {
		System.out.println("빨간 사과");
		
		// Zoo 클래스의 tiger() 호출
		Zoo z = new Zoo();
		z.tiger();
		// z.giraffe(); -> protected void giraffe()는 다른 클래스에서 못 불러옴
		// z.elephant(); -> (default) void giraffe()는 다른 클래스에서 못 불러옴
		// z.lion(); -> private void lion()는 다른 클래스에서 못 불러옴

	}

}
