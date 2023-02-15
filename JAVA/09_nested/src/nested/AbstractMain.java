package nested;

public class AbstractMain{

	public static void main(String[] args) { // main + ctrl 스페이스바 하면 나타낼 수 있음
		AbstractTest at = new AbstractTest() {	//익명 inner 클래스

			public void setName(String name) {	//구현
				this.name = name;
			}
		};	// 키다리 아저씨...
		
		InterA in = new InterA() {
			public void aa() {}
			public void bb() {};
		};
		
		AbstractExam ae = new AbstractExam() {
			// 추상 메소드가 없기 때문에 원하는 메소드를 골라서 Override
		};
		
	}
	

}
