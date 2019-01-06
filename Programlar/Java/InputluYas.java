import java.util.Scanner;
public class InputluYas {
    public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
        System.out.println("Yaş Giriniz = ");
    int yas = scanner.nextInt();
    if (yas >= 18){
        System.out.println("Girebilirsiniz ");

    }
    else{
            System.out.println("Giremezsin !");
        }
    }

}
