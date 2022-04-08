const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send(`
    <h1>Hello from node</h1>
    <p>Hamko kuch ni ata</p>
    `);
});

app.get('/error', (req, res) => {
    process.exit(1);
})

app.listen(8080);