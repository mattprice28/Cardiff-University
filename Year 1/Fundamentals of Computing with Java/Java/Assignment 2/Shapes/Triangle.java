public class Triangle extends Shape {
    int height;
    int width;
    
    public Triangle( int inHeight, int inWidth ) {
        height = inHeight;
        width = inWidth;
    }
    
    public float getArea() {
        System.out.print( "(In Triangle.getArea()):" );
        return .5f * height * width;
    }

}