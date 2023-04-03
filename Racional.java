public class Racional {
    private int numerador;
    private int denominador;

    Racional(int numerador, int denominador) {
        // validação de primos entre si
        for (int i = Math.min(numerador, denominador); i >= 2; i--) {
            if (numerador % i == 0 && denominador % i == 0) {
                numerador = numerador / i;
                denominador = denominador / i;

            }
        }

        this.numerador = numerador;
        this.denominador = denominador;

    }

    public double razao() {
        return (double) numerador / denominador;
    }

    public Racional sum(Racional r1) {
        int numerador = (r1.numerador * this.denominador) + (this.numerador * r1.denominador);
        int denominador = this.numerador * this.denominador;

        return new Racional(numerador, denominador);
        
    }

    public Racional sub(Racional r1) {
        int numerador = (r1.numerador * this.denominador) - (this.numerador * r1.denominador);
        int denominador = this.numerador * this.denominador;
        return new Racional(numerador, denominador);
    }

    public Racional mult(Racional r1) {
        int numerador = this.numerador * r1.numerador;
        int denominador = this.denominador * r1.denominador;
        return new Racional(numerador, denominador);
    }

}