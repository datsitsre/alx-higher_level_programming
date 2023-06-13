#!/usr/bin/node
/*
 * Square object
 */
const SqaureObje = require('./5-square');
class Square extends SqaureObje {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
}
module.exports = Square;
