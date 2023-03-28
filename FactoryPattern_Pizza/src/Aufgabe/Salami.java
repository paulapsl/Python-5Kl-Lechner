package Aufgabe;

public class Salami extends Pizza{
	@Override 
	
	public void backen() {
        System.out.println("Salami-Pizza wird gebacken...");
    }
    public void schneiden() {
        System.out.println("Salami-Pizza wird geschnitten...");
    }
    public void einpacken() {
        System.out.println("Salami-Pizza wird eingepackt...");
    }
    public int getPrice() { 
        return 12; 
    } 

}
