package Aufgabe;

public class RostockPizzeria extends Pizzeria{

	protected Pizza createPizza(String type) {
        if (type.equals("Salami")) {
        	Salami RostockSalami = new Salami();
        	System.out.println("Sie haben eine RostockSalami bestellt.");
            return RostockSalami;
        } else if (type.equals("Hawaii")) {
        	Hawaii RostockHawaii = new Hawaii();
        	System.out.println("Sie haben eine RostockHawaii bestellt.");
            return RostockHawaii;
        } else if (type.equals("Calzone")) {
            Calzone RostockCalzone = new Calzone();
            System.out.println("Sie haben eine RostockCalzone bestellt.");
            return RostockCalzone;
        }else if (type.equals("QuattroStagioni")) {
            QuattroStagioni RostockQuattroStagioni = new QuattroStagioni();
            System.out.println("Sie haben eine RostockQuattroStagioni bestellt.");
            return RostockQuattroStagioni;
        }
        else {
            throw new IllegalArgumentException("Diese Pizza ist im Moment nicht im Sortiment.");
        }
    }
}
