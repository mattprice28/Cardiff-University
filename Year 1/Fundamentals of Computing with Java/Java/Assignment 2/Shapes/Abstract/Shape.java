// Declaring the class abstract means that no objects of this class can be 
// created - only objects of it's subclasses. E.g. 
// Shape s = new Shape(); will not compile
// Shape s = new Circle(6); will.
abstract public class Shape {
   // Declaring this method abstract means that every class we define that
   // *extends* Shape *must* provide an implementation for this method.
   abstract float getArea( );
}