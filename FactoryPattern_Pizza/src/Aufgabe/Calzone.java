package Aufgabe;

public class Calzone extends Pizza{
	@Override 
	
	public void backen() {
        System.out.println("Calzone-Pizza wird gebacken...");
    }
    public void schneiden() {
        System.out.println("Calzone-Pizza wird geschnitten...");
    }
    public void einpacken() {
        System.out.println("Calzone-Pizza wird eingepackt...");
    }
    
    public int getPrice() { 
        return 10; 
    } 
}
