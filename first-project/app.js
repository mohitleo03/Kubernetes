const express = require('express');

const app = express();

app.get('/', (req, res) => {
    try{
        res.send(`
        <h1>Hello from Node</h1>
        <h2>Changes</h2>
        `);
    }
    catch(err){
        console.log(err);
    }
});

app.get('/error', (req, res) => {
    process.exit(1);
})

app.listen(8000);