package Pull;

public class ColorSignal implements Observer{
	private Subject subject;

    public ColorSignal(Subject subject) {
        this.subject = subject;
        subject.addObserver(this);
    }
     //update arbeitet hier bei der Pull-Methode nur mit gelieferten Daten über Getter
    @Override
    public void update() {
        double temperature = subject.getTemperature();
        lightUp(temperature);
    }

    public void lightUp(double temperature) {
        if (temperature > 100) {
            System.out.println("Red light on");
        } else if (temperature < 0) {
            System.out.println("Blue light on");
        } else {
            System.out.println("Green light on");
        }
    }
}
