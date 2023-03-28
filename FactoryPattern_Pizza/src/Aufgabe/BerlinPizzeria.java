package Aufgabe;

public class BerlinPizzeria extends Pizzeria{
	
	protected Pizza createPizza(String type) {
        if (type.equals("Salami")) {
        	Salami BerlinSalami = new Salami();
        	System.out.println("Sie haben eine BerlinSalami bestellt.");
            return BerlinSalami;
        } else if (type.equals("Hawaii")) {
        	Hawaii BerlinHawaii = new Hawaii();
        	System.out.println("Sie haben eine BerlinHawaii bestellt.");
            return BerlinHawaii;
        } else if (type.equals("Calzone")) {
            Calzone BerlinCalzone = new Calzone();
            System.out.println("Sie haben eine BerlinCalzone bestellt.");
            return BerlinCalzone;
        }else if (type.equals("QuattroStagioni")) {
            QuattroStagioni BerlinQuattroStagioni = new QuattroStagioni();
            System.out.println("Sie haben eine BerlinQuattroStagioni bestellt.");
            return BerlinQuattroStagioni;
        }
        else {
            throw new IllegalArgumentException("Diese Pizza ist im Moment nicht im Sortiment!");
        }
    }
}
