import java.util.Scanner;

public class QueOne {
	public static String longWord(String sen) {
		String[] arr = sen.split(" ");
		String ll = "";
		for (String sr : arr) {
			if (sr.length() > ll.length()) {
				ll = sr;
			}
		}
		return ll;
	}

	public static void main(String[] args) {
		String str = "dummy text of the printing and typesetting industry";
		String longWord = QueOne.longWord(str);
		System.out.println("Longest word is : " + longWord);
	}

}
