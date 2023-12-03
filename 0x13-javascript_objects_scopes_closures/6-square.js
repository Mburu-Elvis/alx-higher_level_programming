#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
  }
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let k = 0; k < this.width; k++) {
        row = row.concat(c);
      }
      console.log(row);
    }
  }
}
module.exports = Square;
