#include <iostream>
#include <vector>

using namespace std;

/*
 * Logic of this algorithm.
 * The logic is straight forward as 26_remove-duplicate.cpp
 * We get an array of numbers.
 * Initialize k as the counter for numbers which are not equal
 * to val we are removing.
 * Run loop from 0 to end of the element this time.
 * if (nums[i] != val) {
 *  set nums[k] = nums[i];
 *  increase k by 1;
 * }
 * return k;
 * */

class Solution {
public:
  int removeElement(vector<int> &nums, int val) {
    int k = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] != val) {
        nums[k++] = nums[i];
      }
    }
    return k;
  }
};

int main() {
  vector<int> nums = {1, 2, 2, 3, 4, 5, 6};
  int val = 2;
  int k = Solution().removeElement(nums, val);
  cout << "Total elements " << k << endl;
  for (int i = 0; i < k; i++) {
    cout << nums[i] << endl;
  }
  return 0;
}
