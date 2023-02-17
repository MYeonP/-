package io;

import java.io.Serializable;

public class PersonDTO implements Serializable { //객체 직렬화
	private String name;
	private int age;
	private double height;
	
	public PersonDTO(String name, int age, double height) {
		super();
		this.name = name;
		this.age = age;
		this.height = height;
	} // sours -> Generate Constructor Using Field

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}// sours -> Generate Getter and Setter
	
	
	
	

}
