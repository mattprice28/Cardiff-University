/*
 * Name: Matthew Price
 * Student number: 0924337
 */

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import java.awt.GridLayout;

public class ShortenerFrame extends JFrame {
    // This class is only a starting point. You may wish to add members and 
    // fields to complete the implementation of this class as per the
    // question on the assignment sheet.
    
    // Constants
    private static final int FRAME_WIDTH = 400;
    private static final int FRAME_HEIGHT = 260;
    
    // Instance variables -- GUI components
    private JPanel panel;
    private JLabel instructionLabel;
    private JTextArea inputArea;
    private JTextArea outputArea;
    private JButton shortenButton;
    
    // Constructor
    public ShortenerFrame() {
        super();
        
        //
        // Set up the frame
        setSize( FRAME_WIDTH, FRAME_HEIGHT );
        
        //
        // Set up the panel and layout manager
        panel = new JPanel();
        GridLayout grid = new GridLayout( 0, 1 );  // a one-column layout
        panel.setLayout( grid );
        
        add( panel );  // add panel to the JFrame

        //
        // Set up and add components
        instructionLabel = new JLabel( "Enter text in the field below and click 'Shorten'" );
        panel.add( instructionLabel );
        
        inputArea = new JTextArea();
        panel.add( inputArea );
        inputArea.setLineWrap(true);
        String input = inputArea.getText();
        
        shortenButton = new JButton( "Shorten" );
        panel.add( shortenButton );
        shortenButton.addActionListener(new ActionListener())
        Action shorten = new Shortener();
        
        outputArea = new JTextArea();
        panel.add( outputArea );
        outputArea.setEditable(false);
        outputArea.setLineWrap(false);
        outputArea.setText(shortener.shortenMessage(input));
    }
}

