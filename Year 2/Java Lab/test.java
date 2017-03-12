public class test extends Thread {
// Array of 10000 instances of "test" and 10000 instances of "ClassA"; thread[i] will create a[i]
// Both arrays are static, i.e. shared between all instances of test
	public static test[] thread=new test[10000];
	public static ClassA[] a=new ClassA[10000];
// A single, shared factory
	public static Factory theFactory=new Factory();
// When an instance of test is created, its myThreadNumber gets set to the thread number.
// Accordingly, thread[i] will have thread number i.
	public int myThreadNumber;

	public test(int threadNumber) {
		myThreadNumber=threadNumber;
	}

	public void run() {
		a[myThreadNumber]=theFactory.createA();
	}

	public static void main(String[] args) throws Exception {
		int i;

// Create 10000 instances of the class test; start all of them and wait till they finish
		for (i=0; i<10000; i++) thread[i]=new test(i);
		for (i=0; i<10000; i++) thread[i].start();
		for (i=0; i<10000; i++) thread[i].join();
// If the code works "correctly", each instance of ClassA will refer to an instance of ClassB which
// refers back to the *same* instance of ClassA.
// Test whether a[i] does actually hold an instance of ClassA;
// If so, test whether it refers to an instance of ClassB;
// If so, test whether that instance of ClassB refers back to the same instance of ClassA as we started with
		for (i=0; i<10000; i++) {
			ClassA theA=a[i];
			if (theA==null)
				System.out.println("OOPS ... a is null!");
			else {
				ClassB theB=theA.getB();
				if (theB==null)
					System.out.println("OOPS ... b is null!");
				else
				if (theB.getA() != theA)
					{System.out.println("Hey, we have a problem with 'a' number " + i);}
			}
		}
        }
}

class Factory {
	private ClassA ourA;
	private ClassB ourB;

	public ClassA createA() {
// Create an instance of ClassA and ClassB, and make them refer to each other
		ourA=new ClassA();
		ourB=new ClassB();

		ourA.setB(ourB);
		ourB.setA(ourA);

		return ourA;
	}
}

class ClassA {
// The only thing an instance of this class does, really, is to hold a reference to an instance of ClassB
	private ClassB theB;
	public void setB(ClassB b) {theB=b;}
	public ClassB getB() {return theB;}
}

class ClassB {
// And the only thing an instance of this class does, really, is to hold a reference to an instance of ClassA
	private ClassA theA;
	public void setA(ClassA a) {theA=a;}
	public ClassA getA() {return theA;}
}