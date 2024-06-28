// const { }
function treeHeight(root) {
    if (!root){
        return -1
    }

    if (!root.left && !root.right){
        return 0
    }

    const queue = [root] 
    const res = []
    let edges = 0

    while (queue.length){
        const currNode = queue.shift()
        res.push(currNode.val)
        if (currNode.left || currNode.right) {
            edges += 1
        }
        if (currNode.left) {
            queue.push(currNode.left)
        }

        if (currNode.right) {
            queue.push(currNode.right)
        }
    }
    return edges



}


module.exports = {
    treeHeight
};