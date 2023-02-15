package sungJuk;

import java.util.ArrayList;
import java.util.Scanner;

public class SungJukUpdate implements SungJuk {
	
	@Override
	public void execute(ArrayList<SungJukDTO> arrayList) {
		System.out.println();
		Scanner scan = new Scanner(System.in);
		
		System.out.println("번호 입력 : ");
		int no = scan.nextInt();
		
		int sw = 0;
		for(SungJukDTO sungJukDTO : arrayList) {
			if(sungJukDTO.getNo() == no) {
				sw = 1;
				
				System.out.println(sungJukDTO);
				
				System.out.println();
				System.out.print("수정할 이름 입력 : ");
				String name = scan.next();
				System.out.print("수정할 국어 입력 : ");
				int kor = scan.nextInt();
				System.out.print("수정할 영어 입력 : ");
				int eng = scan.nextInt();
				System.out.print("수정할 수학 입력 : ");
				int math = scan.nextInt();
				
				sungJukDTO.setName(name);
				sungJukDTO.setKor(kor);
				sungJukDTO.setEng(eng);
				sungJukDTO.setMath(math);
				
				sungJukDTO.calc(); // 재계산
				
				System.out.println("수정하였습니다.");
				
			}
		}//for
		
		if(sw == 0) 
			System.out.println("업는 번호 입니다.");
		
		}
		
	

}
