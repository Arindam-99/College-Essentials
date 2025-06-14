const http = require('http');

const server = http.createServer((req, res) => {
    const { method, url } = req;

    res.setHeader('Content-Type', 'application/json');

    if (url === '/') {
        res.writeHead(200);
        res.end(JSON.stringify({ message: 'Welcome to the Home Page' }));
    } else if (url === '/about') {
        res.writeHead(200);
        res.end(JSON.stringify({ message: 'About Us Page' }));
    } else if (url === '/data') {
        if (method === 'GET') {
            res.writeHead(200);
            res.end(JSON.stringify({ message: 'Fetching Data' }));
        } else if (method === 'POST') {
            res.writeHead(201);
            res.end(JSON.stringify({ message: 'Data Created' }));
        } else if (method === 'PUT') {
            res.writeHead(200);
            res.end(JSON.stringify({ message: 'Data Updated' }));
        } else if (method === 'DELETE') {
            res.writeHead(200);
            res.end(JSON.stringify({ message: 'Data Deleted' }));
        } else {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method Not Allowed' }));
        }
    } else {
        res.writeHead(404);
        res.end(JSON.stringify({ error: 'Page Not Found' }));
    }
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
