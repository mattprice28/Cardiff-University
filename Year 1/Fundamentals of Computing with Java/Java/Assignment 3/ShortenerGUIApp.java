/*
 * Name: Matthew Price
 * Student number: 0924337
 */

import javax.swing.JFrame;

public class ShortenerGUIApp {
    public static void main( String[] args ) {
        JFrame frame = new ShortenerFrame();
        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
        frame.setVisible( true );
        frame.setTitle("Shortener App");
    }
}