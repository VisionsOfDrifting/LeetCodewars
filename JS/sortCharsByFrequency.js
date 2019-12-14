'use strict';

function sortByFrequentChars(str) {
  let frequencies = {};
  let index = {};

  let arr = str.split('');
  // Populate the maps
  for (let i = 0; i < arr.length; i++) {
    if (frequencies[arr[i]]) {
      frequencies[arr[i]] = frequencies[arr[i]] + 1;
    } else {
      frequencies[arr[i]] = 1;
      index[i] = arr[i];
    }
  }

  console.log(frequencies);
  console.log(index);

  let chars = {};
  for (let key of Object.keys(frequencies)) {
    if (chars[frequencies[key]]) {
      chars[frequencies[key]].push(key);
    } else {
      chars[frequencies[key]] = [key]; ``
    }
  }

  console.log(chars);

  let retArr = [];
  // for (let key of Object.keys(index)) {
  //   if (retArr.length >= str.length) {
  //     break;
  //   }
  //   for (let ch of chars[frequencies[index[key]]]) {
  //     if (retArr.indexOf(ch) !== -1) {
  //       break;
  //     }
  //     for (let i = 0; i < frequencies[ch]; ++i) {
  //       // console.log(retArr);
  //       retArr.push(ch);
  //     }
  //   }
  // }

  // Note you might need some of the above logic if the keys
  // of chars didn't appear in numerical order. I.E. if this
  // was in python the code probably would be very different.
  for (let key of Object.keys(chars)) {
    let currentInt = parseInt(key, 10);
    for (let ch of chars[currentInt]) {
      for (let i = 0; i < currentInt; i++) {
        retArr.push(ch);
      }
    }
  }

  console.log(retArr);
  return retArr.reverse().join('');
}


const input = 'halalelluejah';
// const input = 'tweet';
const output = sortByFrequentChars(input);
console.log(output);
