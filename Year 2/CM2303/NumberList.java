import java.util.Random;
import java.io.*;

public class NumberList {


    private static int[] anArray;

     public static int[] list() {
    anArray = new int[100];
    for(int i=0;i<anArray.length;i++)
    {
        anArray[i] = randomFill();
    }
    return anArray;
}

    public static void print() throws IOException{
     PrintWriter output;

     output = new PrintWriter(new FileWriter("test.txt"));{
        for(int n: anArray){
        output.println(n+" ");
        }
        output.close();
        }
    }


    public static int randomFill(){

    Random rand = new Random();
    int randomNum = rand.nextInt(100);
    return randomNum;
    }


    }