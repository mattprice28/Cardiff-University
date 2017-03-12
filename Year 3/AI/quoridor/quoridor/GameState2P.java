package quoridor;

import java.util.ArrayList;
import java.util.List;
import moves.*;
/**
 *
 * @author steven
 */
public class GameState2P {

    //dimensions of the board
    private int width = 5;    
    private int height = 5;
    
    //number of walls each player can place
    private int wallsPerPlayer = 5;
    
    //the collection of walls that are currently on the board
    private WallStructure assignedWalls;
    
    //the current states of each player
    private int[] row;
    private int[] col;        
    private int[] nrWallsLeft;
    
    /*
     * The shortest path from each cell to the top and bottom rows
     * is used for the heuristic evaluation by the computer player
     * and to find out which wall positions are legal
     */ 
    private int[][] distanceToTop;
    private int[][] distanceToBottom;
    
    /*
     * The following arrays encode which moves are legal across the board    
     */
    boolean[][] leftLegal;
    boolean[][] rightLegal;
    boolean[][] upLegal;
    boolean[][] downLegal;
    
    /* 
     * The arrays distanceToTop, distanceTobottom, leftLegal, rightLegal, upLegal
     * and downLegal need to be recomputed every time a wall is added. This is 
     * computationally expensive. Moreover, in a naive implementation the same
     * wall structures would be encountered over and over again. Therefore, we
     * remember previously considered game states in a cache. 
     */
    private static GameState2P[] cache;
    static {
        cache = new GameState2P[65536];
    }

    public GameState2P() {
        init();
    }

    public GameState2P(int width,int height, int wallsPerPlayer) {
        this.width=width;
        this.height=height;
        this.wallsPerPlayer=wallsPerPlayer;
        init();
    }
    
    // copy constructor
    public GameState2P(GameState2P state) {
        width=state.width;
        height=state.height;
        wallsPerPlayer=state.wallsPerPlayer;
        assignedWalls = new WallStructure();
        row = new int[2];
        col = new int[2];
        nrWallsLeft = new int[2];
        for (int i = 0; i < row.length; i++) {
            row[i] = state.row[i];
            col[i] = state.col[i];
            nrWallsLeft[i] = state.nrWallsLeft[i];
        }
        for (Wall w : state.assignedWalls.getWalls()) {
            assignedWalls.addWall(w);
        }
        distanceToTop = state.distanceToTop;
        distanceToBottom = state.distanceToBottom;
        leftLegal = state.leftLegal;
        rightLegal = state.rightLegal;
        upLegal = state.upLegal;
        downLegal = state.downLegal;
    }

    private void init(){
        assignedWalls = new WallStructure();
        row = new int[2];
        col = new int[2];
        nrWallsLeft = new int[2];
        row[0] = 0;
        col[0] = (width - 1) / 2;
        row[1] = height - 1;
        col[1] = (width - 1) / 2;
        nrWallsLeft[0] = wallsPerPlayer;
        nrWallsLeft[1] = wallsPerPlayer;
        initDistances();
    }
    
    public int getPlayerRow(int index) {
        return row[index];
    }

    public int getPlayerCol(int index) {
        return col[index];
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }
    
    public boolean isGameOver() {
        return row[0] == height - 1 || row[1] == 0;
    }

    /*
     * When a new wall is added, the values for the arrays distanceToBottom,
     * distanceToTop, leftLegal, rightLegal, upLegal and downLegal need to
     * be recomputed
     */
    public void addWall(Wall w) {
        assignedWalls.addWall(w);
        leftLegal = null;
        rightLegal = null;
        upLegal = null;
        downLegal = null;
        distanceToBottom = null;
        distanceToTop = null;
        initDistances();
    }

    public WallStructure getWallStructure() {
        return assignedWalls;
    }

    private boolean moveUpLegal(int r, int c) {
        if (r == height - 1) {
            //we are at the top row of the board
            return false;
        }
        for (Wall wall : assignedWalls.getWalls()) {
            if (wall.isHorizontal() && wall.getStartRow() == r + 1
                    && (wall.getStartCol() == c || wall.getEndCol() == c)) {
                // move prevented by wall
                return false;
            }
        }
        return true;
    }   

