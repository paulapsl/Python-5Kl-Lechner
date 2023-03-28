package DruckerAufgabe;

public class SchwarzWeiss implements Drucker{

	@Override
	public void drucken(String document) {
		System.out.println("Printing document in Black and White: " + document);
		
	}

}
