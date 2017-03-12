import java.io.*;
import java.util.Arrays;
//Reads integers from a file
//The file name must be passed as an argument when running the code 
//Reads numbers into an array with dynamic dimensions

public class ReadAndCountingSort {


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

	 long startTime = System.nanoTime(); //Start timing
	 	for(int t = 0; t < 999; t++) {   //Repeat sort 1000 times to achieve better results
	 //System.out.println("\nBefore Sorting: ");
        //printArray(num);	
	 countingSort(num);
        //System.out.println("\nAfter Sorting: ");
        //printArray(num);
	}
	 long endTime = System.nanoTime(); // stop timing

    long duration = (endTime - startTime); //calculate duration
    System.out.println();
    System.out.println("\nAverage Time Taken: " + (duration/1000)); // work out average duration

    }

	private static void countingSort(int[] arr){
        int min=arr[0];								// Find max and min values
        int max=arr[0];
        for(int ii=0;ii<arr.length;ii++){
            if(arr[ii]<min){
                min=arr[ii];
            }
            else if(arr[ii]>max){
                max=arr[ii];
            }
        }
	int[] count= new int[max - min + 1];    //Create empty array to count values
	for(int number : arr){
		count[number - min]++;
	}
	int z= 0;
	for(int i= min;i <= max;i++){          //Create array to hold sorted values
		while(count[i - min] > 0){
			arr[z]= i;
			z++;
			count[i - min]--;
			//System.out.println("\nIntermediate stage");
            //printArray(arr);				//Decrease count once value is used
		}
	}
}


    public static void printArray(int[] B) {
        System.out.println(Arrays.toString(B));
    }
 }