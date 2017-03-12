/*
 * Name: Matthew Price
 * Student number: 0924337
/*
 * A class to represent a library.
 * A library can either have unlimited book capacity or limited book capacity.
 * For limited capacity libraries, books on loan still count towards the 
 * capacity (there must be space reserved for when a book is returned).
 */
public class Library {
    private Book[] list;
    private int capacity;
    private int totalNumBooks = 0;
    
    /*
     * Construct a Library with unlimited capacity.
     */ 
    public Library() {
		list = new Book[];
    }

        public void addBook( Book newBook ){
            totalNumBooks = totalNumBooks + inTotalNumCopies;

        }
        public void hasBookWithTitle( String bookTitle){
            t1 = title;
            t2 = bookTitle;
            if (t1.equalsIgnoreCase(t2)){
                return True;
            }
            else {
                return False;
            }
        }

        public void getBookWithTitle( String bookTitle){
            t1 = title;
            t2 = bookTitle;
            if (t1.equalsIgnoreCase(t2)){
                return Book;
            }
        }

        public void numberAvailableBooks() {
            return totalNumBooks;

        }

    /*
     * Construct a Library with limited capacity.
     */ 
    public Library( int inCapacity ) {
    }
		public void addBook( Book newBook ){
            if ((totalNumBooks + inTotalNumCopies) > capacity) {
        throw new IllegalStateException("Capacity exceeded.");
        }
        capacity = (totalNumBooks + inTotalNumCopies);
    }
    
    
    // Add methods here
    // to be completed
}


