//translated the algos

public class Main {
  public static void main(String[] args) {
    //test 1
    int[] array = {1,2,3,4,5};
    System.out.println(sum(5,array));

    //test2
    int[][] matrix1 = createMatrix(5,5);
    int[][] matrix2 = createMatrix(5,5);
    scalarmatmult(5, matrix1, 5, matrix2);

    //test 3
    int[][] matrix3 = createMatrix(5,5);
    matrixmult(5, matrix1, matrix2, matrix3);
    
    
  }
  //sum of the array added togeather
  public static int sum(int n, int arr[]) {
    //ms start time
    Long begin = System.nanoTime(); 
    //result start
    int result = 0;
    //for i less than n
    for(int i =0 ; i<n ; i++){
        result = result +arr[i];
    }
    //end
    long end = System.nanoTime();
    //print runtime
    System.out.println("The runtime is : " + (end-begin) + " nano seconds");
    return result;
  }
  //algo 2
  public static void scalarmatmult(int n, int[][] a, int b, int[][] c){
  //ms start time
    long begin = System.nanoTime();
  //for
    for(int i = 0; i<n;i++){
      for(int j = 0; j<n;j++){
        c[i][j] = a[i][j] *b;
      }
    }
    //end time
    long end = System.nanoTime();
    //print runtime
    System.out.println("The runtime is : " + (end-begin) + " nano seconds");
 }
  //algo 3
  //product of two matrixes
  public static void matrixmult(int n, int[][] a, int[][] b, int[][] c){
    //being time
    long begin = System.nanoTime();
    for(int i = 0; i<n;i++){
      for(int j = 0; j<n;j++){
        c[i][j] = 0;
        for(int k = 0; k<n;k++){
          c[i][j] = c[i][j] + a[i][k] * b[k][j];
        }
        }
      }
    //end time
    long end = System.nanoTime();
    System.out.println("The runtime is : " + (end-begin) + " nano seconds");
  }

  //matrix creator
  public static int[][] createMatrix(int a, int b){
    int[][] matrix = new int[a][b];
    for (int i=0; i<matrix.length; i++) {
        for (int j=0; j<matrix[i].length; j++) {
            matrix[i][j] = (int) (Math.random()*10);
        }
      }
    //return
    return matrix;
  }
  }

  


  // @Test
  // void addition() {
  //     assertEquals(2, 1 + 1);
  // }
