package Pull;

public interface Subject {
	void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
    double getTemperature();
    double getHumidity();

}
