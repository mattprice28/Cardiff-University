/*
 * Name: Matthew Price
 * Student number: 0924337
 */

/*
 * A command-line application that shortens a message.
 */
import java.util.Scanner;

public class ShortenerUtility {
    public static void main(String []args){

        Shortener shortenMsg = new Shortener();

        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();

        System.out.println(shortenMsg.shortenMessage(input));
    } 
}