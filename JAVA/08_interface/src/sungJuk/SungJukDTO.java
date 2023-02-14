package sungJuk;

public class SungJukDTO {	// 1인분
	private int no;
	private String name;
	private int kor, eng, math, tot;
	private double avg;
	
	public SungJukDTO(int no, String name, int kor, int eng, int math) {
		this.no = no;
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
	}
	
    public void calc() {
        tot = kor + eng + math;
        avg = (double) tot / 3;
    }

    public int getNumber() {
        return no;
    }

    public String getName() {
        return name;
    }

    public int getKor() {
        return kor;
    }

    public int getEng() {
        return eng;
    }

    public int getMath() {
        return math;
    }

    public int getTotal() {
        return tot;
    }

    public double getAvg() {
        return avg;
    }
	
	@Override
	public String toString() {
		return no + "\t" + name + "\t" + kor + "\t" + eng + "\t" + math + "\t" + tot + "\t" + avg ;
	}
}
