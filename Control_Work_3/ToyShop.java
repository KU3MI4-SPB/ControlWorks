package Control_Work_3;

import java.util.PriorityQueue;
import java.util.Random;

public class ToyShop {
    private PriorityQueue<Toy> toyQueue;

    public ToyShop() {
        toyQueue = new PriorityQueue<>();
    }

    public void addToy(Toy toy) {
        toyQueue.add(toy);
    }

    public int getRandomToyId() {
        Random random = new Random();
        int randomNumber = random.nextInt(10);

        int cumulativeWeight = 0;
        for (Toy toy : toyQueue) {
            cumulativeWeight += toy.getFrequency();
            if (randomNumber < cumulativeWeight) {
                return toy.getId();
            }
        }
        return -1;
    }

    public Toy getToyById(int randomToyId) {
        for (Toy toy : toyQueue) {
            if (toy.getId() == randomToyId) {
                return toy;
            }
        }
        return null;
    }
}

