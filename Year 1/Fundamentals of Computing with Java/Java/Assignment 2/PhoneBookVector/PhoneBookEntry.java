class PhoneBookEntry {

    private String name;
    private String number;

    public PhoneBookEntry( String inName, String inNumber ) {
        name = inName;
        number = inNumber;
    }

    public String getName( ) {
        return name;
    }

    public String getNumber( ) {
        return number;
    }

    public void setNumber( String inNumber ) {
        number = inNumber;
    }

    public String toString( ) {
        return name + "\t(" + number + ") ";
    }

}