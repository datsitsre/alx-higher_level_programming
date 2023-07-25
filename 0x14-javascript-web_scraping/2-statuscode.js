#!/usr/bin/node
// Status code
const req = require('request');

req(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode);
});
