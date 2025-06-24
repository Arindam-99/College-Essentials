const http = require('http'); // <-- required module

const server = http.createServer((req, res) => {
    // Serve HTML UI for GET /
    if (req.url === '/' && req.method === 'GET') {
        res.setHeader('Content-Type', 'text/html');
        res.end(`
            <h2>Test API Calls</h2>
            <form action="/data" method="post">
                <button type="submit">Send POST</button>
            </form>
            <form onsubmit="event.preventDefault(); fetch('/data', { method: 'PUT' }).then(res => res.text()).then(alert);">
                <button type="submit">Send PUT</button>
            </form>
            <form onsubmit="event.preventDefault(); fetch('/data', { method: 'DELETE' }).then(res => res.text()).then(alert);">
                <button type="submit">Send DELETE</button>
            </form>
        `);
    }

    // Handle POST
    else if (req.url === '/data' && req.method === 'POST') {
        res.setHeader('Content-Type', 'text/plain');
        res.end('POST : Data Received.');
    }

    // Handle PUT
    else if (req.url === '/data' && req.method === 'PUT') {
        res.setHeader('Content-Type', 'text/plain');
        res.end('PUT : Data Updated');
    }

    // Handle DELETE
    else if (req.url === '/data' && req.method === 'DELETE') {
        res.setHeader('Content-Type', 'text/plain');
        res.end('DELETE : Data Deleted');
    }

    // 404 for others
    else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('404 : Not Found');
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
