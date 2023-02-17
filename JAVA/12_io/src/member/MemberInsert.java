package member;

import java.util.List;
import java.util.Scanner;

public class MemberInsert implements Member {
	
	public void execute(List<MemberDTO> list) {
		System.out.println();
		Scanner scan = new Scanner(System.in);
		
		System.out.print("이름 입력 : ");
		String name = scan.next();
		System.out.print("나이 입력 : ");
		int age = scan.nextInt();
		System.out.print("핸드폰 입력 : ");
		String phone = scan.next();
		System.out.print("주소 입력 : ");
		String address = scan.next();
		
		MemberDTO memberDTO = new MemberDTO(name, age, phone, address );
		
		list.add(memberDTO);
		
		System.out.println("입력 완료");
		
		
	}
	
	

}
