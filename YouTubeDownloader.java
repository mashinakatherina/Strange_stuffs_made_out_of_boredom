import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.util.Scanner;

public class YouTubeDownloader {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Put your link here: ");
        StringBuffer url = new StringBuffer(in.next());
        url.insert(12,"ss");

        Desktop desktop = Desktop.getDesktop();
        try {
            desktop.browse((URI.create(url.toString())));
        } catch (IOException e) {

        }
    }
}
