3335. Total Characters in String After Transformations I
Problem Description
You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo (10^9 + 7).
Examples
Example 1:
Input: s = "abcyy", t = 2
Output: 7
Explanation:
- First Transformation (t = 1):
  - 'a' becomes 'b'
  - 'b' becomes 'c'
  - 'c' becomes 'd'
  - 'y' becomes 'z'
  - 'y' becomes 'z'
  - String: "bcdzz"
- Second Transformation (t = 2):
  - 'b' becomes 'c'
  - 'c' becomes 'd'
  - 'd' becomes 'e'
  - 'z' becomes "ab"
  - 'z' becomes "ab"
  - String: "cdeabab"
- Final Length: The string "cdeabab" has 7 characters.

Example 2:
Input: s = "azbk", t = 1
Output: 5
Explanation:
- First Transformation (t = 1):
  - 'a' becomes 'b'
  - 'z' becomes "ab"
  - 'b' becomes 'c'
  - 'k' becomes 'l'
  - String: "babcl"
- Final Length: The string "babcl" has 5 characters.

Constraints

(1 \leq s.length \leq 10^5)
s consists only of lowercase English letters.
(1 \leq t \leq 10^5)

Solution Approach
The problem requires computing the length of a string after t transformations, where each transformation shifts non-'z' characters to the next letter and replaces 'z' with "ab", doubling its contribution to the length. A naive approach of simulating each transformation is infeasible due to the large constraints ((s.length \leq 10^5), (t \leq 10^5)), as the string could grow exponentially.
Instead, a dynamic programming (DP) approach is used to track the frequency of each character after each transformation:

Initialize a DP Table:

Create a table f where f[i][j] represents the count of character j (0 = 'a', ..., 25 = 'z') after i transformations.
Set f[0][j] to the frequency of each character in s.


Update Frequencies:

For each transformation i (1 to t):
'z' (index 25) becomes "ab", contributing to 'a' (index 0) and 'b' (index 1):
f[i][0] = f[i-1][25]
f[i][1] = f[i-1][0] + f[i-1][25]


Other characters shift: f[i][j] = f[i-1][j-1] for j = 2 to 25.


Apply modulo (10^9 + 7) to prevent overflow.


Compute Final Length:

Sum f[t][j] for all j (0 to 25) to get the total length, modulo (10^9 + 7).



Time Complexity: (O(n + t \cdot 26)), where (n) is s.length() (for frequency counting) and (t \cdot 26) for DP updates.Space Complexity: (O(t \cdot 26)), for the DP table. (Can be optimized to (O(26)) using two arrays.)
This approach efficiently handles large inputs and correctly accounts for the extra characters introduced by 'z' transformations.
Solutions
Below are the solutions in Python3, Java, C++, Go, and TypeScript, all implementing the DP approach.
Python3
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        f = [[0] * 26 for _ in range(t + 1)]
        for c in s:
            f[0][ord(c) - ord("a")] += 1
        for i in range(1, t + 1):
            f[i][0] = f[i - 1][25]
            f[i][1] = (f[i - 1][0] + f[i - 1][25]) % (10**9 + 7)
            for j in range(2, 26):
                f[i][j] = f[i - 1][j - 1]
        return sum(f[t]) % (10**9 + 7)

Java
class Solution {
    public int lengthAfterTransformations(String s, int t) {
        final int mod = (int) 1e9 + 7;
        int[][] f = new int[t + 1][26];
        for (char c : s.toCharArray()) {
            f[0][c - 'a']++;
        }
        for (int i = 1; i <= t; ++i) {
            f[i][0] = f[i - 1][25] % mod;
            f[i][1] = (f[i - 1][0] + f[i - 1][25]) % mod;
            for (int j = 2; j < 26; j++) {
                f[i][j] = f[i - 1][j - 1] % mod;
            }
        }
        int ans = 0;
        for (int j = 0; j < 26; ++j) {
            ans = (ans + f[t][j]) % mod;
        }
        return ans;
    }
}

C++
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        const int mod = 1e9 + 7;
        vector<vector<int>> f(t + 1, vector<int>(26, 0));
        for (char c : s) {
            f[0][c - 'a']++;
        }
        for (int i = 1; i <= t; ++i) {
            f[i][0] = f[i - 1][25] % mod;
            f[i][1] = (f[i - 1][0] + f[i - 1][25]) % mod;
            for (int j = 2; j < 26; ++j) {
                f[i][j] = f[i - 1][j - 1] % mod;
            }
        }
        int ans = 0;
        for (int j = 0; j < 26; ++j) {
            ans = (ans + f[t][j]) % mod;
        }
        return ans;
    }
};

Go
func lengthAfterTransformations(s string, t int) int {
    const mod = 1_000_000_007
    f := make([][]int, t+1)
    for i := range f {
        f[i] = make([]int, 26)
    }
    for _, c := range s {
        f[0][c-'a']++
    }
    for i := 1; i <= t; i++ {
        f[i][0] = f[i-1][25] % mod
        f[i][1] = (f[i-1][0] + f[i-1][25]) % mod
        for j := 2; j < 26; j++ {
            f[i][j] = f[i-1][j-1] % mod
        }
    }
    ans := 0
    for j := 0; j < 26; j++ {
        ans = (ans + f[t][j]) % mod
    }
    return ans
}

TypeScript
function lengthAfterTransformations(s: string, t: number): number {
    const mod = 1_000_000_007;
    const f: number[][] = Array.from({ length: t + 1 }, () => Array(26).fill(0));
    for (const c of s) {
        f[0][c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    for (let i = 1; i <= t; i++) {
        f[i][0] = f[i - 1][25] % mod;
        f[i][1] = (f[i - 1][0] + f[i - 1][25]) % mod;
        for (let j = 2; j < 26; j++) {
            f[i][j] = f[i - 1][j - 1] % mod;
        }
    }
    let ans = 0;
    for (let j = 0; j < 26; j++) {
        ans = (ans + f[t][j]) % mod;
    }
    return ans;
}

Notes

Correctness: The DP approach ensures accurate tracking of character frequencies, handling the 'z' → "ab" rule by incrementing 'a' and 'b' counts. It’s robust for all edge cases, including large t, strings with many 'z's, or single-character strings.
Optimization: The space complexity can be reduced to (O(26)) by using two arrays (prev and curr) instead of a full t+1 row table, as each step depends only on the previous step. See the optimized Python3 solution below for an example.
Edge Cases:
Large t (up to (10^5)): The iterative DP handles this efficiently.
Strings with many 'z's: Correctly accounts for doubling effect.
Single character: Works for s = "a", t = 25 (becomes 'z', length 2 after next transformation).


Related Problems: This problem is similar to LeetCode 3337: Total Characters in String After Transformations II, which generalizes transformations using an array nums.

Optimized Python3 Solution (Space-Efficient)
For reference, here’s a space-optimized Python3 solution using (O(26)) space:
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for _ in range(t):
            next_freq = [0] * 26
            next_freq[0] = freq[25]
            next_freq[1] = (freq[0] + freq[25]) % mod
            for j in range(2, 26):
                next_freq[j] = freq[j - 1]
            freq = next_freq
        return sum(freq) % mod

References

LeetCode Problem: 3335. Total Characters in String After Transformations I
GitHub Solutions: doocs/leetcode
YouTube Explanation: codestorywithMIK

