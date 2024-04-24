var lengthOfLongestSubstring = function(s) {
  let maxSubStringLength = 0;

  for (let i = 0; i < s.length; i++) {
      let subString = ''
      for (let j = i; j < s.length; j++) {
        if (!subString.includes(s[j])) {
            subString += s[j]
            // maxSubStringLength = max(maxSubStringLength, subString.length)
            if (subString.length > maxSubStringLength) {
                maxSubStringLength = subString.length
            }
            // console.log(subString, maxSubStringLength)
        } else {
            subString = ''
        }
      }
  }

  return maxSubStringLength  
};

console.log(lengthOfLongestSubstring(' '))
// console.log(lengthOfLongestSubstring('abca'))