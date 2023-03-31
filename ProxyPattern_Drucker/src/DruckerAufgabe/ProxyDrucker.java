package DruckerAufgabe;

public class ProxyDrucker implements DruckerInterface{
	private Drucker drucker;
    private boolean schwarzWeiss;

    public ProxyDrucker(String text, boolean schwarzWeiss) {
        this.drucker = new Drucker(text);
        this.schwarzWeiss = schwarzWeiss;
    }

    public void switchToSchwarzWeiss(boolean schwarzWeiss) {
        this.schwarzWeiss = schwarzWeiss;
    }

    public void drucken() {
        if (schwarzWeiss) {
            System.out.println("Drucke Text in Schwarz-Weiﬂ: " + drucker.getText());
        } else {
        	System.out.println("Drucke Text in Farbe: " + drucker.getText());
        }
    }

}
