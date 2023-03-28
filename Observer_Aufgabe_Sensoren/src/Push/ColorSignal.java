package Push;

public class ColorSignal implements Observer{
	private double temperature;

	//im Gegensatz zur Pull-Methode werden hier temperature und humidity �bergeben und
	//m�ssen nicht �ber getter und setter bezogen werden
    @Override
    //hier wird ein Nachteil vom Push-Prinzip ersichtlich: es wird auch die Info
    //humidity �bergeben, die gar nicht gebraucht wird
    public void update(double temperature, double humidity) {
        this.temperature = temperature;
        lightUp();
    }

    public void lightUp() {
        if (temperature > 100) {
            System.out.println("Red light on");
        } else if (temperature < 0) {
            System.out.println("Blue light on");
        } else {
            System.out.println("Green light on");
        }
    }
}
