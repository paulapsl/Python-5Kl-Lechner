package Aufgabe;

public class QuattroStagioni extends Pizza {
	@Override 
	
	public void backen() {
        System.out.println("Quattro Stagioni-Pizza wird gebacken...");
    }
    public void schneiden() {
        System.out.println("Quattro Stagioni-Pizza wird geschnitten...");
    }
    public void einpacken() {
        System.out.println("Quattro Stagioni-Pizza wird eingepackt...");
    }
    public int getPrice() { 
        return 13; 
    } 
}
