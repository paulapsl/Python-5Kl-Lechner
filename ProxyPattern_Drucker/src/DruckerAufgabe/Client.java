package DruckerAufgabe;

public class Client {

	public static void main(String[] args) {
        Drucker blackAndWhitePrinter = new SchwarzWeiss();
        Drucker colorPrinter = new Farbe();

        blackAndWhitePrinter.drucken("Hello, world!");
       
        colorPrinter.drucken("Hello, world!");

	}

}
