package nested;

public abstract class AbstractTest { // POJO 형식(기본, 오리지널)
	String name;

	public String getName() {
		return name;
	}

	public abstract void setName(String name); // 추상 메소드로 설정  {
//		this.name = name;
//	}
// 추상 메소드를 가지고 있으면 그 클래스는 추상 클래스여야 한다.
// 반대로 추상 클래스는 추상 메소드가 있을 수도 있고 없을 수도 있다.
// 즉, 추상 메소드가 있으면 클래스는 무조건 추상 클래스.
// abstract : 추상 설정



}
