let obj = {a: 'foo', b: 'bar'};
const obj2 = {z: 'baz'};

obj = obj2; // const will prevent this operation. 
console.log(obj)

// const obj = {a: 'foo', b: 'bar'};
// const obj2 = {z: 'baz'};

// obj = obj2; // const will prevent this operation. 