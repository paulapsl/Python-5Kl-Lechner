package Push;

public class Client {
	public static void main(String[] args) {
		// Instanz der Wetterstation
        WeatherStation weatherStation = new WeatherStation();
        
        // Instanz der konkreten Beobachter
        Display display = new Display();
        ColorSignal light = new ColorSignal();
        
        // zum Observer hinzuf�gen
        weatherStation.addObserver(display);
        weatherStation.addObserver(light);

        // Messwerte �bergeben
        weatherStation.setMeasurements(20, 60);
    }
}
