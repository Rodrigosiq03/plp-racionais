public class TesteRacional {
    public static void main(String[] args) {
        Racional result1 = new Racional(5, 7);
        Racional result2 = new Racional(3, 4);
        double resultado_razao = result1.razao();
        Racional resultado_soma = result2.sum(result1);
        System.out.println("/RAZAO/ O resultado entre os dois valores inseridos foi de " + resultado_razao);
        System.out.println("/SOMA/ O resultado entre os dois valores inseridos foi de " + resultado_soma.razao());
    }
}
