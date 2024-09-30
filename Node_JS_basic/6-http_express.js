const express = require('express');

const app = express();

app.get('/', (_, res) => {
  res.send('Hello Holberton School!');
});


app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
