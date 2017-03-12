public class Circle extends Shape {
   private int radius;

   public Circle( int inRadius ) {
      radius = inRadius;
   }

   public float getArea( ) {
      // Output for illustration only
      System.out.print( "(In Circle.getArea()):" );
      return (float) Math.PI * radius * radius;
   }
}