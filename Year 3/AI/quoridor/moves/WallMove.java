package moves;

import quoridor.GameState2P;
import quoridor.Wall;

/**
 *
 * @author steven
 */
public class WallMove implements Move {
        Wall w;
        int index;

        public WallMove(int index, Wall w) {
            this.index = index;
            this.w = w;
        }

        public GameState2P doMove(GameState2P s) {
            return s.placeWall(index, w);
        }

        public String toString() {
            return "WALL (" + w.getStartRow() + "," + w.getStartCol() + "," + w.isHorizontal() + ")";
        }
    }
