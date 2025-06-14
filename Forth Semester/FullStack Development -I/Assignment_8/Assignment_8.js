// Node.js program demonstrating the use of Buffers

// Creating buffers using Buffer.from() and Buffer.alloc()
const bufferFrom = Buffer.from('Hello, Buffer!');
console.log("Buffer from string:", bufferFrom);
console.log("Buffer as string:", bufferFrom.toString());

const bufferAlloc = Buffer.alloc(10); // Allocating 10 bytes
console.log("Allocated Buffer:", bufferAlloc);

// Writing data into buffer
bufferAlloc.write("Node.js", "utf-8");
console.log("Buffer after writing:", bufferAlloc.toString());

// Slicing a buffer
const slicedBuffer = bufferFrom.slice(7, 13);
console.log("Sliced Buffer:", slicedBuffer.toString());

//Output
//Buffer from string: <Buffer 48 65 6c 6c 6f 2c 20 42 75 66 66 65 72 21>
// Buffer as string: Hello, Buffer!
// Allocated Buffer: <Buffer 00 00 00 00 00 00 00 00 00 00>
// Buffer after writing: Node.js
// Sliced Buffer: Buffer