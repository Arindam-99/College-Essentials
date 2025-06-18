//a)Write a Node.js program to describe local modules with two functions.
//b)Write a Node.js program to describe local modules with an object.

// Importing local module (mathOperations.js)
const mathOperations = require('./mathOperations');
console.log("Addition:", mathOperations.add(5, 3));
console.log("Multiplication:", mathOperations.multiply(4, 2));

console.log("\n--------------------------------------\n");

// Importing local module (userInfo.js)
const userInfo = require('./userInfo');
console.log(userInfo.greet());

// mathOperations.js
const mathOperations = {
    add: (a, b) => a + b,
    multiply: (a, b) => a * b
};
module.exports = mathOperations;

// userInfo.js
const userInfo = {
    name: "John Doe",
    age: 30,
    greet: function () {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
};
module.exports = userInfo;
