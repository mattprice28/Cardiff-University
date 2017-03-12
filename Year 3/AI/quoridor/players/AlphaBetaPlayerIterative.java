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
public class AlphaBetaPlayerIterative extends QuoridorPlayer {

    public static Random random = new Random();
    private int indexOpponent;    
    private int startDepth=1;
    private long availableTime=5000;
    
    public AlphaBetaPlayerIterative(GameState2P state, int index, Quoridor game) {
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
        
        Move lastBest = null;
        for (; System.currentTimeMillis() < timeup; depth++) {
            Move bestMove = null;
            double bestScore = 0;
            for (Move m : legalMoves) {
                GameState2P next = m.doMove(state);
                double score = getMinScoreAlphaBeta(next, depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY, timeup);

                if (System.currentTimeMillis() > timeup) {
//                    System.out.println("last depth = " + depth);
                    break;
                }
                if (bestMove == null || score > bestScore) {
                    bestMove = m;
                    bestScore = score;
                }
            }
            if (System.currentTimeMillis() < timeup) {
                lastBest = bestMove;
            }         
        }
        GameState2P newState = lastBest.doMove(state);
        game.doMove(index, newState);
    }

    /*
     * Consider all possible moves by our opponent
     */
    private double getMinScoreAlphaBeta(GameState2P s, int depth, double alpha, double beta, long timeup) {
        double res;
        if (depth == 0 || s.isGameOver()) {
            res = s.evaluateState(index);
        }
        else {
            List<Move> opponentMoves = GameState2P.getLegalMoves(s, indexOpponent);
            res = Double.POSITIVE_INFINITY;
            for (Move move : opponentMoves) {
                if (System.currentTimeMillis() > timeup) {
                    return -1;
                }
                GameState2P next = move.doMove(s);
                double score = getMaxScoreAlphaBeta(next, depth - 1, alpha, beta, timeup);
                res = Math.min(res, score);
                beta = Math.min(beta, score);
                if (beta <= alpha) {
                    break;
                }
            }
        }
        return res;
    }

    /*
     * Consider all possible moves we can play
     */
    private double getMaxScoreAlphaBeta(GameState2P s, int depth, double alpha, double beta, long timeup) {
        double res;
        if (depth == 0 || s.isGameOver()) {
            res = s.evaluateState(index);
        }
        else {
            List<Move> myMoves = GameState2P.getLegalMoves(s, index);
            res = Double.NEGATIVE_INFINITY;
            for (Move move : myMoves) {
                if (System.currentTimeMillis() > timeup) {
                    return -1;
                }
                GameState2P next = move.doMove(s);
                double score = getMinScoreAlphaBeta(next, depth - 1, alpha, beta, timeup);
                res = Math.max(res, score);
                alpha = Math.max(alpha, score);
                if (beta <= alpha) {
                    break;
                }
            }
        }
        return res;
    }
}
