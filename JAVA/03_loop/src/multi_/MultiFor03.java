package multi_;

public class MultiFor03 {

	public static void main(String[] args) {
		int dan=2, i;
		
		for(i=1; i<=9; i++) { // for i 시작
			
			for(dan=2; dan<=9; dan++) { // for i 시작
				
				System.out.print(dan + "*" + i + "=" + dan*i + "\t");
				
				if(dan%9 == 0) System.out.println();
			} // for dan 끝
			
		} // for i 끝

	}

}

/*
[문제] 구구단 2단 ~ 9단 만들기

2*1 = 2	3*1 = 3	4*1 = 4 5*1 = 5	6*1 =6	7*1 = 7	8*1	= 8	9*1 = 9
2*2 = 4	3*2 = 6	4*2 = 8
...


*/