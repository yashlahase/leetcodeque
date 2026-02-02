class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        int need = k - 1;

        multiset<int> small, large;
        long long smallSum = 0;
        long long ans = LLONG_MAX;

        int left = 1;

        for (int right = 1; right < n; right++) {
            small.insert(nums[right]);
            smallSum += nums[right];

            if ((int)small.size() > need) {
                auto it = prev(small.end());
                large.insert(*it);
                smallSum -= *it;
                small.erase(it);
            }

            if (right - left > dist) {
                if (small.find(nums[left]) != small.end()) {
                    smallSum -= nums[left];
                    small.erase(small.find(nums[left]));
                } else {
                    large.erase(large.find(nums[left]));
                }
                left++;
            }

            while ((int)small.size() < need && !large.empty()) {
                auto it = large.begin();
                small.insert(*it);
                smallSum += *it;
                large.erase(it);
            }

            if ((int)small.size() == need) {
                ans = min(ans, smallSum);
            }
        }

        return nums[0] + ans;
    }
};
