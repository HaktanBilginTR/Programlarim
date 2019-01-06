import java.util.Scanner;
public class BedenKitleEndeksi {
    public static void main(String[] args){
Scanner scanner = new Scanner(System.in);
        System.out.println("Beden Kitle Endeksi Hesaplama");
        while (true){
            System.out.println("Kütle : ");
            int kutle = scanner.nextInt();
            System.out.println("Boy : ");
            float boy = scanner.nextFloat();
            float boy2 = boy*boy;
            float sonuc = (float) kutle/boy2;
            System.out.println("Sonuç : " + sonuc + "\n");

}}}