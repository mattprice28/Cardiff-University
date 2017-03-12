package players;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import quoridor.GameDisplay;
import quoridor.GameState2P;
import quoridor.Quoridor;
import quoridor.Wall;

/**
 *
 * @author steven
 */
public class HumanPlayer extends QuoridorPlayer implements KeyListener {

    boolean placeWall = false;
    int initialWallRow = 2; 
    int initialWallCol = 2; 
    boolean isCurrentWallHorizontal = true;

    public HumanPlayer(GameState2P state, int index, Quoridor game) {
        super(state, index, game);
    }

    public void setDisplay(GameDisplay display) {
        super.setDisplay(display);
    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyChar() == 'w') {
            placeWall = !placeWall;
            if (placeWall) {
                display.showWallCandidate(new Wall(initialWallRow, initialWallCol, isCurrentWallHorizontal));
            }
            else {
                display.updateState(state);
            }
        }
        else if (!placeWall) {
            GameState2P newState = null;
            if (e.getKeyCode() == KeyEvent.VK_UP) {
                newState = state.moveUp(index);
            }
            else if (e.getKeyCode() == KeyEvent.VK_DOWN) {
                newState = state.moveDown(index);
            }
            else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
                newState = state.moveRight(index);
            }
            else if (e.getKeyCode() == KeyEvent.VK_LEFT) {
                newState = state.moveLeft(index);
            }
            if (newState != null) {
                display.removeKeyListener(this);
                game.doMove(index, newState);
            }
        }
        else {
            if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                GameState2P newState = state.placeWall(index, new Wall(initialWallRow, initialWallCol, isCurrentWallHorizontal));
                if (newState != null) {
                    display.removeKeyListener(this);
                    game.doMove(index, newState);
                }
            }
            else {
                if (e.getKeyCode() == KeyEvent.VK_UP) {
                    if ((!isCurrentWallHorizontal && initialWallRow < state.getHeight() - 2)
                            || (isCurrentWallHorizontal && initialWallRow < state.getHeight() - 1)) {
                        initialWallRow++;
                    }
                }
                else if (e.getKeyCode() == KeyEvent.VK_DOWN) {
                    if ((!isCurrentWallHorizontal && initialWallRow > 0)
                            || (isCurrentWallHorizontal && initialWallRow > 1)) {
                        initialWallRow--;
                    }
                }
                else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
                    if ((!isCurrentWallHorizontal && initialWallCol < state.getWidth() - 1)
                            || (isCurrentWallHorizontal && initialWallCol < state.getWidth() - 2)) {
                        initialWallCol++;
                    }
                }
                else if (e.getKeyCode() == KeyEvent.VK_LEFT) {
                    if ((!isCurrentWallHorizontal && initialWallCol > 1)
                            || (isCurrentWallHorizontal && initialWallCol > 0)) {
                        initialWallCol--;
                    }
                }
                else if (e.getKeyChar() == 'r') {
                    isCurrentWallHorizontal = !isCurrentWallHorizontal;
                    if (isCurrentWallHorizontal) {
                        initialWallRow++;
                        initialWallCol--;
                        if (initialWallCol == state.getWidth() - 1) {
                            initialWallCol--;
                        }
                        if (initialWallRow == 0) {
                            initialWallRow++;
                        }
                    }
                    else {
                        initialWallRow--;
                        initialWallCol++;
                        if (initialWallRow == state.getHeight() - 1) {
                            initialWallRow--;
                        }
                        if (initialWallCol == 0) {
                            initialWallCol++;
                        }
                    }
                }

                display.updateState(state);
                display.showWallCandidate(new Wall(initialWallRow, initialWallCol, isCurrentWallHorizontal));
            }
        }
    }

    public void keyReleased(KeyEvent e) {
    }

    public void doMove() {
        placeWall = false;
        initialWallRow = 2;
        initialWallCol = 2;
        isCurrentWallHorizontal = true;
        display.addKeyListener(this);
    }
}
