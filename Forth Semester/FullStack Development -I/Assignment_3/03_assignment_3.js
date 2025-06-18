//3.Write a Node.js program to demonstrate command-line argument and parse their values.

// Install yargs using: npm install yargs
const yargs = require('yargs');

// Parsing command-line arguments
const argv = yargs
    .usage('Usage: node $0 --name [string] --age [num]')
    .option('name', {
        alias: 'n',
        describe: 'Your name',
        type: 'string',
        demandOption: true
    })
    .option('age', {
        alias: 'a',
        describe: 'Your age',
        type: 'number',
        demandOption: true
    })
    .help()
    .argv;

// Displaying parsed values
console.log(`Hello, ${argv.name}! You are ${argv.age} years old.`);
 // Running process
 /*node 03_assignment_3.js --name "Arindam" --age 25
>>
Hello, Arindam! You are 25 years old. */