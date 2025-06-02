import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
        String input = br.readLine().strip();
        if (input.isEmpty()) {
            bw.write("0");
        } else {
            String[] tokens = input.split(" ");
            bw.write(Integer.toString(tokens.length));
        }

        bw.flush();

        bw.close();
        br.close();
    }
}
