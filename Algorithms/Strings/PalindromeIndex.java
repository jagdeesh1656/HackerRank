import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
	public static boolean isPalindrome(String givenString)
    {
        if ((givenString.charAt(0) != givenString.charAt(givenString.length() - 1)))
            return false;
        if (givenString.length() <= 1)
            return true;
        
        int halfLength = givenString.length() / 2;
        
        String halfString = null;
        String otherHalf = null;
        halfString = givenString.substring(0, halfLength);
        if (givenString.length() % 2 == 0)
        {
            otherHalf = givenString.substring(halfLength, givenString.length());
        }
        else if ((givenString.length() + 1) % 2 == 0)
        {
            otherHalf = givenString.substring(halfLength + 1, givenString.length());
        }
         
        if (halfString != null && otherHalf != null)
        {
            StringBuilder sb = new StringBuilder(otherHalf);
            if (halfString.equals(sb.reverse().toString()))
                return true;
        }
        
        return false;
        
    }
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner reader = new Scanner(System.in);
        int testCases = Integer.parseInt(reader.nextLine());
        for (int  i = 0; i < testCases; i++)
        {
            
            String givenString = reader.nextLine();
            givenString = givenString.toLowerCase();
            char firstCharacter = '\0';
            char lastCharacter = '\0';
            int firstIndex = -1;
            int lastIndex = -1;
            
            if(givenString != null && givenString.trim().length() >= 1)
            {   
                firstCharacter = givenString.charAt(0);
                lastCharacter = givenString.charAt(givenString.length() - 1);
                
                firstIndex = 0;
                lastIndex = givenString.length() - 1;
            }
            
            if(isPalindrome(givenString))
            {
               System.out.println("-1");
               continue;
            }
            
            while (firstIndex <= lastIndex)
            {
                if (givenString.charAt(firstIndex) == givenString.charAt(lastIndex))
                {
                    firstIndex ++;
                    lastIndex --;
                }
                else
                {
                    if(isPalindrome(givenString.substring(0, firstIndex) + givenString.substring(firstIndex + 1)))
                        System.out.println(firstIndex);
                    else 
                        System.out.println(lastIndex);
                    break;
                }
            }
        }
    }
}
