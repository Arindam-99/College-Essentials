//Write a Node.js script for the REPL environment, including functions, array methods, and asynchronous operations.
// Define a sample array
const numbers = [1, 2, 3, 4, 5];

// Function to double each number in the array
function doubleNumbers(arr) {
    return arr.map(num => num * 2);
}

// Function to filter even numbers
function filterEvenNumbers(arr) {
    return arr.filter(num => num % 2 === 0);
}

// Function to sum all numbers in the array
function sumNumbers(arr) {
    return arr.reduce((acc, num) => acc + num, 0);
}

// Asynchronous function that simulates fetching data
async function fetchData() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Data fetched successfully!");
        }, 2000);
    });
}

// Export functions for REPL usage
module.exports = {
    numbers,
    doubleNumbers,
    filterEvenNumbers,
    sumNumbers,
    fetchData
};

// Instructions for REPL usage
console.log("Node.js REPL Script Loaded. Try these commands:");
console.log("doubleNumbers(numbers)");
console.log("filterEvenNumbers(numbers)");
console.log("sumNumbers(numbers)");
console.log("await fetchData()");

//-----OutPut------
//Node.js REPL Script Loaded. Try these commands:
// doubleNumbers(numbers)
// filterEvenNumbers(numbers)
// sumNumbers(numbers)
// await fetchData()