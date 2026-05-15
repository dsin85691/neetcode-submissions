class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_counts; // unordered map of s counts
        unordered_map<char, int> t_counts; // unordered map of t counts

        // build frequency maps
        for (int i = 0; i < s.size(); i++) {
            s_counts[s[i]]++;
            t_counts[t[i]]++;
        }

        // compare counts
        for (const auto& pair : s_counts) {
            char key = pair.first;

            if (s_counts[key] != t_counts[key]) {
                return false;
            }
        }

        return true;
    }
};