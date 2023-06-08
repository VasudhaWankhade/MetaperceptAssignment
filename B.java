package quefour;

public class B {
	public static int[] LastDigits(int[] arr) {
		int[] arrB = new int[2];
		for (int i = 0; i < arr.length; i++) {
			for(int j=0;j<arrB.length;j++) {
				if(i==j) {
					arrB[i]=arr[j]%10;
				}
			}
		}
		return arrB;
	}

}
