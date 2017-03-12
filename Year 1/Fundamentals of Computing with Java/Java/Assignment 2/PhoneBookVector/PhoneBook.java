import java.util.Vector;

public class PhoneBook {

    private Vector<PhoneBookEntry> entries;

    public PhoneBook( ) {
        entries = new Vector<PhoneBookEntry>();
    }

    public void add( String name, String number ) {
		entries.add(new PhoneBookEntry(name, number));
    }

    public String toString( ) {
        StringBuffer temp = new StringBuffer();
        for (int i = 0; i < entries.size(); ++i) {
            temp.append( entries.get(i).toString() + "\n" );
        }
        return temp.toString();
    }

}