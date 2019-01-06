import java.util.Scanner;
public class GirisYapma {
    public static void main(String[] args){
        String ozad = "Haktan";
        String ozsifre = "4181887";
        Scanner scanner = new Scanner(System.in);
        while (true){
            System.out.print("Kullanıcı Adınız : ");
            String ad = scanner.nextLine();
            System.out.print("Sifreniz : ");
            String sifre = scanner.nextLine();
            if(sifre.equals(ozsifre) && ad.equals(ozad)){
                System.out.println("Hoşgeldin " + ad);
                break;
            }
            else{
                System.out.println("Yanlış Girildi. Tekrar Deneyin");
            }}
    }
}
