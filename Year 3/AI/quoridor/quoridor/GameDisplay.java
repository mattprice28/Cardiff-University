package quoridor;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;
import java.util.Set;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 *
 * @author steven
 */
public class GameDisplay {
    
    private JFrame frame;
    private GameState2P current;
    private int nrRows;
    private int width;
    private int height;
    private int cellSize =  50;    
    private Graphics2D bufferGraphics;
    private Graphics2D screenGraphics;
    BufferedImage bufferImage;
    BufferedImage screenImage;   
    
    public GameDisplay(GameState2P state){        
        width = state.getWidth() * cellSize;
        height = state.getHeight() * cellSize;   
        nrRows = state.getHeight();        
        initFrame();        
        updateState(state);
    }
    
    private void initFrame(){
       
        bufferImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
        screenImage  = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
        bufferGraphics = bufferImage.createGraphics();
        screenGraphics  = screenImage.createGraphics();        
        
        RenderingHints hints = new RenderingHints(RenderingHints.KEY_ANTIALIASING,
                                                  RenderingHints.VALUE_ANTIALIAS_ON);
        hints.put(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
        bufferGraphics.addRenderingHints(hints);
        
        ImageIcon icon = new ImageIcon(screenImage);
        JLabel draw = new JLabel(icon);        
        frame = new JFrame();
        frame.setContentPane(draw);        
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);                   
        frame.setTitle("Quoridor");        
        frame.pack();
        frame.requestFocusInWindow();
        frame.setVisible(true); 
    }
    
    public void updateState(GameState2P newState){        
        current = newState;
        for(int i=0;i<current.getHeight();i++){
            for(int j=0;j<current.getWidth();j++){                
                    drawBackground(i,j);               
            }    
        }
        
        drawPlayerPosition(nrRows-1-current.getPlayerRow(0),current.getPlayerCol(0),new Color(150,0,0));
        drawPlayerPosition(nrRows-1-current.getPlayerRow(1),current.getPlayerCol(1),new Color(0,150,0));
        Set<Wall> walls = current.getWallStructure().getWalls();       
        for(Wall wall:walls){
            drawWall(wall);
        }
        screenGraphics.drawImage(bufferImage, 0, 0, null);
        frame.repaint();

    }
    
    public void showWallCandidate(Wall wall){        
        bufferGraphics.setColor(new Color(200,200,200)); 
        int col1 = wall.getStartCol();
        int col2 = wall.getStartCol() + 2* (wall.getEndCol() - wall.getStartCol());
        int row1 = nrRows-wall.getStartRow() - 2*(wall.getEndRow() - wall.getStartRow());
        int row2 = nrRows-wall.getStartRow();
        int colOffset = (col1==col2)?6:-6;
        int rowOffset = (row1==row2)?6:-6;           
        bufferGraphics.fillRect(col1 * cellSize-colOffset, row1 * cellSize-rowOffset,
                                (col2 - col1) * cellSize + 2*colOffset,
                                (row2 - row1) * cellSize + 2*rowOffset);
        
        bufferGraphics.setColor(new Color(100,100,100));        
        float dash1 [] = {2.0f};
        bufferGraphics.setStroke(new BasicStroke(3,BasicStroke.CAP_BUTT,BasicStroke.JOIN_MITER,10.0f, dash1, 0.0f));
        bufferGraphics.drawRect(col1 * cellSize-colOffset, row1 * cellSize-rowOffset,
                                (col2 - col1) * cellSize + 2*colOffset,
                                (row2 - row1) * cellSize + 2*rowOffset);
        bufferGraphics.setStroke(new BasicStroke(1));
        screenGraphics.drawImage(bufferImage, 0, 0, null);
        frame.repaint();
    }
    
    private void drawWall(Wall wall){
        bufferGraphics.setColor(new Color(200,200,100)); 
        int col1 = wall.getStartCol();
        int col2 = wall.getStartCol() + 2* (wall.getEndCol() - wall.getStartCol());
        int row1 = nrRows-wall.getStartRow() - 2*(wall.getEndRow() - wall.getStartRow());
        int row2 = nrRows-wall.getStartRow();
        int colOffset = (col1==col2)?6:-6;
        int rowOffset = (row1==row2)?6:-6;        
        bufferGraphics.fillRect(col1 * cellSize-colOffset, row1 * cellSize-rowOffset,
                                (col2 - col1) * cellSize + 2*colOffset,
                                (row2 - row1) * cellSize + 2*rowOffset);
        
        bufferGraphics.setColor(new Color(100,100,50));
        bufferGraphics.setStroke(new BasicStroke(3));        
        bufferGraphics.drawRect(col1 * cellSize-colOffset, row1 * cellSize-rowOffset,
                                (col2 - col1) * cellSize + 2*colOffset,
                                (row2 - row1) * cellSize + 2*rowOffset);
        bufferGraphics.setStroke(new BasicStroke(1));
    }
    
    private void drawBackground(int row, int col){
        drawEmpty(row,col); 
        bufferGraphics.setColor(new Color(200,200,255));
        bufferGraphics.fillRect(col * cellSize + 6, row * cellSize + 6, cellSize-12, cellSize-12);
        bufferGraphics.setColor(new Color(200,100,255));
        bufferGraphics.setStroke(new BasicStroke(3));
        bufferGraphics.drawRect(col * cellSize + 6, row * cellSize + 6, cellSize-12, cellSize-12);       
        bufferGraphics.setStroke(new BasicStroke(1));
    }       
    
     private void drawPlayerPosition(int row, int col, Color color){        
        bufferGraphics.setColor(color);
        bufferGraphics.fillOval(col * cellSize +8, row * cellSize +8, cellSize -16 , cellSize -16);        
    }
     
    private void drawEmpty(int row, int col){
        bufferGraphics.setColor(new Color(30,30,55));
        bufferGraphics.fillRect(col * cellSize , row * cellSize, cellSize, cellSize);        
    }
    
    public void addKeyListener(KeyListener list){
        frame.addKeyListener(list);
    }
    
    public void removeKeyListener(KeyListener list){
        frame.removeKeyListener(list);
    }
}
