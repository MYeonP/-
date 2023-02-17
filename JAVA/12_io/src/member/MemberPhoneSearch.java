package member;

import java.util.List;
import java.util.Scanner;

public class MemberPhoneSearch implements Member {

	@Override
	public void execute(List<MemberDTO> list) {
		System.out.println();
		Scanner scan = new Scanner(System.in);
		
		System.out.println("검색할 핸드폰 입력 : ");
		String phone = scan.next();
		
		int sw = 0;
		for(MemberDTO memberDTO : list) {
			if(memberDTO.getPhone().equals(phone)) {
				System.out.println("이름\t나이\t핸드폰\t\t주소");
				System.out.println(memberDTO);
				sw=1;
				
				break;
			}
		}
		
		if(sw == 0)
			System.out.println("검색한 핸드폰 번호가 없습니다.");

	}

}
