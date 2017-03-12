import java.io.*;
import java.util.Random;
//Writes integers to a file
//The file name must be supplied as an argument when running the code 

public class FileOutput {


	public static void main(String args[]) throws IOException{
		PrintWriter output;
		Random rand = new Random();

		for (int t=10; t<1000000; t=(t*10)) {

	 		output = new PrintWriter(new FileWriter("random" + t + ".txt"));
	 		for(int i=0; i<t; i++) {
			output.println(rand.nextInt(t)); // random
			//output.println(i); // ascending order
			//output.println(t - (i+1)); // descending order
			}
		
		output.close();
		
		}
	}
}