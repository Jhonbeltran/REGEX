import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InvalidObjectException;

public class regex {
  public static void main(String[] args) {
    String file = "../../files/results.csv";

    try {
      BufferedReader br = new BufferedReader(new FileReader(file));
      String line;

      while((line = br.readLine()) != null) {
        System.out.println(line);
      }

      br.close();
    } catch(IOException err) {
      System.out.println(err);
    }
  }
}