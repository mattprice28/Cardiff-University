import java.io.*;
import java.util.Arrays;
//Reads integers from a file
//The file name must be passed as an argument when running the code 
//Reads numbers into an array with dynamic dimensions

public class ReadAndInsertionSort {

 public static void main(String args[]) throws IOException{
	 int num[] = new int[10];
	 int k = 10;
	 int count = 0;
	 BufferedReader input;
	 String line;

	 input = new BufferedReader(new FileReader("descending100000.txt"));
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
		 //System.out.println(num[count]);
		 line = input.readLine();
		 count++;
	 }
	 input.close();
	 int[] original = num;
	 num = new int[count];
	 for (int i = 0;i < count;i++)
	 	num[i] = original[i];
	 original = null;

	 long startTime = System.nanoTime();
	 	for(int t = 0; t < 999; t++) {
	 	//System.out.println("\nBefore Sorting: ");
        //printArray(num);	
	 insertionSort(num);
        //System.out.println("\nAfter Sorting: ");
        //printArray(num);
	}
	 long endTime = System.nanoTime();

    long duration = (endTime - startTime);
    System.out.println();
    System.out.println("\nAverage Time Taken: " + (duration/1000));


    }

	 private static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {				//loop through array
            int valueToSort = arr[i];						//select value
            int j = i;
            while (j > 0 && arr[j - 1] > valueToSort) {		// check value of selected number against other values
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = valueToSort;
            //System.out.println("\nIntermediate stage");
            //printArray(arr);							//Place in correct position
        }
    }

    public static void printArray(int[] B) {
        System.out.println(Arrays.toString(B));
    }  
 }