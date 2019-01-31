/* eslint-disable no-plusplus */
/*
This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of
all occurrences of the pattern in the string.

For example, given the string "abracadabra" and
the pattern "abr", you should return [0, 7].
*/
/*
I will assume that this is an algorithm that only takes
strings as argument and that the strings are not null.

This function returns an array of indicies where the
substring begins within the search string.
If no instances of the substring are found
an empty array is returned.
*/

function indexOfSubString(searchString, subString) {
  const firstLetter = subString.charAt(0);
  const subStringLen = subString.length;
  const indexOfMatch = [];
  let possibleSubstring = false;
  let possibleIndex = -1;

  if (
    typeof searchString !== 'string'
    || typeof subString !== 'string'
    || searchString === ''
    || subString === ''
  ) {
    console.log('Please provide non-empty strings for both arguments');
    return [];
  }

  for (let i = 0, j = 0; i < searchString.length; ++i) {
    console.log(searchString.charAt(i), subString.charAt(j), j);
    if (possibleSubstring && searchString.charAt(i) === subString.charAt(j)) {
      console.log('Found another letter in the subString');
      if (++j === subStringLen) {
        console.log('Found the last letter in the subString');
        indexOfMatch.push(possibleIndex);
        [possibleIndex, j, possibleSubstring] = [-1, 0, false];
      }
    } else if (!possibleSubstring && searchString.charAt(i) === firstLetter) {
      console.log('Found the first letter');
      [possibleSubstring, possibleIndex] = [true, i];
      ++j;
    } else if (searchString.charAt(i) !== subString.charAt(j)) {
      console.log("That wasn't a substring");
      [possibleIndex, j, possibleSubstring] = [-1, 0, false];
    }
    console.log(possibleIndex, possibleSubstring);
  }
  return indexOfMatch;
}

const string = 'Rikk-tikk-tikki-tikki-tchk';
// 'abracadabra';
const sub = 'tikk';
// 'abr';

console.log(indexOfSubString(string, sub));
