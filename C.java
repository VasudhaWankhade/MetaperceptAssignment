package quefour;

public class C {
	public static int multiply() {
		int[] last = B.LastDigits(A.AcceptNum(45766, 32456));
		int mul = 1;
		for (int i : last) {
			mul = mul * i;
		}
		return mul;
	}
	public static void main(String[] args) {
		int multiplication = C.multiply();
		System.out.println("Product of last two dgits is : "+ multiplication);
	}
}
