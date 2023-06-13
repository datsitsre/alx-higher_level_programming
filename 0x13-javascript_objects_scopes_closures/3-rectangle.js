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
    for (let index = 0; index < this.height; index++) {
      let index2 = 0;
      for (; index2 < this.width; ++index2) {
        process.stdout.write('X');
      }
      if (index2 === this.width) {
        console.log('');
      }
    }
  }
}

module.exports = Rectangle;
