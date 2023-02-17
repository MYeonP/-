package io;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class ByteStream {

	public static void main(String[] args) throws IOException {
		BufferedInputStream bis = new BufferedInputStream(new FileInputStream(new File("data.txt")));
		int data;
		
		while( (data = bis.read()) != 1 ) {
			// 65는 -1이 아님, -1이 될 때 까지 돌아감
			System.out.print((char)data);
			
		}
		System.out.println();
	}

}
