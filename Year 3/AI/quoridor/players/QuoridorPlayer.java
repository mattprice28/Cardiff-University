package players;

import quoridor.GameDisplay;
import quoridor.GameState2P;
import quoridor.Quoridor;

/**
 *
 * @author steven
 */
public abstract class QuoridorPlayer {
    
    protected GameState2P state;
    protected GameDisplay display;    
    protected Quoridor game;
    int index;
        
    public QuoridorPlayer(GameState2P state, int index, Quoridor game){
        this.state=state;                             
        this.index = index;
        this.game=game;
    }     
 
    public void setState(GameState2P state){
        this.state=state;
    }
    
    public int getIndex(){
        return index;
    }
    
   public void setDisplay(GameDisplay display) {
        this.display = display;        
    }
    
    public abstract void doMove();
    
}
