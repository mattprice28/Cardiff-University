import java.io.*;
import java.util.Arrays;
//Reads integers from a file
//The file name must be passed as an argument when running the code 
//Reads numbers into an array with dynamic dimensions

public class ReadAndSelectionSort {


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

	 countingSort(num);
        //System.out.println("\nAfter Sorting: ");
        //printArray(num);

    }

	 private static void countingSort(int[] arr) {
        // array to be sorted in, this array is necessary
        // when we sort object datatypes, if we don't, 
        // we can sort directly into the input array     
        int[] aux = new int[arr.length];

        // find the smallest and the largest value
        int min = arr[0];
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) min = arr[i];
            else if (arr[i] > max) max = arr[i];
        }

        // init array of frequencies
        int[] counts = new int[max - min + 1];

        // init the frequencies
        for (int i = 0;  i < arr.length; i++) {
            counts[arr[i] - min]++;
        }

        // recalculate the array - create the array of occurences
        counts[0]--;
        for (int i = 1; i < counts.length; i++) {
            counts[i] = counts[i] + counts[i-1];
        }

        // Sort the array right to the left
        // 1) look up in the array of occurences the last occurence of the given value
        // 2) place it into the sorted array
        // 3) decrement the index of the last occurence of the given value
        // 4) continue with the previous value of the input array (goto: 1), terminate if all values were already sorted
        for (int i = arr.length - 1; i >= 0; i--) {
            aux[counts[arr[i] - min]--] = arr[i];
        }

        return aux;
    }
       long endTime = System.nanoTime();

    long duration = (endTime - startTime);
    System.out.println();
    System.out.println("\nAverage Time Taken: " + (duration/1000));
}

    public static void printArray(int[] B) {
        System.out.println(Arrays.toString(B));
    }
 }