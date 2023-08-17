#!/usr/bin/node
/**
 * this script imports a dictionary of occurrences by user id and computes a
 * dictionary of user ids by occurrence
 */

const dict = require('./101-data.js').dict;
const newDict = {};

for (const occurences in dict) {
  if (dict.hasOwnProperty(occurences)) {
    const value = dict[occurences];
    newDict[value] = newDict[value] || [];
    newDict[value].push(occurences);
  }
}

console.log(newDict);
