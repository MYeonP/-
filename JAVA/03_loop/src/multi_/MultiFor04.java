package multi_;

public class MultiFor04 {

	public static void main(String[] args)
	{
		for(int i = 2; i <= 9; i=i+3) {
			for(int j = 1; j <= 9; j++) {
				for(int dan = i; dan < i + 3; dan++) {
					if(dan == 10) {
						break;
					}
					System.out.print(dan + " * " + j + " = " + dan * j + "\t");
					
				}
				System.out.println();
			}
			System.out.println();
		}
	}
}


/*
[문제] 2~9단까지 출력하되 3개씩 끊어서 출력 하시오
3중 for문을 사용하세요 (3중 for문, if)

2*1=2	3*1=3	4*1=4
2*2=4	3*2=6	4*2=8
2*3=6	3*3=9	4*3=12
2*4=8	3*4=12	4*4=16
2*5=10	3*5=15	4*5=20
2*6=12	3*6=18	4*6=24
2*7=14	3*7=21	4*7=28
2*8=16	3*8=24	4*8=32
2*9=18	3*9=27	4*9=36

*/