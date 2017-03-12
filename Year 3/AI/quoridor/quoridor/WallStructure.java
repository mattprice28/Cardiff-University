package quoridor;

import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author steven
 */
public class WallStructure {

    Set<Wall> walls;
    int hashCode = 0;

    public WallStructure() {
        walls = new HashSet();
    }

    public void addWall(Wall w) {
        walls.add(w);
        int h = w.hashCode();
        hashCode+= h*h;
    }

    public Set<Wall> getWalls(){
        return walls;
    }
    
    public int hashCode() {
        return hashCode;
    }
       
    public boolean intersects(Wall wall){
        for (Wall w1 : walls) {
            if (wall.intersects(w1)) {
                return true;
            }
        }
        return false;
    }
    
    public String toString(){
        return walls.toString();
    }
    
    public boolean equals(Object o){
        if(!(o instanceof WallStructure))
            return false;
        WallStructure ws = (WallStructure)o;
        if(walls.size() != ws.walls.size())
            return false;
        for(Wall wall:walls){
            if(!ws.walls.contains(wall))
                return false;
        }
        return true;
    }
}
