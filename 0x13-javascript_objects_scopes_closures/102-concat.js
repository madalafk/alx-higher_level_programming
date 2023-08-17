#!/usr/bin/node
/**
 * this script concatenates 2 files
 */

const fs = require('fs');
const file_1 = fs.readFileSync(process.argv[2], 'utf8');
const file_2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], file_1 + file_2);
