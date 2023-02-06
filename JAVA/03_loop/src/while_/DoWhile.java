package while_;

public class DoWhile {

	public static void main(String[] args) {
		// 1 2 3 4 5 6 7 8 9 10
		int a = 0;
		do {
			a ++;
			System.out.print(a + " ");
		}while(a<10);
		System.out.println();
		
		// A B C D E F G ~~~ X Y Z
		// 한 줄에 7개씩 출력하시오 : 7의 배수
		char ch = 'A';
		int count = 0;
		do {
			System.out.print(ch + " ");
			ch ++; // B부터 시작됨
			
			count ++; // 개수 : 1 2 3
			if(count%7 == 0) System.out.println(); 
			// count가 7의 배수입니까?(7로 나누어 나머지가 0입니까?)
		}while(ch<='Z');
		

	}

}
