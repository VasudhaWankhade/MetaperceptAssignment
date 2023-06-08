
public class QueFive {
public static void CheckEmail(String email) {
	String validChar = "^+@+[A-Za-z0-9+._-]+$";
	if(email.contains("^[A-Za-z0-9+._-]+@+[gmail.com]+$")) {
		System.out.println("Valid Email Id");
	}
	else {
		System.out.println("Invalid Email Id");
	}
}
public static void main(String[] args) {
	QueFive.CheckEmail("abcd@gmail.com");
}
}
