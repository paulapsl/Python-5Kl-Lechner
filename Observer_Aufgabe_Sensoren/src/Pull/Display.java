package Pull;

//der konkrete Beobachter
public class Display implements Observer {
	//Instanz von Subject, um getter aufrufen zu können
	private Subject subject;

    public Display(Subject subject) {
        this.subject = subject;
        subject.addObserver(this);
    }
    
    //hier müssen getter aufgerufen werden, weil Werte von WeatherStation nicht übergeben werden
    @Override
    public void update() {
        double temperature = subject.getTemperature();
        double humidity = subject.getHumidity();
        display(temperature, humidity);
    }

    public void display(double temperature, double humidity) {
        System.out.println("Current temperature: " + temperature + " degrees Celsius");
        System.out.println("Current humidity: " + humidity + "%");
    }
}
