import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class 2DArray {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int arr_i=0; arr_i < 6; arr_i++){
            for(int arr_j=0; arr_j < 6; arr_j++){
                arr[arr_i][arr_j] = in.nextInt();
            }
        }
        
        int sum = sumOfHourglass(0, arr);
        for(int i = 0; i < 22; i++)
        {
            if (i%6 ==4 || i%6 == 5) continue;
            if (sumOfHourglass(i, arr) > sum)
            {
                
                sum = sumOfHourglass(i, arr);   
            }
        }
        
        System.out.println(sum);
    }
    
    public static int sumOfHourglass(int start, int[][] arr)
    {
        int row = start / 6;
        int col = start % 6;
        
        return arr[row][col]  + arr[row + 2][col] + arr[(row)][col + 1] + arr[(row + 1)][col + 1] + arr[(row + 2)][col + 2] + arr[(row + 2)][col + 1] + arr[(row)][col + 2] ;
    }
}
