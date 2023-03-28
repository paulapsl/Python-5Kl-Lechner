package Aufgabe;

public class Hawaii extends Pizza{
	@Override 
	
	 public void backen() {
        System.out.println("Hawaii-Pizza wird gebacken...");
    }
    public void schneiden() {
        System.out.println("Hawaii-Pizza wird geschnitten...");
    }
    public void einpacken() {
        System.out.println("Hawaii-Pizza wird eingepackt...");
    }
    public int getPrice() { 
        return 8; 
    } 
}
