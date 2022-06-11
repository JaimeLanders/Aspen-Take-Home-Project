'use strict';

// load environment variables
const { error: dotenvError } = require('dotenv').config();
if (dotenvError) {
  throw dotenvError;
}
const MESSAGE = process.env.MESSAGE || 'Hello world!';
const PORT = parseInt(process.env.PORT, 10) || 3000;

const express = require('express');
const app = express();
const os = require('os');

// capture configurable settings
app.locals.MESSAGE = MESSAGE;
app.locals.PORT = PORT;

app.get('/', (req, res) => {
  res.send({
    hostname: os.hostname(),
    msg: MESSAGE,
    nodeVersion: process.version,
    pid: process.pid,
    uptime: process.uptime(),
  });
});

app.listen(PORT, () => {
  console.log(`[${process.pid}] listening at http://localhost:${PORT}`);
});

module.exports = app;
