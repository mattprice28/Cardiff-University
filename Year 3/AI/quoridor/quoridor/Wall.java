package quoridor;

/**
 *
 * @author steven
 */
public class Wall {

    private int startRow;
    private int startCol;
    private boolean horizontal;

    public Wall(int startRow, int startCol, boolean horizontal) {
        this.startRow = startRow;
        this.startCol = startCol;
        this.horizontal = horizontal;
    }

    public boolean isHorizontal() {
        return horizontal;
    }

    public int getStartRow() {
        return startRow;
    }

    public int getStartCol() {
        return startCol;
    }

    public int getEndRow() {
        return horizontal ? startRow : startRow + 1;
    }

    public int getEndCol() {
        return horizontal ? startCol + 1 : startCol;
    }

    public boolean intersects(Wall w) {
        if (horizontal && w.horizontal) {
            return startRow == w.startRow && (startCol >= w.startCol - 1 && startCol <= w.startCol + 1);
        }
        else if (!horizontal && !w.horizontal) {
            return startCol == w.startCol && (startRow >= w.startRow - 1 && startRow <= w.startRow + 1);
        }
        else if (horizontal && !w.horizontal) {
            return startCol == w.startCol - 1 && startRow == w.startRow + 1;
        }
        else {
            return w.startCol == startCol - 1 && w.startRow == startRow + 1;
        }

    }

    public String toString(){
        if(horizontal)
            return "(H," + startRow+","+startCol+")";
        else
            return "(V," + startRow+","+startCol+")";
    }
    
    public int hashCode() {
        if (horizontal) {
            return startRow + startCol * 16;
        }
        else {
            return startRow + startCol * 16 + 1024;
        }
    }

    public boolean equals(Object o) {
        if (!(o instanceof Wall)) {
            return false;
        }
        Wall w = (Wall) o;
        if (startCol != w.startCol || startRow != w.startRow) {
            return false;
        }
        else if ((horizontal && !w.horizontal) || (w.horizontal && !horizontal)) {
            return false;
        }
        else {
            return true;
        }
    }
}
