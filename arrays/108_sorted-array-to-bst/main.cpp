#include <ios>
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    if (nums.empty())
      return nullptr;

    int mid = nums.size() / 2;
    TreeNode *root = new TreeNode(nums[mid]);

    if (mid > 0) {
      vector<int> leftSub(nums.begin(), nums.begin() + mid);
      root->left = sortedArrayToBST(leftSub);
    }

    if (mid + 1 < nums.size()) {
      vector<int> rightSub(nums.begin() + mid + 1, nums.end());
      root->right = sortedArrayToBST(rightSub);
    }
    return root;
  }
};

void inorder(TreeNode *root) {
  if (!root)
    return;
  inorder(root->left);
  cout << root->val << " ";
  inorder(root->right);
}

void deleteBST(TreeNode *root) {
  if (!root)
    return;

  deleteBST(root->left);
  deleteBST(root->right);

  delete root;
}

int main() {
  vector<int> nums = {1, 2, 0, 3, 4};
  TreeNode *root = Solution().sortedArrayToBST(nums);
  inorder(root);
  deleteBST(root);
  return 0;
}
