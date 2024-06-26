// View the full problem and run the test cases at:
//  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

const { TreeNode } = require('./tree_node.js');


function buildTree(preorder, inorder) {
  if (inorder.length){
    let index = inorder.indexOf(preorder.shift());
    const root = new TreeNode(inorder[index])
    root.left = buildTree(preorder, inorder.slice(0, index));
    root.right = buildTree(preorder, inorder.slice(index+1));

    return root;
  }
  return null;

}
