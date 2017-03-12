package players;

import java.util.List;
import java.util.Random;
import quoridor.GameState2P;
import quoridor.Quoridor;
import moves.*;

/**
 *
 * @author steven
 */
public class RandomSimulationPlayer extends QuoridorPlayer {

    public static Random random = new Random();
    private int indexOpponent;    
    private int startDepth=1;
    private long availableTime=5000;
    
    public RandomSimulationPlayer(GameState2P state, int index, Quoridor game) {
        super(state, index, game);
        indexOpponent = (index + 1) % 2;
    }

    public void setStartDepth(int startDepth){
        this.startDepth=startDepth;
    }
    
    public void setAvailableTime (long time){
        this.availableTime=availableTime;
    }
    
    public void doMove() {
        List<Move> legalMoves = GameState2P.getLegalMoves(state, index);
        long starttime = System.currentTimeMillis();
        long timeup = starttime + availableTime;
        int depth = startDepth;

        for (; System.currentTimeMillis() < timeup;){
            Move randomMove = legalMoves.get(random.nextInt(legalMoves.size()));
            // System.out.println(randomMove);

            if (System.currentTimeMillis() > timeup) {
                break;
            }

        }

        GameState2P newState = randomMove.doMove(state);
        game.doMove(index, newState);
    }

}
