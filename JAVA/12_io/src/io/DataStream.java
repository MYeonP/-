package io;

import java.io.*;

public class DataStream {
    public static void main(String[] args) throws IOException { // IOException이 FileNotFoundException의 부모
        try {
    	// 파일 출력
    	DataOutputStream dataOutputStream = new DataOutputStream(new FileOutputStream("result.txt"));
//        FileOutputStream fileOutputStream = new FileOutputStream("result.txt");
//        DataOutputStream dataOutputStream = new DataOutputStream(fileOutputStream);

        dataOutputStream.writeUTF("홍길동");
        dataOutputStream.writeInt(25);
        dataOutputStream.writeDouble(185.3);

        dataOutputStream.close(); // 반드시 close

        // 파일 읽기
        DataInputStream dataInputStream = new DataInputStream(new FileInputStream("result.txt"));
        String name = dataInputStream.readUTF();
        int age = dataInputStream.readInt();
        double height = dataInputStream.readDouble();
        
        System.out.println("이름 = " + name);
        System.out.println("나이 = " + age);
        System.out.println("키 = " + height);
        
        dataInputStream.close();
        
    }catch(IOException e) {
    	e.printStackTrace();
    }
        
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    }
}
