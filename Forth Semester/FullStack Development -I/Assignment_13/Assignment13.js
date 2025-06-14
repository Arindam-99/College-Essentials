const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const operations = require('./operations');

const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

// Home Page Route
app.get('/', (req, res) => {
    res.send('<h1>Welcome to the Calculator</h1><a href="/calculator">Go to Calculator</a>');
});

// Calculator Page Route
app.get('/calculator', (req, res) => {
    res.send(`
        <h1>Simple Calculator</h1>
        <form action="/calculate-result" method="POST">
            <input type="number" name="num1" placeholder="Enter first number" required>
            <input type="number" name="num2" placeholder="Enter second number" required>
            <select name="operation">
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
    `);
});

// Calculate Result Route
app.post('/calculate-result', (req, res) => {
    const num1 = parseFloat(req.body.num1);
    const num2 = parseFloat(req.body.num2);
    const operation = req.body.operation;
    let result;

    switch (operation) {
        case 'add':
            result = operations.add(num1, num2);
            break;
        case 'subtract':
            result = operations.subtract(num1, num2);
            break;
        case 'multiply':
            result = operations.multiply(num1, num2);
            break;
        case 'divide':
            result = num2 !== 0 ? operations.divide(num1, num2) : 'Error: Division by zero';
            break;
        default:
            result = 'Invalid operation';
    }
    
    res.send(`<h1>Result</h1><p>The result of ${operation} on ${num1} and ${num2} is ${result}</p><a href="/calculator">Back</a>`);
});

// Start the Server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
