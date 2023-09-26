#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});