    private boolean moveDownLegal(int r, int c) {
        if (r == 0) {
            //we are at the bottom row of the board
            return false;
        }
        for (Wall wall : assignedWalls.getWalls()) {
            if (wall.isHorizontal() && wall.getStartRow() == r
                    && (wall.getStartCol() == c || wall.getEndCol() == c)) {
                // move prevented by wall
                return false;
            }
        }
        return true;
    }
    
    private boolean moveRightLegal(int r, int c) {
        if (c == width - 1) {
            //we are at the rightmost column of the board
            return false;
        }
        for (Wall wall : assignedWalls.getWalls()) {
            if (!wall.isHorizontal() && wall.getStartCol() == c + 1
                    && (wall.getStartRow() == r || wall.getEndRow() == r)) {
                // move prevented by wall
                return false;
            }
        }
        return true;
    }

    private boolean moveLeftLegal(int r, int c) {
        if (c == 0) {
            //we are at the leftmost column of the board
            return false;
        }
        for (Wall wall : assignedWalls.getWalls()) {
            if (!wall.isHorizontal() && wall.getStartCol() == c
                    && (wall.getStartRow() == r || wall.getEndRow() == r)) {
                // move prevented by wall
                return false;
            }
        }
        return true;
    }
    
    public GameState2P moveUp(int playerIndex) {
        if (upLegal[row[playerIndex]][col[playerIndex]]) {
            GameState2P newState = new GameState2P(this);
            newState.row[playerIndex] = row[playerIndex] + 1;
            return newState;
        }
        else {
            return null;
        }
    }
    
    public GameState2P moveDown(int playerIndex) {
        if (downLegal[row[playerIndex]][col[playerIndex]]) {
            GameState2P newState = new GameState2P(this);
            newState.row[playerIndex] = row[playerIndex] - 1;
            return newState;
        }
        else {
            return null;
        }
    }

    
    public GameState2P moveRight(int playerIndex) {
        if (rightLegal[row[playerIndex]][col[playerIndex]]) {
            GameState2P newState = new GameState2P(this);
            newState.col[playerIndex] = col[playerIndex] + 1;
            return newState;
        }
        else {
            return null;
        }
    }  

    public GameState2P moveLeft(int playerIndex) {
        if (leftLegal[row[playerIndex]][col[playerIndex]]) {
            GameState2P newState = new GameState2P(this);
            newState.col[playerIndex] = col[playerIndex] - 1;
            return newState;
        }
        else {
            return null;
        }
    }

    public GameState2P placeWall(int playerIndex, Wall wall) {
        //Check whether player has any walls left
        if (nrWallsLeft[playerIndex] == 0) {
            return null;
        }

        //Check whether wall intersects with an existing wall
        if (assignedWalls.intersects(wall)) {
            return null;
        }

        //Try adding wall
        GameState2P newState = new GameState2P(this);
        newState.nrWallsLeft[playerIndex]--;
        newState.addWall(wall);

        //Check whether the new wall cuts off one of the players from their goal                
        if (newState.distanceToTop[row[0]][col[0]] < 0 || newState.distanceToBottom[row[1]][col[1]] < 0) {
            return null;
        }
        return newState;
    }

    private void initDistances() {
        int h = assignedWalls.hashCode() % cache.length;
        if (cache[h] != null && cache[h].assignedWalls.equals(assignedWalls)) {              
            leftLegal = cache[h].leftLegal;
            rightLegal = cache[h].rightLegal;
            upLegal = cache[h].upLegal;
            downLegal = cache[h].downLegal;
            distanceToTop = cache[h].distanceToTop;
            distanceToBottom = cache[h].distanceToBottom;
        }
        else {            
            leftLegal = new boolean[height][width];
            rightLegal = new boolean[height][width];
            upLegal = new boolean[height][width];
            downLegal = new boolean[height][width];
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    leftLegal[i][j] = moveLeftLegal(i, j);
                    rightLegal[i][j] = moveRightLegal(i, j);
                    upLegal[i][j] = moveUpLegal(i, j);
                    downLegal[i][j] = moveDownLegal(i, j);
                }
            }

