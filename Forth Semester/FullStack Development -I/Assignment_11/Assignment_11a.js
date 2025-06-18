//a)	Write a Node.js program to create a server using the http core module.
// server.js

const http = require('http');

// Create the server
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello, this is a basic Node.js server!');
});

// Listen on port 3000
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

