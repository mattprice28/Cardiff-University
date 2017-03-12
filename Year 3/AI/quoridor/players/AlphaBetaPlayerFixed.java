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
public class AlphaBetaPlayerFixed extends QuoridorPlayer {

    public static Random random = new Random();
    private int indexOpponent;
    private int maxDepth = 2;

    public AlphaBetaPlayerFixed(GameState2P state, int index, Quoridor game) {
        super(state, index, game);
        indexOpponent = (index + 1) % 2;
    }

    public void setMaxDepth(int maxDepth){
        this.maxDepth=maxDepth;
    }
    
    public void doMove() {
        Move m = chooseMove();
        GameState2P newState = m.doMove(state);
        game.doMove(index, newState);
    }
    
    public Move chooseMove() {
        List<Move> legalMoves = GameState2P.getLegalMoves(state, index);
        Move bestMove = null;
        double bestScore = 0;
        for (Move m : legalMoves) {
            GameState2P next = m.doMove(state);
            double score = getMinScoreAlphaBeta(next, maxDepth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
            if (bestMove == null || score > bestScore) {
                bestMove = m;
                bestScore = score;
            }
        }    
        return bestMove;
    }

    /*
     * Consider all possible moves by our opponent
     */
    private double getMinScoreAlphaBeta(GameState2P s, int depth, double alpha, double beta) {
        double res;
        if (depth == 0 || s.isGameOver()) {
            res = s.evaluateState(index);
        }
        else {
            List<Move> opponentMoves = GameState2P.getLegalMoves(s, indexOpponent);
            res = Double.POSITIVE_INFINITY;
            for (Move move : opponentMoves) {
                GameState2P next = move.doMove(s);
                double score = getMaxScoreAlphaBeta(next, depth - 1, alpha, beta);
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
    private double getMaxScoreAlphaBeta(GameState2P s, int depth, double alpha, double beta) {
        double res;
        if (depth == 0 || s.isGameOver()) {
            res = s.evaluateState(index);
        }
        else {
            List<Move> myMoves = GameState2P.getLegalMoves(s, index);
            res = Double.NEGATIVE_INFINITY;
            for (Move move : myMoves) {                
                GameState2P next = move.doMove(s);
                double score = getMinScoreAlphaBeta(next, depth - 1, alpha, beta);
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
