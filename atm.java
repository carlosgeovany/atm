import java.text.SimpleDateFormat;
import java.util.Scanner;
import java.util.*;
import java.util.List;



public class atm {
    public static void main(String args[]) {
        System.out.println("Bienvenido a su cajero automático...");
        int saldo = 1000;
        int flag = 0;
        int intentos = 3;
        List<List<String>> historico = new ArrayList<>();
        Scanner input = new Scanner(System.in);
        String pwd = "1235", password = "";
        System.out.println("Ingrese su contraseña, solo tiene 3 intentos");

        while (!password.equals(pwd)){
            password = input.next();
            flag ++;
            intentos --;
            System.out.println("contraseña incorrecta, vuelve a intentarlo, te quedan "+intentos+" intentos...");
            if (flag == 3){
                System.out.println("Lo sieto ha superado el límete máximo de intentos. Finalizando el programa");
                break;
            }
        }
        if(password.equals(pwd)){
            System.out.println("Bienvenido Carlos");
            String opcion;
            boolean salida = false;
            do {
                String mainMenu = ("====MENU==== \n"
                        + "1.Consultar saldo\n"
                        + "2.Retiro de efectivo\n"
                        + "3.Histórico de movimientos\n"
                        + "4.Salir\n");
                System.out.println(mainMenu);
                System.out.println("Selecciona la opción deseada: ");

                opcion = input.next();

                switch (opcion) {
                    case "1":
                        System.out.println("Consulta de Saldo");
                        System.out.println("Su actual es de $" + saldo + " pesos");
                        break;

                    case "2":
                        System.out.println("Retiro de Efectivo");
                        if (saldo == 0){
                            System.out.println("Lo sentimos su saldo actual es de $0 pesos");
                        }
	    	            else
                            try{
                                System.out.println("¿Qué cantidad desea retirar? ");
                                int retiro = input.nextInt();
                                if (retiro > saldo){
                                    System.out.println("Fondos insuficientes...");
                                }
		    		            else{
                                    String fecha = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new java.util.Date());
                                    List<String> temp = new ArrayList<String>();
                                    temp.add(Integer.toString(saldo));
                                    temp.add(Integer.toString(retiro));
                                    temp.add(fecha);
                                    historico.add(temp);
                                    saldo -= retiro;
                                    System.out.println("Retiro realizado con éxito");
		    		            }
                            } catch (Exception e) {
                                System.out.println("Introduce solo valores numéricos enteros...");
                            }
                        break;
                    case "3":
                        System.out.println("Histórico de movimientos");
                        if (historico.size() == 0){
                            System.out.println("Cuenta sin movimientos");
                        }
                        else{
                            System.out.println("[Saldo Inicial, Retiro, Fecha]");
                            for (int i = 0; i < historico.size(); i++)
                                System.out.print(historico.get(i) + "\n");
                        }
                        break;
                    case "4":
                        salida = true;
                        System.out.println("Gracias por usar su cajero automático, hasta luego");
                        break;
                    default:
                        System.out.println("Opción inválida, inténtelo de nuevo...");
                        break;
                }
            } while(!salida);
        }
    }
}
