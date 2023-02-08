package class_;

public class SungJukMain02 {

	public static void main(String[] args) {
		SungJuk aa = new SungJuk();		// 1:1 관계
		SungJuk bb = new SungJuk();		// 똑같은 SungJuk(); 이지만
		SungJuk cc = new SungJuk();		// 종속은 각각 aa, bb, cc. 각각의 객체!
		// 세 개의 클래스가 만들어졌다(aa 클래스, bb 클래스, cc 클래스)
		
		SungJuk[] ar = new SungJuk[3]; //객체 배열
		ar[0] = new SungJuk(); // 클래스 생성
		ar[0].setData("홍길동", 91, 95, 100); // 호출"
		
		ar[1] = new SungJuk(); // 클래스 생성
		ar[1].setData("프로도", 100, 89, 75); // 호출"
		
		ar[2] = new SungJuk(); // 클래스 생성
		ar[2].setData("죠르디", 75, 80, 48); // 호출"

		for(int i = 0; i <ar.length; i++) {
			ar[i].calc();
			System.out.println(ar[i].getName() + "\t"
					   		+ ar[i].getKor() + "\t"
					   		+ ar[i].getEng() + "\t"
					   		+ ar[i].getMath() + "\t"
					   		// + String.format("%.2f", ar[0].getAvg()) + "\t"
					   		+ ar[i].getAvg() + "\t"
					   		+ ar[i].getGrade());
		}
		
//		ar[0] = new SungJuk(); // 클래스 생성
//		ar[0].setData("홍길동", 91, 95, 100); // 호출"
//		ar[0].calc();
//		System.out.println(ar[0].getName() + "\t"
//				   + ar[0].getKor() + "\t"
//				   + ar[0].getEng() + "\t"
//				   + ar[0].getMath() + "\t"
//				   // + String.format("%.2f", ar[0].getAvg()) + "\t"
//				   + ar[0].getAvg() + "\t"
//				   + ar[0].getGrade() + "\t");
//		
//		ar[1] = new SungJuk(); // 클래스 생성
//		ar[1].setData("프로도", 100, 89, 75); // 호출"
//		ar[1].calc();
//		System.out.println(ar[1].getName() + "\t"
//				   + ar[1].getKor() + "\t"
//				   + ar[1].getEng() + "\t"
//				   + ar[1].getMath() + "\t"
//				   // + String.format("%.2f", ar[0].getAvg()) + "\t"
//				   + ar[1].getAvg() + "\t"
//				   + ar[1].getGrade() + "\t");
//		
//		ar[2] = new SungJuk(); // 클래스 생성
//		ar[2].setData("죠르디", 75, 80, 48); // 호출"
//		ar[2].calc();
//		System.out.println(ar[2].getName() + "\t"
//				   + ar[2].getKor() + "\t"
//				   + ar[2].getEng() + "\t"
//				   + ar[2].getMath() + "\t"
//				   // + String.format("%.2f", ar[2].getAvg()) + "\t"
//				   + ar[2].getAvg() + "\t"
//				   + ar[2].getGrade() + "\t");
				
				
	}

}
