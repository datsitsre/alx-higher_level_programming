#!/usr/bin/node
/*
 *
 * Imports Array amd computes a new array
 */

const array1 = require('./100-data').list;

console.log(array1);
console.log(array1.map((x, idx) => x * idx));
