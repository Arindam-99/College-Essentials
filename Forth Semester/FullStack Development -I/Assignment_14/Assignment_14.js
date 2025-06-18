//a)	Create a Node.js project using Express that:
//b)	Responds with both HTML and JSON.
//c)	Serves different HTML files at different routes

const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Home Route (Serves an HTML file)
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// About Route (Serves another HTML file)
app.get('/about', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'about.html'));
});

// JSON Response Route
app.get('/api/data', (req, res) => {
    res.json({
        message: "Hello, this is a JSON response!",
        status: "success",
        data: {
            name: "Express App",
            version: "1.0.0"
        }
    });
});

// Start the Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
