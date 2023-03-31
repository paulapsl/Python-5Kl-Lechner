package DruckerAufgabe;

public class Drucker implements DruckerInterface{
	private String text;

    public Drucker(String text) {
        this.text = text;
    }

    public void drucken() {
        System.out.println("Drucke Text: " + text);
    }

	public String getText() {
		return text;
	}

	public void setText(String text) {
		this.text = text;
	}
    
    
}
