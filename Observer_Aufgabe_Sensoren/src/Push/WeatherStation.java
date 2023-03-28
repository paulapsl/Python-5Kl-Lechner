package Push;

import java.util.ArrayList;
import java.util.List;

//das konkrete Subjekt --> Observable (Push-Variante)
public class WeatherStation implements Subject{
	private List<Observer> observers;
    private double temperature;
    private double humidity;

    public WeatherStation() {
        observers = new ArrayList<>();
    }
    
    // Aktualisiert die Messwerte und benachrichtigt alle Observer 
    public void setMeasurements(double temperature, double humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        notifyObservers();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }
    
    //temperature und humidity in update mitgesendet
    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(temperature, humidity);
        }
    }

}
