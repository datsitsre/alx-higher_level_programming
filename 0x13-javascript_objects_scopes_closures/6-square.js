#!/usr/bin/node
/*
 * Square object
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
}
module.exports = Square;
