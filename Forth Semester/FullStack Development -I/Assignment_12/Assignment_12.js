//12.Write a Node.js program to perform CRUD operations (Create, Read, Update, Delete) on a file using the fs core module.
const fs = require('fs');
const filePath = 'data.txt';

// Create or Write to a File
function createFile(content) {
    fs.writeFile(filePath, content, (err) => {
        if (err) {
            console.error('Error creating file:', err);
        } else {
            console.log('File created successfully');
        }
    });
}

// Read a File
function readFile() {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
        } else {
            console.log('File contents:', data);
        }
    });
}

// Update a File (Append Data)
function updateFile(newContent) {
    fs.appendFile(filePath, `\n${newContent}`, (err) => {
        if (err) {
            console.error('Error updating file:', err);
        } else {
            console.log('File updated successfully');
        }
    });
}

// Delete a File
function deleteFile() {
    fs.unlink(filePath, (err) => {
        if (err) {
            console.error('Error deleting file:', err);
        } else {
            console.log('File deleted successfully');
        }
    });
}

// Example Usage
createFile('Hello, this is a sample content.');
setTimeout(() => readFile(), 1000);
setTimeout(() => updateFile('This is new appended content.'), 2000);
setTimeout(() => readFile(), 3000);
setTimeout(() => deleteFile(), 4000);

//OutPUT
// File created successfully
// File contents: Hello, this is a sample content.
// File updated successfully
// File contents: Hello, this is a sample content.
// This is new appended content.
// File deleted successfully