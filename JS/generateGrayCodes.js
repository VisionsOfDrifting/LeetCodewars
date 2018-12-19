/*
// This function generates all n bit Gray codes and prints the
// generated codes
function generateGrayarr(n) {
  // base case
  if (n <= 0) {
    return;
  }
  // 'arr' will store all generated codes
  let arr = [];
  // start with one-bit pattern
  arr.push("0");
  arr.push("1");
  // Every iteration of this loop generates 2*i codes from previously
  // generated i codes.
  console.log(arr);
  let i = 0,
    j = 0;
  for (i = 2; i < 1 << n; i = i << 1) {
    // Enter the prviously generated codes again in arr[] in reverse
    // order. Nor arr[] has double number of codes.
    console.log(i);
    for (j = i - 1; j >= 0; j--) {
      arr.push(arr[j]);
    }
    // append 0 to the first half
    for (j = 0; j < i; j++) {
      arr[j] = "0" + arr[j];
    }
    // append 1 to the second half
    for (j = i; j < 2 * i; j++) {
      arr[j] = "1" + arr[j];
    }
  }
  // print contents of arr[]
  for (i = 0; i < arr.len; i++) {
    console.log(arr[i]);
  }
}

generateGrayarr(3);
*/

function generateGrayarr(n) {
  if (n <= 0) {
    return;
  }
  let arr = [];
  arr.push("0");
  arr.push("1");
  let i = 0,
    j = 0;
  for (i = 2; i < 1 << n; i = i << 1) {
    console.log("Outer");
    console.log("i", i);
    for (j = i - 1; j >= 0; j--) {
      console.log("Inner First");
      console.log("j", j, "arr[j]", arr[j]);
      arr.push(arr[j]);
    }
    for (j = 0; j < i; j++) {
      console.log("Inner Second");
      console.log("j", j, "arr[j]", arr[j]);
      arr[j] = "0" + arr[j];
    }
    for (j = i; j < 2 * i; j++) {
      console.log("Inner Third");
      console.log("j", j, "arr[j]", arr[j]);
      arr[j] = "1" + arr[j];
    }
    console.log("End");
    console.log(arr);
  }
  // console.log(arr);
}

generateGrayarr(5);
