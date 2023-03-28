package Aufgabe;

import java.util.Scanner;

public class Client {

	public static void main(String[] args) { 
		System.out.println("Welche Pizza wollen Sie bestellen [Salami, Calzone, Hawaii, QuattroStagioni]?");
		Scanner scanner = new Scanner(System.in);
		String pizzatype = scanner.nextLine();
        HamburgPizzeria hp = new HamburgPizzeria();
        Pizza p = hp.createPizza(pizzatype);
        p.backen();
        p.schneiden();
        p.einpacken();
        System.out.println("Zu bezahlen sind [€]: ");
        System.out.println(p.getPrice()); 
    } 
	
}
