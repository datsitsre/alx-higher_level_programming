#!/usr/bin/node
/*
 * Task 17
 */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value++;
};
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
