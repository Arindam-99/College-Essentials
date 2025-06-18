//a)	Extend the Express project to:
// b)	 Serve different HTML files at different routes and perform a calculation (e.g., add two numbers from a user form).
// c)	Implement routing with dynamic parameters in the URL.
// d)	Use application-level middleware for tasks like logging or handling errors.

const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const PORT = 3000;

// Middleware for logging requests
app.use((req, res, next) => {
    const log = `${new Date().toISOString()} - ${req.method} ${req.url}\n`;
    fs.appendFile('server.log', log, (err) => {
        if (err) console.error('Logging error:', err);
    });
    console.log(log.trim());
    next();
});

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));

// Home Route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// About Route
app.get('/about', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'about.html'));
});

// Calculator Form Route
app.get('/calculator', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'calculator.html'));
});

// Perform Calculation
app.post('/calculate', (req, res) => {
    const num1 = parseFloat(req.body.num1);
    const num2 = parseFloat(req.body.num2);
    const result = num1 + num2;
    res.send(`<h1>Calculation Result</h1><p>The sum of ${num1} and ${num2} is ${result}</p><a href="/calculator">Back</a>`);
});

// Dynamic Route Example
app.get('/user/:name', (req, res) => {
    const userName = req.params.name;
    res.send(`<h1>Hello, ${userName}!</h1><a href="/">Go Home</a>`);
});

// Error Handling Middleware
app.use((req, res, next) => {
    res.status(404).send('<h1>404 - Page Not Found</h1>');
});

// Start the Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
