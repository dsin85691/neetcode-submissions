class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int min_size = min(word1.length(), word2.length()); // length() --> is the way to get C++ length value
        string new_str = ""; 
        for (int i = 0; i < min_size; i++) { 
            new_str += word1[i]; 
            new_str += word2[i]; 
        }
        if (word1.length() > min_size) new_str += word1.substr(min_size);
        if (word2.length() > min_size) new_str += word2.substr(min_size); // substr() --> gets you the substr starting at min_size
        return new_str;
    }
};