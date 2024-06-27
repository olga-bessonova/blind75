function breadthFirstArray(root) {
    // Queue FIFO
    const queue = [root] 
    const res = []

    while (queue.length){
        const currNode = queue.shift()
        res.push(currNode.val)
        if (currNode.left) {
            queue.push(currNode.left)
        }

        if (currNode.right) {
            queue.push(currNode.right)
        }
    }
    return res
}

module.exports = {
    breadthFirstArray
};