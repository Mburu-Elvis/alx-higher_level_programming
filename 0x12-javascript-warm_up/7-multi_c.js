#!/usr/bin/node
const argv = process.argv;
let i = parseInt(argv[2]);
if (argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  if (i > 0) {
    while (i > 0) {
      console.log('C is fun');
      i--;
    }
  }
}
