package DruckerAufgabe;

public class Client {

	public static void main(String[] args) {
        DruckerInterface drucker = new ProxyDrucker("Dies ist ein Test", true);
        drucker.drucken();

        ((ProxyDrucker) drucker).switchToSchwarzWeiss(false);
        drucker.drucken(); 
    }
}
