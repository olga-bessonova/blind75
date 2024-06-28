const { breadthFirstArray } = require('./breadth_first_array');

function treeSum(root) {
    if (!root){
        return 0
    }
    const bfs = breadthFirstArray(root)

    const sum = bfs.reduce((accumulator, currentValue) => {
        return accumulator + currentValue;
    }, 0);
    return sum
}


module.exports = {
    treeSum
};