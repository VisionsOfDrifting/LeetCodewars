import java.util.*;
public class twoSum{

   public static int[] twoSum(int[] nums, int target) {
      int[] arr = new int[2];
      int[] key = new int[2];
      boolean found = false;
      HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
      /* iterate through the array */
      for(int i = 0; i < nums.length; i++){
         /* check if the map has an element which is equal to the difference
          * between the target and current element */
         Integer val = map.get(target - nums[i]);
         if(val == null){ // no match found, add the current item and index to map
            map.put(nums[i], i);
         }else{ // match found, update the index values
            key[0] = target - nums[i];
            key[1] = nums[i];
            arr[0] = val;
            arr[1] = i;
            found = true;
            break;
         }
      }
      if(found){ System.out.println("Match Found!");
                System.out.println(key[0] + " + " + key[1] + " = " + target);
      }else{System.out.println("No Match Found");}
      return arr;
   }

   public static void main(String[] args){
      int[] nums = {1, 7, 11, 15};
      for(int x: nums) System.out.print(x+" ");
      System.out.println();
      int target = 22;
      System.out.println("target = " + target);
      for(int x: twoSum(nums, target)) System.out.print(x+" ");
      System.out.println();
   }

}