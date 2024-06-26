function inOrderArray(root) {
    if (!root){
        return []
    }

    // Recursively get the in-order traversal of the left subtree
    let leftArray = inOrderArray(root.left);

    // Recursively get the in-order traversal of the right subtree
    let rightArray = inOrderArray(root.right);

    // Combine the arrays: left subtree + root + right subtree
    return [...leftArray, root.val, ...rightArray];

}

function postOrderArray(root) {
    if (!root){
        return []
    }

    // Recursively get the in-order traversal of the left subtree
    let leftArray = postOrderArray(root.left);

    // Recursively get the in-order traversal of the right subtree
    let rightArray = postOrderArray(root.right);

    // Combine the arrays: left subtree + root + right subtree
    return [...leftArray, ...rightArray, root.val];

}


module.exports = {
    inOrderArray,
    postOrderArray
};