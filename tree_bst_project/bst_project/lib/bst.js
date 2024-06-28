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
    


}

module.exports = {
    TreeNode,
    BST
};