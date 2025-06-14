const fs = require('fs');

console.log("1. Start of the program");

// Synchronous function example
function synchronousExample() {
    console.log("2. Synchronous function start");
    let sum = 0;
    for (let i = 0; i < 1e6; i++) {
        sum += i;
    }
    console.log("3. Synchronous function end, Sum:", sum);
}

synchronousExample();

// Asynchronous function example
function asynchronousExample() {
    console.log("4. Asynchronous function start");
    setTimeout(() => {
        console.log("6. Inside setTimeout (Asynchronous)");
    }, 1000);
    console.log("5. Asynchronous function end");
}

asynchronousExample();

console.log("7. End of the program");

//Output
//1. Start of the program
// 2. Synchronous function start
// 3. Synchronous function end, Sum: 499999500000
// 4. Asynchronous function start
// 5. Asynchronous function end
// 7. End of the program
// 6. Inside setTimeout (Asynchronous)