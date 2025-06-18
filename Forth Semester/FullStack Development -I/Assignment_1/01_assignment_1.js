//1	Create a Node.js script demonstrating variables, functions, conditionals, loops, objects, arrays, and asynchronous code.

// Define variables
const greeting = "Hello, Node.js!";
let counter = 0;

// Function to display a message
function showMessage(message) {
    console.log(message);
}

// Object representing a user
const user = {
    name: "John Doe",
    age: 30,
    isAdmin: true,
    greet: function () {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
};

// Array of numbers
const numbers = [10, 20, 30, 40, 50];

// Loop through the array
for (let i = 0; i < numbers.length; i++) {
    console.log(`Number at index ${i}: ${numbers[i]}`);
}

// Using conditionals
if (user.isAdmin) {
    console.log(`${user.name} has admin privileges.`);
} else {
    console.log(`${user.name} is a regular user.`);
}

// Asynchronous function using Promises
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = "Sample data from database";
            resolve(data);
        }, 2000);
    });
}

// Using async/await to handle asynchronous code
async function getData() {
    console.log("Fetching data...");
    try {
        const data = await fetchData();
        console.log("Received data:", data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Execute functions
showMessage(greeting);
user.greet();
getData();

/* OUTPUT 
Number at index 0: 10
Number at index 1: 20
Number at index 2: 30
Number at index 3: 40
Number at index 4: 50
John Doe has admin privileges.
Hello, Node.js!
Hello, my name is John Doe and I am 30 years old.
Fetching data...
Received data: Sample data from database
 */