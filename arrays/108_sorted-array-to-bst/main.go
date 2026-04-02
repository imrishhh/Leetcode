package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	mid := len(nums) / 2
	root := &TreeNode{
		Val:   nums[mid],
		Left:  nil,
		Right: nil,
	}

	if mid > 0 {
		leftSub := nums[0:mid]
		root.Left = sortedArrayToBST(leftSub)
	}

	if mid+1 < len(nums) {
		rightSub := nums[mid+1:]
		root.Right = sortedArrayToBST(rightSub)
	}
	return root
}

func inorder(root *TreeNode) {
	if root == nil {
		return
	}
	inorder(root.Left)
	fmt.Print(root.Val, " ")
	inorder(root.Right)
}

func main() {
	nums := []int{2, 3, 0, 4, 5}
	root := sortedArrayToBST(nums)
	inorder(root)
}
