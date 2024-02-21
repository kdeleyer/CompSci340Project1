//translated the algos

import java.time.Instant;
import java.time.Duration;
public class Main {
  public static void main(String[] args) {
    //test 1
    //int[] array = {1,2,3,4};
    //System.out.println(sum(4,array));

    //test2
    
    
  }
  public static int sum(int n, int arr[]) {
    //ms start time
    Instant being = Instant.now();
    //result start
    int result = 0;
    //for i less than n
    for(int i =0 ; i<n ; i++){
        result = result +arr[i];
    }
    //end
    Instant end = Instant.now();
    //print runtime
    System.out.println("The runtime is : " + Duration.between(being,end));
    return result;
  }
  //algo 2
  public static void scalarmatmult(int n, int[][] a,     int b, int[][] c){
  //ms start time
  Instant being = Instant.now();
  //for
  for(int i = 0; i<n;i++){
    for(int j = 0; j<n;i++){
      c[i][j] = a[i][j] *b;
    }
  }
  //end time
  Instant end = Instant.now();
  //print runtime
  System.out.println("The runtime is : " + Duration.between(being,end));
 }
  //algo 3
  public static void matrixmult(int n, int[][] a, int[][] b, int[][] c){
    //being time
    Instant being = Instant.now();
    for(int i = 0; i<n;i++){
      for(int j = 0; j<n;j++){
        c[i][j] = 0;
        for(int k = 0; k<n;k++){
          c[i][j] = c[i][j] + a[i][k] * b[k][j];
        }
        }
      }
    //end time
    Instant end = Instant.now();
    System.out.println("The runtime is : " + Duration.between(being,end));
  }
  }

}
