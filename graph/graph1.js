class GraphNode {
  constructor(val) {
    this.val = val;
    this.neighbours = [];
  }
}

let a = new GraphNode('a');
let b = new GraphNode('b');
let c = new GraphNode('c');
let d = new GraphNode('d');
let e = new GraphNode('e');
let f = new GraphNode('f');
a.neighbours = [e, c, b];
c.neighbours = [b, d];
e.neighbours = [a];
f.neighbours = [e];