            List<FrontierNode> frontierTop = new ArrayList();
            List<FrontierNode> frontierBot = new ArrayList();

            distanceToTop = new int[height][width];
            distanceToBottom = new int[height][width];

            for (int j = 0; j < width; j++) {
                frontierTop.add(new FrontierNode(height - 1, j, 0));
                frontierBot.add(new FrontierNode(0, j, 0));
            }
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    distanceToTop[i][j] = -1;
                    distanceToBottom[i][j] = -1;
                }
            }

            // use breadth-first search to compute the values of distanceToTop
            while (!frontierTop.isEmpty()) {
                FrontierNode n = frontierTop.get(0);
                frontierTop.remove(0);
                if (distanceToTop[n.row][n.col] == -1 || distanceToTop[n.row][n.col] > n.dist) {
                    distanceToTop[n.row][n.col] = n.dist;
                    if (n.row > 0 && (distanceToTop[n.row - 1][n.col] == -1 || distanceToTop[n.row - 1][n.col] > n.dist + 1) && downLegal[n.row][n.col]) {
                        frontierTop.add(new FrontierNode(n.row - 1, n.col, n.dist + 1));
                    }
                    if (n.row < height - 1 && (distanceToTop[n.row + 1][n.col] == -1 || distanceToTop[n.row + 1][n.col] > n.dist + 1) && upLegal[n.row][n.col]) {
                        frontierTop.add(new FrontierNode(n.row + 1, n.col, n.dist + 1));
                    }
                    if (n.col > 0 && (distanceToTop[n.row][n.col - 1] == -1 || distanceToTop[n.row][n.col - 1] > n.dist + 1) && leftLegal[n.row][n.col]) {
                        frontierTop.add(new FrontierNode(n.row, n.col - 1, n.dist + 1));
                    }
                    if (n.col < width - 1 && (distanceToTop[n.row][n.col + 1] == -1 || distanceToTop[n.row][n.col + 1] > n.dist + 1) && rightLegal[n.row][n.col]) {
                        frontierTop.add(new FrontierNode(n.row, n.col + 1, n.dist + 1));
                    }
                }
            }

            // use breadth-first search to compute the values of distanceToBottom
            while (!frontierBot.isEmpty()) {
                FrontierNode n = frontierBot.get(0);
                frontierBot.remove(0);
                if (distanceToBottom[n.row][n.col] == -1 || distanceToBottom[n.row][n.col] > n.dist) {
                    distanceToBottom[n.row][n.col] = n.dist;
                    if (n.row > 0 && (distanceToBottom[n.row - 1][n.col] == -1 || distanceToBottom[n.row - 1][n.col] > n.dist + 1) && downLegal[n.row][n.col]) {
                        frontierBot.add(new FrontierNode(n.row - 1, n.col, n.dist + 1));
                    }
                    if (n.row < height - 1 && (distanceToBottom[n.row + 1][n.col] == -1 || distanceToBottom[n.row + 1][n.col] > n.dist + 1) && upLegal[n.row][n.col]) {
                        frontierBot.add(new FrontierNode(n.row + 1, n.col, n.dist + 1));
                    }
                    if (n.col > 0 && (distanceToBottom[n.row][n.col - 1] == -1 || distanceToBottom[n.row][n.col - 1] > n.dist + 1) && leftLegal[n.row][n.col]) {
                        frontierBot.add(new FrontierNode(n.row, n.col - 1, n.dist + 1));
                    }
                    if (n.col < width - 1 && (distanceToBottom[n.row][n.col + 1] == -1 || distanceToBottom[n.row][n.col + 1] > n.dist + 1) && rightLegal[n.row][n.col]) {
                        frontierBot.add(new FrontierNode(n.row, n.col + 1, n.dist + 1));
                    }
                }
            }
            cache[h]=this;
        }
    }


    public static List<Move> getLegalMoves(GameState2P state, int index) {
        List<Move> res = new ArrayList();
        int r = state.row[index];
        int c = state.col[index];
        
        //Check in which directions the player can move
        if (state.moveDownLegal(r, c)) {
            res.add(new PlayerDownMove(index));
        }
        if (state.moveUpLegal(r, c)) {
            res.add(new PlayerUpMove(index));
        }
        if (state.moveLeftLegal(r, c)) {
            res.add(new PlayerLeftMove(index));
        }
        if (state.moveRightLegal(r, c)) {
            res.add(new PlayerRightMove(index));
        }
        
        //Check at which positions a wall can be added
        for (int i = 1; i < state.height - 1; i++) {
            for (int j = 0; j < state.width-1; j++) {
                Wall w = new Wall(i, j, true);
                GameState2P newState = state.placeWall(index, w);
                if (newState != null) {
                    res.add(new WallMove(index, w));
                }
            }
        }
        for (int i = 0; i < state.height-1; i++) {
            for (int j = 1; j < state.width - 1; j++) {
                Wall w = new Wall(i, j, false);
                GameState2P newState = state.placeWall(index, w);
                if (newState != null) {
                    res.add(new WallMove(index, w));
                }
            }
        }
        return res;
    }

   public boolean isWinner(int index) {        
        if (index == 0) {
            if (row[0] == height - 1) //we have won
            {
                return true;
            }
            if (row[1] == 0) //we have lost
            {
                return false;
            }            
        }
        else {
            if (row[0] == height - 1) //we have lost
            {
                return false;
            }
            if (row[1] == 0) //we have won
            {
                return true;
            }            
        }      
        return false; // we are not in a final state
    }
    
    /*
     * Heuristic evaluation of the state, used by the minimax algorithm
     */
    public double evaluateState(int index) {
        int distToGoal;
        int opponentDistToGoal;
        int nrWalls;
        int opponentNrWalls;
        boolean winning=false;
        boolean losing=false;
        if (index == 0) {
            if (row[0] == height - 1) //we have won
            {
                winning=true;
            }
            if (row[1] == 0) //we have lost
            {
                losing=true;
            }
            if (distanceToTop == null) {
                initDistances();
            }
            distToGoal = distanceToTop[row[0]][col[0]];
            opponentDistToGoal = distanceToBottom[row[1]][col[1]];
            nrWalls = nrWallsLeft[0];
            opponentNrWalls = nrWallsLeft[1];
        }
        else {
            if (row[0] == height - 1) //we have lost
            {
                losing=true;
            }
            if (row[1] == 0) //we have won
            {
                winning=true;
            }
            if (distanceToTop == null) {
                initDistances();
            }
            opponentDistToGoal = distanceToTop[row[0]][col[0]];
            distToGoal = distanceToBottom[row[1]][col[1]];
            opponentNrWalls = nrWallsLeft[0];
            nrWalls = nrWallsLeft[1];
        }
        int res =(opponentDistToGoal - distToGoal);
        if(winning)
            res+=1000;
        if(losing)
            res-=1000;
        return res;
    }

    public boolean equals (Object o){
        if(!(o instanceof GameState2P))
            return false;
        GameState2P gs = (GameState2P) o;
        if(!assignedWalls.equals(gs.assignedWalls))
            return false;
        for(int i=0;i<row.length;i++){
            if(row[i]!=gs.row[i] || col[i]!=gs.col[i] || nrWallsLeft[i]!=gs.nrWallsLeft[i])
                return false;
        }
        return true;
    }
    
    public int hashCode(){
        int res = assignedWalls.hashCode();
        for(int i=0;i<row.length;i++){
            res += (i+1)*16*row[i];
            res += (i+1)*1024*col[i];
            res += (i+1)*32768*nrWallsLeft[i];
        }
        return res;
    }
    
    
    /*
     * Inner class which is used to implement breadth-first search
     * in the method initDistances
     */
    public static class FrontierNode {

        int row;
        int col;
        int dist;

        public FrontierNode(int row, int col, int dist) {
            this.row = row;
            this.col = col;
            this.dist = dist;
        }
    }
}
