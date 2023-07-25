#!/usr/bin/node
const filename = require('fs');

filename.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
