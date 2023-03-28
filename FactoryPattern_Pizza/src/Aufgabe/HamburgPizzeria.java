package Aufgabe;

public class HamburgPizzeria {

	protected Pizza createPizza(String type) {
        if (type.equals("Salami")) {
        	Salami HamburgSalami = new Salami();
        	System.out.println("Sie haben eine HamburgSalami bestellt.");
            return HamburgSalami;
        } else if (type.equals("Hawaii")) {
        	Hawaii HamburgHawaii = new Hawaii();
        	System.out.println("Sie haben eine HamburgHawaii bestellt.");
            return HamburgHawaii;
        } else if (type.equals("Calzone")) {
            Calzone HamburgCalzone = new Calzone();
            System.out.println("Sie haben eine HamburgCalzone bestellt.");
            return HamburgCalzone;
        }else if (type.equals("QuattroStagioni")) {
            QuattroStagioni HamburgQuattroStagioni = new QuattroStagioni();
            System.out.println("Sie haben eine HamburgQuattroStagioni bestellt.");
            return HamburgQuattroStagioni;
        }
        else {
            throw new IllegalArgumentException("Diese Pizza ist im Moment nicht im Sortiment!");
        }
    }
}
