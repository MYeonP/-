package abstract_;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class Today {

	public static void main(String[] args) throws ParseException {
		Date date = new Date(); //시스템의 시간과 날짜를 가져옴
		System.out.println("오늘 날짜 : " + date);
		
		// 형식 지정 : 0000년 0월 0일
		SimpleDateFormat sdf = new SimpleDateFormat("y년 MM월 dd일 E요일 HH:mm:ss");
		System.out.println("오늘 날짜 : " + sdf.format(date));
		System.out.println();
		
		// 입력
		SimpleDateFormat input = new SimpleDateFormat("yyyyMMddHHmmss");
		Date birth = input.parse("19910716091415");	// String -> Date형 변환
		
		System.out.println("내 생일 = " + birth);
		System.out.println("내 생일 = " + sdf.format(birth));
		
		// Calendar cal = new Calendar(); - error
		
		// 기준은 시스템 날짜와 시간
		Calendar cal = new GregorianCalendar();//sub class
		Calendar cal2 = Calendar.getInstance();//메소드
		
		int year = cal.get(Calendar.YEAR);
		int month = cal.get(Calendar.MONTH) +1; // 1월 -> 0, 2월 -> 1, ... 
		int day = cal.get(cal.DAY_OF_MONTH);
		int week = cal.get(cal.DAY_OF_WEEK); // 일요일 -> 1, 월요일 -> 2,...
		
		String datOfweek;
		switch(week) { 
		case 1 : datOfweek = "일"; break;
		case 2 : datOfweek = "월"; break;
		case 3 : datOfweek = "화"; break;
		case 4 : datOfweek = "수"; break;
		case 5 : datOfweek = "목"; break;
		case 6 : datOfweek = "금"; break;
		case 7 : datOfweek = "토";
		}
		
		int hour = cal.get(Calendar.HOUR_OF_DAY);
		int minute = cal.get(Calendar.MINUTE); 
		int second = cal.get(Calendar.SECOND);
		System.out.println(year + "년 " + month + "월 " + day + "일");

	}

}
