__source__ = 'https://leetcode.com/problems/word-pattern/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-pattern.py
# Time:  O(n)
# Space: O(c), c is unique count of pattern

# Given a pattern and a string str, find if str follows the same pattern.
#
# Examples:
#   1. pattern = "abba", str = "dog cat cat dog" should return true.
#   2. pattern = "abba", str = "dog cat cat fish" should return false.
#   3. pattern = "aaaa", str = "dog cat cat dog" should return false.
#   4. pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
#   1. Both pattern and str contains only lowercase alphabetical letters.
#   2. Both pattern and str do not have leading or trailing spaces.
#   3. Each word in str is separated by a single space.
#   4. Each letter in pattern must map to a word with length that is at least 1.
# Companies
# Dropbox Uber Tesla
# Related Topics
# Hash Table
# Similar Questions
# Isomorphic Strings Word Pattern II
#
from itertools import izip  # Generator version of zip.
import unittest
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != self.wordCounts(str):
            return False

        w2p, p2w = {}, {}

        for p, w in izip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                # Contradict mapping.
                return False
        return True


    def wordCounts(self, str):
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt

     # Generate a word at a time without saving all the words.
    def wordGenerator(self, str):
        w = ""
        for c in str:
            if c == ' ':
                yield w
                w = ""
            else:
                w += c
        yield w


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split() #Space O(n)
        if len(pattern) != len(words):
            return False

        w2p, p2w = {}, {}
        for p, w in izip(pattern, words):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                 # Contradict mapping.
                return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#95.84% 1ms
public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] strs = str.split(" ");
        if (pattern.length() != strs.length) {
            return false;
        }
        String[] mapping = new String[26];
        Set<String> set = new HashSet<>();
        for (int i = 0; i < pattern.length(); i++) {
            int index = pattern.charAt(i) - 'a';
            if (mapping[index] == null) {
                if (set.contains(strs[i])) {
                    return false;
                }
                mapping[index] = strs[i];
                set.add(strs[i]);
            } else {
                if (!mapping[index].equals(strs[i])) {
                    return false;
                }
            }
        }
        return true;
    }
}

#30.28%  2ms
public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] arr= str.split(" ");
        HashMap<Character, String> map = new HashMap<Character, String>();
        if(arr.length!= pattern.length())
            return false;
        for(int i=0; i<arr.length; i++){
            char c = pattern.charAt(i);
            if(map.containsKey(c)){
                if(!map.get(c).equals(arr[i]))
                    return false;
            }else{
                if(map.containsValue(arr[i]))
                    return false;
                map.put(c, arr[i]);
            }
        }
        return true;
    }
}

'''