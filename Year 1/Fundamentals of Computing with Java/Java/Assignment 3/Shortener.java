/*
 * Name: Matthew Price
 * Student number: 0924337
 */

import java.io.File;
import java.util.Scanner;
import java.io.*;


public class Shortener {
    // This class is only a starting point. You should complete all members
    // below, but you may also need to add other fields and methods to
    // finish the implementation as per the question on the assignment sheet.
    private File abbreviations;
    String[] temp = new String[2];
    
    /*
     * Default constructor that will load a default abbreviations text file.
     */
    public Shortener() {
        
        //file = new File ("abbreviations.txt");
        abbreviations = new File("abbreviations.txt");

    }
    
    /*
     * Constructor that will load the abbreviations file represented by the
     * File parameter.
     */
    public Shortener( File inAbbreviationsFile ) {
        
         abbreviations = inAbbreviationsFile;

    }
    
    /*
     * Constructor that will load the abbreviations file that the String 
     * parameter is a file path for.
     */
    public Shortener( String inAbbreviationsFilePath ) {
        
        String abbreviationsFilePath = inAbbreviationsFilePath;
        abbreviations = new File(abbreviationsFilePath);

    }
    
    /*
     * This method attempts to shorten a word by finding its abbreviation. If 
     * no abbreviation exists for this word, then this method will return the 
     * original (i.e., unshortened) word.
     * 
     * You may assume that words are always lower case.
     *
     * `inWord` should be a single word (no spaces). It may optionally be
     * followed by one of the five following punctuation characters:
     *   ,
     *   ?
     *   .
     *   !
     *   ;
     * If one of these characters is at the end of the word this method will
     * shorten the word (ignoring the punctuation) and return the shortened
     * word with the punctuation character at the end.
     * For example,
     *     shortenerObject.shortenWord( "hello?" )
     * should return
     *     "lo?"
     *
     * You may assume that words are always lower case.
     */
    public String shortenWord( String inWord ) {

            // try {
            //     FileReader reader = new FileReader (abbreviations);
            //     BufferedReader in = new BufferedReader ( reader );

            //     String s;
            //     while ( (s=in.readline() ) != null ){
            //         System.out.println(s);
            //     }

            //     in.close();

            // }catch ( FileNotFoundException e ){
            //     System.out.println( e );
            // }
            // catch ( IOException e ){
            //     System.out.println( e );
            // }


        String stringMatch = inWord.toLowerCase();
        try{
            Scanner abbreviationFile = new Scanner(abbreviations);

            abbreviationFile.useDelimiter(",|\\n");

            while (abbreviationFile.hasNext()) {
                String word = abbreviationFile.next();
                String replace = abbreviationFile.next();
                //System.out.println(word);
                //System.out.println(replace);
                //String[] temp = new String[2];
                temp[0] = word;
                temp[1] = replace;
                //System.out.println(temp[0] + ", " + temp[1]);

                if(temp[0].equals(stringMatch)){
                System.out.println(temp[1]);
                continue;
                }

                // else if (abbreviationFile.hasNext() != true){
                //     System.out.println(stringMatch);
                // }
   
            }

            if (abbreviationFile.hasNext() != true){
                System.out.println(stringMatch);
            }
        }

        catch ( FileNotFoundException e ){
            System.out.println( e );
        }
        
    return "T";
    }

    
    /*
     * Attempts to shorten a message by replacing words with their 
     * abbreviations. 
     *
     * You may assume that messages are always lower case.
     *
     * Punctuation characters (,?.!;) should be retained after shortening. See
     * `shortenWord( String inWord )` for more information.
     */
    public String shortenMessage( String inMessage ) {
        
        String message = (inMessage);
        String [] words = message.split("\u0020");
        for (int i = 0; i < words.length; i++){
            shortenWord(words[i]);
        }
    return "default";
    }
}