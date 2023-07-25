#!/usr/bin/node
// Contents of a webpage and sores it in a file
const request = require('request');
const filename = require('fs');

request(process.argv[2], function (_err, _res, body) {
  filename.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
