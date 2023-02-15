package collection;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class CollectionMain {

	@SuppressWarnings("all")	// 모든 경고 억제
	public static void main(String[] args) {
		Collection coll = new ArrayList();
		coll.add("호랑이");
		coll.add("사자");
		coll.add("호랑이");	// 중복을 허용함
		coll.add(25);	// 정수형 가능
		coll.add(43.8);	// 실수형 가능
		coll.add("기린");
		coll.add("코끼리");
		
		Iterator it = coll.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}// while
		
		// it.hasNext() : 항목이 있나요? (true) & 항목이 없나요? (false)
		// it.next() : 항목을 꺼내고 다음 항목으로 이동

	}

}
