import java.util.Arrays;
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int fleet = 0;
        double carFleetTime = Double.NEGATIVE_INFINITY;

        int n = position.length;
        Car[] cars = new Car[n];
        for (int i = 0; i < n; i++) {
            cars[i] = new Car(position[i], (double)(target - position[i]) / speed[i]);
        }
        Arrays.sort(cars, (a, b) -> Double.compare(b.position, a.position));

        for (Car car : cars) {
            double reachTime = car.reachTime;
            if (reachTime > carFleetTime) {
                carFleetTime = reachTime;
                fleet++;
            }
        }

        return fleet;
    }

    private static class Car {
        int position;
        double reachTime;

        Car(int position, double reachTime) {
            this.position = position;
            this.reachTime = reachTime;
        }
    }
}
