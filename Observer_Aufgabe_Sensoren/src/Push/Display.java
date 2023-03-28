package Push;

//der konkrete Beobachter
public class Display implements Observer {
	private double temperature;
    private double humidity;

    //hier werden Daten direkt mit übergeben
    @Override
    public void update(double temperature, double humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    public void display() {
        System.out.println("Current temperature: " + temperature + " degrees Celsius");
        System.out.println("Current humidity: " + humidity + "%");
    }
}
