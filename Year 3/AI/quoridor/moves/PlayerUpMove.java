package moves;

import quoridor.GameState2P;

/**
 *
 * @author steven
 */
 public class PlayerUpMove implements Move {

        int index;

        public PlayerUpMove(int index) {
            this.index = index;
        }

        public GameState2P doMove(GameState2P s) {
            return s.moveUp(index);
        }

        public String toString() {
            return "UP";
        }
    }