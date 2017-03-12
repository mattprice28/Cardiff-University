public class PhoneBookTest {

    public static void main( String[] args ) {

        // Create and fill phone book
        PhoneBook pb = new PhoneBook();
        pb.add( "Bob", "+44 (0) 483984" );
        pb.add( "Carl", "38478" );
        pb.add( "Don", "3878" );
        pb.add( "Ed", "3848" );
        pb.add( "Frank", "8478" );
        System.out.println();

        // Output whole book
        System.out.println( pb );
        System.out.println();

        // Find entries
        System.out.println( "Carl's number is " + pb.numberFor( "Carl" ) );
        System.out.println( "Debbie's number is " + pb.numberFor( "Debbie" ) );
    }

}
