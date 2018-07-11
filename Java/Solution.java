// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
   public static String solution(String S, int K) {
      // write your code in Java SE 8
      String retString = "";
      String retString2 = "";
      Pattern p = Pattern.compile("[a-zA-Z0-9]");
      S = S.toUpperCase();
      //System.out.println(S);
      int counter = 0;
      for(int i = S.length(); i > 0; --i){
         String c = S.substring(i-1,i); //Specify (begin index, end index)
         //System.out.println(c);
         Matcher m = p.matcher(c);
         //System.out.println(m.find());
         if(m.find() == true){
            if(counter == K){
               counter = 1; //to get into this if we must have found a char
               if(K != 0){
                   retString2 = retString2.concat("-");
               }
            }else{
               ++counter;
            }
            retString2 = retString2.concat(c);
         }
         //System.out.println(retString2);
         //System.out.println("Counter: "+counter);
      }
      //reverse the string twice to get proper output
      for(int i = retString2.length(); i > 0; --i){
         retString = retString.concat(retString2.substring(i-1,i));
      }
      //System.out.println(retString);
      //Total runtime should be O(3N) = O(N)
      //Total space should be O(2N) = O(N)
      return retString;
   }

   public static void main(String[] args){
      //String S = "2-4A0r7-4k";
      //int K = 4;
      String S = "2-4A0r7-4k";
      int K = 3;
      //String S = "r";
      //int K = 1;
      System.out.println(solution(S,K));
   }
}
/*

Compilation successful.

Example test:   ('2-4A0r7-4k', 4)
OK

Example test:   ('2-4A0r7-4k', 3)
OK

Example test:   ('r', 1)
OK

Your test case: ['233-asl-asfjn-ansk', 5]
Returned value: '233AS-LASFJ-NANSK'

Your test case: ['30-12-21-32-req-31-23r-v-23v-br-3fe-00', 3]
Returned value: '301-221-32R-EQ3-123-RV2-3VB-R3F-E00'

Your test case: ['----------------', 1]
Returned value: ''

Your test case: ['30-12-21-32-req-31-23r-v-23v-br-3fe-00', 0]
Returned value: '30122132REQ3123RV23VBR3FE00'

Your test case: ['----------------', 0]
Returned value: ''

Your test case: ['nwqnfhiwohvlknbwgobvlkbeobkeqf', 7]
Returned value: 'NW-QNFHIWO-HVLKNBW-GOBVLKB-EOBKEQF'

Your code is syntactically correct and works properly on the example test.
Note that the example tests are not part of your score. 
On submission at least 8 test cases not shown here will assess your solution.
*/