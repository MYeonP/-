package abstract_;

public abstract class AbstractTest { // POJO(Plain Old Java Object)
	protected String name;
	// 생성자, setter, getter 생성 필수
	
	public AbstractTest() {
		
	}
	
	public AbstractTest(String name) {
		super();
		this.name = name;
	}
	
	public String getName() {	//구현
		return name;
	}

//	public void setName(String name) {	//구현
//		this.name = name;
//	}
	
	public abstract void setName(String name); // 추상 메소드

}
