package Control_Work_3;

import java.io.FileWriter;
import java.io.IOException;

public class Program {
    public static void main(String[] args) {
        ToyShop toyShop = new ToyShop();
        toyShop.addToy(new Toy(1, "конструктор", 2));
        toyShop.addToy(new Toy(2, "робот", 2));
        toyShop.addToy(new Toy(3, "кукла", 6));

        try {
            FileWriter fileWriter = new FileWriter("Control_Work_3/result.txt");
            for (int i = 0; i < 10; i++) {
                int randomToyId = toyShop.getRandomToyId();
                Toy toy = toyShop.getToyById(randomToyId);
                String nameToy = toy.getName();
                fileWriter.write(randomToyId + " " + nameToy + "\n");
            }
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
