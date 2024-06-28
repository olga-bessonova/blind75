function depthFirstSearch(root, targetVal) {
    if (!root){
        return null
    }

    if (root.val === targetVal){
        return root
    }

    if (root.left) {
        let leftRes = depthFirstSearch(root.left, targetVal)
        if (leftRes) {
            return leftRes
        }
    }

    if (root.right) {
        let rightRes = depthFirstSearch(root.right, targetVal)
        if (rightRes) {
            return rightRes
        }
    }

    return null;

}


module.exports = {
    depthFirstSearch
};