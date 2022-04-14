const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send(`

    <h1>Hamko kuch ni ata</h1>
    `);
});

app.get('/error', (req, res) => {
    process.exit(1);
})

app.listen(8080);