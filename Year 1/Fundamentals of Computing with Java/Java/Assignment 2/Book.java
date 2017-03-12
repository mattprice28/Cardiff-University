/*
 * Name: Matthew Price
 * Student number: 0924337
 */

/*
 * A class to represent a number of copies of a library book.
 */
public class Book {
    private String author;
    private String title;
    private int totalNumCopies;
    private int availableCopies;

	/*
	 * Constructor method for creating a book with a given author,
	 * title, and number of copies.
	 * This constructor checks that the total number of copies argument is 
	 * valid; i.e., the number of copies should be 1 or more. 
	 * If not valid, the constructor will throw an IllegalArgumentException with
	 * an appropriate error message.
	 */
	public Book( String inAuthor, String inTitle, int inTotalNumCopies ) {
		if (totalNumCopies < 1) {
throw new IllegalStateException("Must enter at least 1 copy.");
}

		author = inAuthor;
		title = inTitle;
		totalNumCopies = inTotalNumCopies;
	}

	/*
	 * An accessor method that returns the book's author.
	 */
	public String getAuthor() {
		return author;
	}

	/*
	 * An accessor method that returns the book's title.
	 */
	public String getTitle() {
		return title;
	}

	/*
	 * An accessor method that returns the total number of copies of this book.
	 * This should count both withdrawn and returned books.
	 */ 
	public int getTotalCopies() {
		return totalNumCopies;
	}

	/*
	 * Returns the number of copies of the book that are available
	 * (i.e., not on loan).
	 */
	public int getAvailableCopies() {
		return availableCopies;
	}

	/*
	 * Mark one of the copies of this book as on loan.
	 * If there are no available copies to withdraw then this method should 
	 * throw an IllegalStateException with an appropriate error message.
	 */
	public void withdrawCopy() {
		if (availableCopies < 1) {
throw new IllegalStateException("There are no copies available.");
}
		availableCopies --;
	}

	/*
	 * Mark one of the copies of this book as returned.
	 * If all of the copies of this book are already returned, this ethod
	 * should throw an IllegalStateException with an appropriate error message.
	 */
	public void returnCopy() {
				if (availableCopies == totalNumCopies) {
throw new IllegalStateException("All copies have been returned.");
}
		availableCopies ++;
	}
}


