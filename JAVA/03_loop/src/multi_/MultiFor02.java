package multi_;

public class MultiFor02 {

	public static void main(String[] args) {
		int dan=2, i;
		
		for(dan=2; dan<=9; dan++) { // for dan 시작
			
			for(i=1; i<=9; i++) { // for i 시작
				System.out.println(dan + "*" + i + "=" + dan*i);
			} // for i 끝
			System.out.println();
			
		} // for dan 끝
		
	}

}

/*
[문제] 구구단 2단 ~ 9단 만들기
2*1 = 2
2*2 = 4
...
2*9 = 18

3*1 = 3
3*2 =6
...
3*9 = 27

*/