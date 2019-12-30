/*Problem:
  Given a String of length S, reverse the whole string without reversing
  the individual words in it. Words are separated by dots.

  Approach:
  Find the indices of the delemiter in the string.
  Iterate over the words coresponding to the indicies and generate a
  newBegining and newEnding string.
  Concatenate the newBegning and newEnding and return
  Time O(s), Space O(s)

  Optimizations:
  You could do this without finding the indices first. You would have to 
  generate the two strings at the same time you are searching for the indices.

  I'm sure there is a way to do the reversal in place, but I am not sure how.
*/

function reverseWords(s = '', delimeter = '.') {
  const indicesOfDelimeter = [];
  // Find the indicies of the delimeter: Time O(s)
  for (let i = 0; i < s.length; ++i) {
    const c = s[i];
    if (c === delimeter) {
      indicesOfDelimeter.push(i);
    }
  }
  // console.log(s.length);
  console.log(indicesOfDelimeter);

  // Auxilary variables to generate the new string: Memory O(s)
  let newBegining = '', newEnding = '';

  // Generate the new string by walking over the indices: Time O(s/2)
  // You could do this in O(s) instead if you wanted to, the code would be simpler
  for (let i = indicesOfDelimeter.length - 1, j = 0; i >= 0; --i, ++j) {
    if (j > indicesOfDelimeter.length / 2) {
      break;
    }
    const start1 = indicesOfDelimeter[j - 1] ? indicesOfDelimeter[j - 1] + 1 : 0;
    const end2 = indicesOfDelimeter[i + 1] ? indicesOfDelimeter[i + 1] : s.length;

    // If the string is an odd length we want to skip concatanating the same last word to the newEnding
    if (j !== indicesOfDelimeter.length / 2) {
      const word1 = s.slice(start1, indicesOfDelimeter[j]);
      newEnding = '.' + word1 + newEnding;
    }

    const word2 = s.slice(indicesOfDelimeter[i] + 1, end2);
    newBegining = newBegining + word2 + '.';

    // console.log(i, j);
    // console.log(start1, indicesOfDelimeter[j]);
    // console.log(word1);
    // console.log(indicesOfDelimeter[i], end2);
    // console.log(word2);
    // console.log(newEnding, newBegining);
  }

  return newBegining + newEnding.slice(1, newEnding.length);
}


input = "i.like.this.program.very.much"
console.log(input);
output = reverseWords(input)
console.log(output);
input = "i.like.this.program.much"
console.log(input);
output = reverseWords(input)
console.log(output);
