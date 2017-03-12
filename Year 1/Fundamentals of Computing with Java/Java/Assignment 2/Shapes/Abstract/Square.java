public class Square extends Shape {
   private int length;

   public Square( int inLength ) {
      length = inLength;
   }

   public float getArea() {
      // Output for illustration only
      System.out.print( "(In Square.getArea()):" );
      return length * length;
   }
}