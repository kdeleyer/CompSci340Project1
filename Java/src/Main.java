//written by PennP

public class Main {
    //test array inputs
    static int[] auto = new int[]{10, 50, 100, 500, 1000, 2500, 5000};
    //tracker for runtime
    static int[][][] tracker = new int[7][7][3];
    public static void main(String[] args) {
        //five runs
        for(int j = 0; j<7;j++){
            //track runs in inner loop
            int t = 0;
            for (int i : auto) {
                //test runs
                //Array size
                System.out.println("Working on array size of: " + i);
                //test 1
                int[] array = createArray(i);
                tracker[j][t][0] = sum(i, array);

                //test2
                int[][] matrix1 = createMatrix(i, i);
                int[][] matrix2 = createMatrix(i, i);
                tracker[j][t][1] = scalarmatmult(i, matrix1, i, matrix2);

                //test 3
                int[][] matrix3 = createMatrix(i, i);
                tracker[j][t][2] = matrixmult(i, matrix1, matrix2, matrix3);

                //add t
                t+=1;
        }
        }
        //totals
        printTot();



    }

    //sum of the array added togeather
    public static int sum(int n, int arr[]) {
        //result
        int result = 0;
        //ms start time
        long begin = System.nanoTime();
        //for i less than n
        for (int i = 0; i < n; i++) {
            result = result + arr[i];
        }
        //end
        long end = System.nanoTime();
        //print runtime
        return(int)(end-begin);
    }

    //algo 2
    public static int scalarmatmult(int n, int[][] a, int b, int[][] c) {
        //ms start time
        long begin = System.nanoTime();
        //for
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                c[i][j] = a[i][j] * b;
            }
        }
        //end time
        long end = System.nanoTime();
        //print runtime
        return(int)(end-begin);
    }

    //algo 3
    //product of two matrixes
    public static int matrixmult(int n, int[][] a, int[][] b, int[][] c) {
        //being time
        long begin = System.nanoTime();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                c[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    c[i][j] = c[i][j] + a[i][k] * b[k][j];
                }
            }
        }
        //end time
        long end = System.nanoTime();
        return(int)(end-begin);
    }

    //matrix creator
    public static int[][] createMatrix(int a, int b) {
        int[][] matrix = new int[a][b];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = (int) (Math.random() * 10);
            }
        }
        //return
        return matrix;
    }
    //array creator
    public static int[] createArray(int a){
        int [] array = new int[a];
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) (Math.random() * 10);
        }
        return array;
    }

    //total runtimes
    public static void printTot(){
        //for methods
        for(int i = 0; i<3;i++){
            //for size
            for(int j = 0; j<7; j++){
                //sum to print
                int total = (tracker[0][j][i]+tracker[1][j][i]+tracker[2][j][i]+tracker[3][j][i]+tracker[4][j][i]+tracker[5][j][i]+tracker[6][j][i])/7;
                //print runtime (sorry for the long line)
                System.out.println("The runtime of algorithm " + (i+1) + " in nanoseconds for size " + auto[j] + " is " + total);
            }
        }
    }
}
