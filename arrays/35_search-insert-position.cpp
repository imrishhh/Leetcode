#include <iostream>
#include <vector>

using namespace std;

/*
 * Logic for this algorithm.
 * Constraint is we must do it in time complexity O(log n)
 * For this we must use binary search and for that array must be sorted.
 * So, we assume vector is always sorted here.
 * For binary search:
 * Initialize low = 0 and high = size of vector - 1;
 * While low <= high:
 *  mid = low + (high - low) / 2; We start from middle.
 *  if (nums[mid] == target) // If mid is the target then we simply return mid;
 *    return mid;
 *
 * If we found we returned mid (position) else we check,
 * if (nums[mid] < target):
 *  low = mid + 1; if target is greater then we know our target is bigger than
 * middle value so we discard everything below mid. else high = mid - 1; else we
 * discard everything above mid index and set it as next high.
 * at the end if nothing found we return low which will be the position where
 * the target element can go in if exists.
 * */

class Solution {
public:
  int searchInsert(vector<int> &nums, int target) {
    int low = 0, high = nums.size() - 1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (nums[mid] == target) {
        return mid;
      }

      if (nums[mid] < target) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return low;
  }
};

int main() {
  vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int target = 8;
  int pos = Solution().searchInsert(nums, target);
  cout << "Position of " << target << " is " << pos << endl;
  return 0;
}
