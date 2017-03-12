package quoridor;

import players.*;

/**
 *
 * @author steven
 */
public class Quoridor {

    GameState2P state;
    QuoridorPlayer[] players;
    GameDisplay display;
    boolean showGUI = true;

    public Quoridor() {
        startGUIGame();
    }
   
    public void startGUIGame() {
        state = new GameState2P();
        showGUI = true;
        display = new GameDisplay(state);
        players = new QuoridorPlayer[2];
        // players[0] = new HumanPlayer(state, 0, this);
        players[0] = new RandomSimulationPlayer(state, 0, this);
        players[1] = new RandomSimulationPlayer(state, 0, this);
        // players[1] = new AlphaBetaPlayerIterative(state, 1, this);

        for (int i = 0; i < 2; i++) {
            players[i].setDisplay(display);
        }
        players[0].doMove();
    }

    public void doMove(int playerIndex, GameState2P newState) {
        state = newState;
        for (int i = 0; i < 2; i++) {
            players[i].setState(newState);
        }
        final int nextIndex = (playerIndex + 1) % 2;
        if (showGUI) {
            display.updateState(newState);
        }
        if (!newState.isGameOver()) {
            /*
             * Run the method chooseMove in a separate thread
             * to avoid the GUI from becoming unresponsive while 
             * the next move by the computer player is being computed
             */
            if (showGUI) {
                new Thread() {
                    public void run() {
                        players[nextIndex].doMove();
                    }
                }.start();
            }
            else {
                players[nextIndex].doMove();
            }
        }
        else if (showGUI) {
            java.awt.Toolkit.getDefaultToolkit().beep();
        }
    }

    public static void main(String[] args) {
        new Quoridor();
    }
}
