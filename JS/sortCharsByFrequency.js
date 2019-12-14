/** Question:
 * This problem was asked by Twitter.
 *
 * Given a string, sort it in decreasing order based on the frequency of 
 * characters. If there are multiple possible solutions, return any of them.
 *
 * For example, given the string tweet, return tteew. 
 * eettw would also be acceptable.
 * 
 * Approach: 
 * There is of course an O(N^2) solution. 
 * There is also a BTS solution that runs in O(Nlog(N)).
 * Finally there is a Hash Table / Map solution that runs in O(Nlog(N)).
 * https://afteracademy.com/blog/sort-characters-by-frequency
 * 
 * The following code is my implementation of the hash map solution in JS.
 * We will create two maps.
 * 1) char => frequency
 * 2) frequency => [...chars]
 * If we could create the second map without the first it would slightly
 * optimize space.
 * 
 * Once we have the second map we can itterate over the keys and generate the
 * string we want in reverse order. 
 * E.G. instead of 'tteew' we have 'weett' and we will reverse it.
 * Note: we must sort the keys and the value array of the second map to have
 * a uniform outcome.
 * https://stackoverflow.com/questions/5467129/sort-javascript-object-by-key
 * 
 * In another programing language like Python it may be trivial to simply 
 * construct the string in reverse order, but since JavaScript does not
 * natively support itterating through strings I am relying on the built in 
 * array methods. By this I mean using the 'of' keyword, you could always
 * write a loop and use str.charAt(i), but this would be rather verbose.
 * 
 * My hope in writing the code using the 'of' keyword is that it would
 * translate rather well into Python changing the syntax to say:
 * for ch in arr:
 *     ...
 */

'use strict';

function sortByFrequentChars(str) {
  let frequencies = {};
  let arr = str.split('');

  // Populate the first map
  for (let ch of arr) {
    if (frequencies[ch]) {
      frequencies[ch] = frequencies[ch] + 1;
    } else {
      frequencies[ch] = 1;
    }
  }

  console.log(frequencies);

  let chars = {};

  // Populate the second map
  for (let key of Object.keys(frequencies)) {
    if (chars[frequencies[key]]) {
      chars[frequencies[key]].push(key);
    } else {
      chars[frequencies[key]] = [key];
    }
  }

  console.log(chars);

  let retArr = [];

  // Populate the return array
  for (let key of Object.keys(chars).sort()) {
    let currentInt = parseInt(key, 10);
    for (let ch of chars[currentInt].sort()) {
      for (let i = 0; i < currentInt; i++) {
        retArr.push(ch);
      }
    }
  }

  console.log(retArr);
  // Construct the return string
  return retArr.reverse().join('');
}


// const input = 'halalelluejah';
const input = 'tweet';
const output = sortByFrequentChars(input);
console.log(output);
