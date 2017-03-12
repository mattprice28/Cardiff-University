public class TestShape {
   public static void main( String[] args ) {
      Shape[] a = { new Shape(), new Circle(5), new Square(10),
	                new Circle(2) };

      for (int i = 0; i < a.length; ++i) {
         System.out.println( "Area is " + a[i].getArea() );
      }
   }
}