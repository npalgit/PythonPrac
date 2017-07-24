__source__ = 'https://leetcode.com/problems/flip-game-ii/tabs/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flip-game-ii.py
# Time:  O(n + c^2)
# Space: O(c)
# You are playing the following Flip Game with your friend: Given a string
# that contains only these two characters: + and -,
# you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# For example, given s = "++++", return true.
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#
# Follow up:
# Derive your algorithm's runtime complexity.
# Companies
# Google
# Related Topics
# Backtracking
# Similar Questions
# Nim Game Flip Game Guess Number Higher or Lower II Can I Win
# '''

# Time:  O(n + c^2)
# Space: O(c)

# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/discuss/64344/theory-matters-from-backtracking-128ms-to-dp-0m

# The imap() function returns an iterator that calls a function on the values in the input iterators, and returns the results.
# It works like the built-in map(), except that it stops when any input iterator is exhausted
# (instead of inserting None values to completely consume all of the inputs).

# izip() returns an iterator that combines the elements of several iterators into tuples.
# It works like the built-in function zip(), except that it returns an iterator instead of a list.
import itertools
import re
class Solution(object):
    def canWin(self, s):
        g, g_final = [0], 0
        for p in itertools.imap(len, re.split('-+', s)):
            while len(g) <= p:
                # Theorem 2: g[game] = g[subgame1]^g[subgame2]^g[subgame3]...;
                # and find first missing number.
                g += min(set(xrange(p)) - {x^y for x, y in itertools.izip(g[:len(g)/2], g[-2:-len(g)/2-2:-1])}),
            g_final ^= g[p]
        return g_final > 0  # Theorem 1: First player must win iff g(current_state) != 0


# Time:  O(n + c^3 * 2^c * logc), n is length of string, c is count of "++"
# Space: O(c * 2^c)
# hash solution.
# We have total O(2^c) game strings,
# and each hash key in hash table would cost O(c),
# each one has O(c) choices to the next one,
# and each one would cost O(clogc) to sort,
# so we get O((c * 2^c) * (c * clogc)) = O(c^3 * 2^c * logc) time.
# To cache the results of all combinations, thus O(c * 2^c) space.
class Solution2(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}

        def canWinHelper(consecutives):                                         # O(2^c) time
            consecutives = tuple(sorted(c for c in consecutives if c >= 2))     # O(clogc) time
            if consecutives not in lookup:
                lookup[consecutives] = any(not canWinHelper(consecutives[:i] + (j, c-2-j) + consecutives[i+1:])  # O(c) time
                                           for i, c in enumerate(consecutives)  # O(c) time
                                           for j in xrange(c - 1))              # O(c) time
            return lookup[consecutives]                                         # O(c) time

        # re.findall: O(n) time, canWinHelper: O(c) in depth
        return canWinHelper(map(len, re.findall(r'\+\++', s)))

# Time:  O(c * n * c!), n is length of string, c is count of "++"
# Space: O(c * n), recursion would be called at most c in depth.
#                  Besides, it costs n space for modifying string at each depth.
class Solution3(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        is_win = False
        while not is_win and i < n:                                     # O(n) time
            if s[i] == '+':
                while not is_win and i < n and s[i+1] == '+':           # O(c) time
                     # t(n, c) = c * (t(n, c-1) + n) + n = ...
                     # = c! * t(n, 0) + n * c! * (c + 1) * (1/0! + 1/1! + ... 1/c!)
                     # = n * c! + n * c! * (c + 1) * O(e) = O(c * n * c!)
                    is_win = not self.canWin(s[:i] + '--' + s[i+2:])    # O(n) space
                    i += 1
            i += 1
        return is_win


# Java:
# http://buttercola.blogspot.com/2015/10/leetcode-flip-game-ii.html
Java='''
#60.16%
public class Solution {
    public boolean canWin(String s) {
        if(s == null || s.length() == 0 ) return false;
        char[] arr = s.toCharArray();
        return dfs(arr);
    }

    private boolean dfs(char[] arr){
        for(int i= 1 ; i < arr.length; i++){
            if(arr[i-1] == '+' && arr[i] == '+'){
                arr[i-1] = '-';
                arr[i] = '-';

                boolean win = !dfs(arr);

                arr[i-1] = '+';
                arr[i] = '+';

                if(win) return true;
            }
        }
        return false;

    }
}

# backtracking + memorization 68%
public class Solution {
    public boolean canWin(String s) {
        return canWin(s, new HashMap<>());
    }

    public boolean canWin(String s, Map<String, Boolean> cache) {
        if (cache.containsKey(s)) {
            return cache.get(s);
        }
        int index = -1;
        while ((index = s.indexOf("++", index + 1)) >= 0) {
            String next = new StringBuilder().append(s.substring(0, index)).append("--").append(s.substring(index + 2)).toString();
            if (!canWin(next, cache)) {
                cache.put(s, true);
                return true;
            }
        }
        cache.put(s, false);
        return false;
    }
}

# 76%
public class Solution {
    HashMap<String, Boolean> map = new HashMap<>();

    public boolean canWin(String s) {
        if(map.containsKey(s))  return map.get(s);

        for (int start = 0; start < s.length();) {
            int index = s.indexOf("++", start);
            if (index < 0) break;
            String newS = s.substring(0, index) + "--" + s.substring(index + 2);
            if (!canWin(newS)) {
                map.put(s, true);
                return true;
            }
            start = index + 1;
        }
        map.put(s, false);
        return false;
    }
}
'''