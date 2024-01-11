package demo;
import java.util.*;
public class assign2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the first Number");
		int a=sc.nextInt();
		System.out.println("Enter the second Number");
		int b=sc.nextInt();
		System.out.println("Enter the third Number");
		int c=sc.nextInt();
		
		if(a>b && a>c){
			System.out.println(a+" is the biggest Number");
		}
		else if (b>a && b>c){
			System.out.println(b+"is the biggest Number");
		}
		else{
			System.out.print(c+"is the biggest number");
		}

	}

}
