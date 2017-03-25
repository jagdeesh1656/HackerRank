import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        String s = in.next();
        long n = in.nextLong();
        
        long numberOfRepititions = n / s.length();
        long numberOfAs = s.length() - s.replace("a", "").length();
        long result = numberOfRepititions * numberOfAs;
        
        if (n % s.length() != 0)
        {
            for (int i = 0; i < n % s.length(); i++)
            {
                if (s.charAt(i) == 'a')
                    result ++;   
            }
                
        }
        
        System.out.println(result);
    }
}
