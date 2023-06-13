#!/usr/bin/node
/*
 * Rectangle object
 */
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const myVar = '';
    for (let index = 0; index < myVar; index++) {
      console.log('X'.repeat(myVar));
    }
  }
}

module.exports = Rectangle;
