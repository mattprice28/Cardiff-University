package moves;

import quoridor.GameState2P;

/**
 *
 * @author steven
 */
public interface Move {
        public GameState2P doMove(GameState2P s);
    }
