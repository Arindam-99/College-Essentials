const { performance } = require('perf_hooks');

function measureExecutionTime(fn, ...args) {
    const start = performance.now();
    const result = fn(...args);
    const end = performance.now();
    return { result, time: end - start };
}

function exampleFunction1() {
    let sum = 0;
    for (let i = 0; i < 1e6; i++) {
        sum += i;
    }
    return sum;
}

function exampleFunction2(n) {
    return Array.from({ length: n }, (_, i) => i ** 2);
}

const functions = [
    { name: 'exampleFunction1', fn: exampleFunction1, args: [] },
    { name: 'exampleFunction2', fn: exampleFunction2, args: [1e5] }
];

functions.forEach(({ name, fn, args }) => {
    const { result, time } = measureExecutionTime(fn, ...args);
    console.log(`${name} executed in ${time.toFixed(2)} ms`);
});

// Output
//exampleFunction1 executed in 5.97 ms
//exampleFunction2 executed in 9.77 ms