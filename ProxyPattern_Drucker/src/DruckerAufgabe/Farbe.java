package DruckerAufgabe;

public class Farbe implements Drucker {

	@Override
	public void drucken(String document) {
		System.out.println("Printing document in Color: " + document);
		
	}
}
