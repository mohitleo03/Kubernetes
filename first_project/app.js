const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send(`
    <h1>Hello from node</h1>
    <p>This is some data</p>
    `);
});

app.get('/error', (req, res) => {
    process.exit(1);
})

app.listen(8080);