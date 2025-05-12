#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    std::vector<int> findEvenNumbers(std::vector<int>& digits) {
        // Count frequency of each digit
        int freq[10] = {0};
        for (int d : digits) {
            freq[d]++;
        }
        
        std::unordered_set<int> result;
        
        // Iterate over all possible hundreds, tens, and units digits
        for (int hundred = 1; hundred <= 9; hundred++) { // No leading zero
            if (freq[hundred] == 0) continue;
            for (int ten = 0; ten <= 9; ten++) {
                if (freq[ten] == 0) continue;
                for (int unit = 0; unit <= 8; unit += 2) { // Even digits: 0, 2, 4, 6, 8
                    if (freq[unit] == 0) continue;
                    // Check if we have enough digits
                    int need_h = (hundred == ten) + (hundred == unit) + 1;
                    int need_t = (ten == hundred) + (ten == unit) + 1;
                    int need_u = (unit == hundred) + (unit == ten) + 1;
                    if (need_h <= freq[hundred] && need_t <= freq[ten] && need_u <= freq[unit]) {
                        int num = hundred * 100 + ten * 10 + unit;
                        result.insert(num);
                    }
                }
            }
        }
        
        // Convert set to sorted vector
        std::vector<int> ans(result.begin(), result.end());
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};