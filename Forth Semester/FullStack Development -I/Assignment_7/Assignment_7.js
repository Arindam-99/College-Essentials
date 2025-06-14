// a) Node.js program to describe the core 'path' module
const path = require('path');

console.log("Path Module Examples:");
console.log("Directory Name:", path.dirname(__filename));
console.log("Base Name:", path.basename(__filename));
console.log("File Extension:", path.extname(__filename));
console.log("Join Paths:", path.join(__dirname, 'test', 'file.txt'));
console.log("Resolve Path:", path.resolve('test', 'file.txt'));

console.log("\n--------------------------------------\n");
// Output: 
// Path Module Examples:
// Directory Name: C:\Users\ARINDAM  DAS\OneDrive\Desktop\Node Js of college\Assignment_7
// Base Name: Assignment_7.js
// File Extension: .js
// Join Paths: C:\Users\ARINDAM  DAS\OneDrive\Desktop\Node Js of college\Assignment_7\test\file.txt
// Resolve Path: C:\Users\ARINDAM  DAS\OneDrive\Desktop\Node Js of college\Assignment_7\test\file.txt

// b) Node.js program to describe the core modules 'path' and 'fs'
const fs = require('fs');

console.log("File System (fs) Module Examples:");
const filePath = path.join(__dirname, 'example.txt');

// Writing to a file
fs.writeFileSync(filePath, 'Hello, this is a test file!');
console.log("File written successfully.");

// Reading from a file
const data = fs.readFileSync(filePath, 'utf8');
console.log("File content:", data);

// Checking if a file exists
if (fs.existsSync(filePath)) {
    console.log("File exists.");
}

// Deleting a file
fs.unlinkSync(filePath);
console.log("File deleted successfully.");
//Output
//--------------------------------------

// File System (fs) Module Examples:
// File written successfully.
// File content: Hello, this is a test file!
// File exists.
// File deleted successfully.