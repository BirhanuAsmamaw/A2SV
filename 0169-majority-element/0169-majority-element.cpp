#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
            if (counts[num] > nums.size() / 2) {
                return num;
            }
        }
        return -1;
    }
};
