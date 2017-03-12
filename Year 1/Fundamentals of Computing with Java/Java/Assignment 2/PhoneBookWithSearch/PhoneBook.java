public class PhoneBook {

    private PhoneBookEntry[] list;
    private int size;
    private int maxListLength = 1;

    public PhoneBook( ) {
        list = new PhoneBookEntry[maxListLength];
    }

    public void add( String name, String number ) {
		if ( size == list.length ) {
			maxListLength = 2 * maxListLength;
			PhoneBookEntry[] temp = new PhoneBookEntry[ maxListLength ];
			System.arraycopy( list, 0, temp, 0, list.length );
			list = temp;
		}
        list[size] = new PhoneBookEntry( name, number );
        size++;
    }

    public String numberFor( String name ) {
        for (int i = 0; i < size; ++i) {
            if ( list[i].getName().equals(name) ) {
                return list[i].getNumber();
            }
        }
        return "NOT FOUND";
    }

    public String toString( ) {
        StringBuffer temp = new StringBuffer();
        for (int i = 0; i < size; ++i) {
            temp.append( list[i].toString() + "\n" );
        }
        return temp.toString();
    }

}