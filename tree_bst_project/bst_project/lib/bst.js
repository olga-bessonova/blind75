class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}


class BST {
    constructor(){
        this.root = null
    }
    
    insert(val){
        const newNode = new TreeNode(val)
        if (this.root === null){
            this.root = newNode;
            return;
        }

        let current = this.root;
        while (true) {
            if (val < current.val){
                if (!current.left){
                    current.left =  newNode
                    return;
                }
                current = current.left
            } else {
                if (!current.right){
                    current.right =  newNode
                    return;
                }
                current = current.right
            }
        }
    }

    searchRecur(val, node = this.root) {
        if (node === null) {
            return false;
        }
        if (node.val === val) {
            return true;
        } else if (val < node.val) {
            return this.searchRecur(val, node.left);
        } else {
            return this.searchRecur(val, node.right);
        }
    }

    searchRecur(val, node = this.root) {
        // Base case: if node is null, value is not found
        if (!node) return false;
        // Base case: if node's value equals search value, return true
        if (node.val === val) return true;
        // Recursive case: search left or right subtree based on value comparison
        if (val < node.val) {
            return this.searchRecur(val, node.left);
        } else {
            return this.searchRecur(val, node.right);
        }
    }

    searchIter(val) {
        let current = this.root;
        while (current) {
            if (val === current.val) {
                return true;
            } else if (val < current.val) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return false;
    }   


}

module.exports = {
    TreeNode,
    BST
};