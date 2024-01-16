#!/usr/bin/node
const argv = process.argv;
const size = parseInt(argv[2]);
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  let mySquare = '';
  for (let k = 0; k < size; k++) {
    mySquare = mySquare.concat('X');
  }
  console.log(mySquare);
}
