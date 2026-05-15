#include <unordered_map>
using namespace std; 

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; // hash map 
        for (int num : nums) { // iterating through each element of nums
            if (seen.count(num)) { // Check if we have seen number 
                return true; // if we did return true
            }
            seen.insert(num); // if not continue adding to the set
        }
        return false; // return false

    }
};