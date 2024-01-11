package demo;
import java.util.*;
public class assign6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Employee ID");
		int a=sc.nextInt();
		System.out.println("Enter the Employee name");
		String n=sc.next();
		System.out.println("Enter the salary");
		int s=sc.nextInt();
		System.out.println("Enter the address");
		String address=sc.next();
		System.out.println("Enter the contact information");
		long contact=sc.nextLong();
		System.out.println("Enter the Gender Details");
		String gender=sc.next();
		
		System.out.print(a+" "+n+" "+s+" "+address+" "+contact+" "+gender);
		

	}

}
