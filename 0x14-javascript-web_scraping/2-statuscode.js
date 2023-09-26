#!/usr/bin/node
// displays the status code of a GET request.
const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
