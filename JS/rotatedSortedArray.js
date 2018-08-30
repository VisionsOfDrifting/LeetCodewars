/* This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array). 

You can assume all the integers in the array are unique. */

function rotatedBinarySearch(array, target) {
  var low = 0, high = array.length-1;
  while(low <= high) {
    mid = Math.floor((low+high)/2);
    console.log('Index: ', low, mid, high);
    console.log('Value: ', array[low],array[mid],array[high]);
    if(array[mid] === target) {
      return mid;
    } else if(array[mid] > target) {
      if(array[high] > array[mid] || array[low] <= target) {
        high = mid - 1;
      } else { // (array[high] <= array[mid] || array[low] > target)
        low = mid + 1;
      }
    } else { // (array[mid] <= target)
      if(array[low] < array[mid] || array[high] >= target){
        low = mid + 1;
      } else { // (array[low] >= array[mid] || array[high] < target)
        high = mid -1;
      }
    }
  }
  return null;
}


array = [13, 18, 25, 2, 8, 10];
target = 8;
console.log('Array:', array);
console.log('Target:', target);
console.log(rotatedBinarySearch(array, target));

