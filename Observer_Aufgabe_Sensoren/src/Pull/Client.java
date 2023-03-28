package Pull;

public class Client {
	public static void main(String[] args) {
		WeatherStation weatherStation = new WeatherStation();

		//add Observer passiert in Display bzw. ColorSignal-Klasse
		
        Display display = new Display(weatherStation);
        ColorSignal light = new ColorSignal(weatherStation);

        // Set new measurements
        weatherStation.setMeasurements(100, 60);
    }
}
