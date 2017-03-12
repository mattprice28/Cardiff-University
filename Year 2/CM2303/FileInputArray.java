import java.io.*;
import java.util.Arrays;
//Reads integers from a file
//The file name must be passed as an argument when running the code 
//Reads numbers into an array with dynamic dimensions

public class FileInputArray {


 public static void main(String args[]) throws IOException{
	 int num[] = new int[10];
	 int k = 10;
	 int count = 0;
	 BufferedReader input;
	 String line;

	 input = new BufferedReader(new FileReader("randomSmall.txt"));
	 line = input.readLine();

	 while(line != null)
	 {
	 	//dynamic array dimensions
	 	//makes array storage bigger, if needed
		 if (count==(num.length-1)) {
			 int n = num.length;
			 int[] original = num;
			 num = new int[n*2];
			 for (int i = 0;i < n;i++)
			   num[i] = original[i];
			 original = null;
		 }
		 num[count] = Integer.parseInt(line);
		 System.out.println(num[count]);
		 line = input.readLine();
		 count++;
	 }
	 input.close();
	 int[] original = num;
	 num = new int[count];
	 for (int i = 0;i < count;i++)
	 	num[i] = original[i];
	 original = null;

	 insertionSort(num);
        System.out.println("\nAfter Sorting: ");
        printArray(num);

    }

	 private static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int valueToSort = arr[i];
            int j = i;
            while (j > 0 && arr[j - 1] > valueToSort) {
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = valueToSort;
        }
    }

    public static void printArray(int[] B) {
        System.out.println(Arrays.toString(B));
    }
 }