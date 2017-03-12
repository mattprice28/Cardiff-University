package moves;

import quoridor.GameState2P;

/**
 *
 * @author steven
 */
public class PlayerDownMove implements Move {

    int index;

    public PlayerDownMove(int index) {
        this.index = index;
    }

    public GameState2P doMove(GameState2P s) {
        return s.moveDown(index);
    }

    public String toString() {
        return "DOWN";
    }
}
