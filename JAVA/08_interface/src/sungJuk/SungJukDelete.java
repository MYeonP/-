package sungJuk;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class SungJukDelete implements SungJuk {

	@Override
	public void execute(ArrayList<SungJukDTO> arrayList) {
		System.out.println();
		Scanner scan = new Scanner(System.in);
		
		System.out.print("삭제 할 이름 입력 : ");
		String name = scan.next();
		
		int count = 0;
//		for(int i=0; i<arrayList.size(); i++) {
//			if(arrayList.get(i).getName().equals(name)) {
//				arrayList.remove(i);
//				count++; //1 2 3 
//			}
//		}//for		
		
//		java.util.ConcurrentModificationException 에러 발생
//		for(SungJukDTO sungJukDTO : arrayList) {
//			if(sungJukDTO.getName().equals(name)) {
//				arrayList.remove(sungJukDTO);
//				count++; //1 2 3 
//			}
//		}//for
		
		Iterator<SungJukDTO> it = arrayList.iterator();
		while(it.hasNext()) {
			SungJukDTO sungJukDTO = it.next();
			
			if(sungJukDTO.getName().equals(name)) {
				it.remove(); //it.next()가 반환하는 항목을 지운다.
				count++;
			}
		}//while
	
		if(count == 0) 
			System.out.println("회원의 정보가 없습니다");
		else
			System.out.println(count+"건을 삭제하였습니다");
	}

}
















