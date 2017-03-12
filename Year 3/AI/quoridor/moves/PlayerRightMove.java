package moves;

import quoridor.GameState2P;

/**
 *
 * @author steven
 */
public class PlayerRightMove implements Move {

    int index;

    public PlayerRightMove(int index) {
        this.index = index;
    }

    public GameState2P doMove(GameState2P s) {
        return s.moveRight(index);
    }

    public String toString() {
        return "RIGHT";
    }
}