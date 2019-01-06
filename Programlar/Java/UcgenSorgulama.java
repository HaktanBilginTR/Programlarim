import java.util.Scanner;

public class UcgenSorgulama {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);


        System.out.println("Üçgen Sorgulama");
        while (true){
            System.out.print("1. Kenar : ");
            int kenar1 = scanner.nextInt();
            System.out.print("2. Kenar : ");
            int kenar2 = scanner.nextInt();
            System.out.print("3. Kenar : ");
            int kenar3 = scanner.nextInt();
            if( kenar1 + kenar2 > kenar3 && kenar3 > kenar1 - kenar2){
                System.out.println("Bu Bir Üçgendir.");
            }


            else{
                System.out.println("Bu Bir Üçgen Değildir.");




            }

            }













    }





}
