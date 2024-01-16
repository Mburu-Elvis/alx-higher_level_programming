#!/usr/bin/node
const argv = process.argv;
let myStr;
if (argv[2] === undefined) {
  argv[2] = 'undefined';
}
if (argv[3] === undefined) {
  argv[3] = 'undefined';
}
myStr = argv[2];
myStr = myStr.concat(' is ');
myStr = myStr.concat(argv[3]);
console.log(myStr);
