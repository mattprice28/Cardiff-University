package moves;

import quoridor.GameState2P;

/**
 *
 * @author steven
 */
public class PlayerLeftMove implements Move {

        int index;

        public PlayerLeftMove(int index) {
            this.index = index;
        }

        public GameState2P doMove(GameState2P s) {
            return s.moveLeft(index);
        }

        public String toString() {
            return "LEFT";
        }
    }
