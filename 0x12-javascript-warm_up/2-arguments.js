#!/usr/bin/node
const lenArgv = process.argv.length - 2;
if (lenArgv === 0) {
  console.log('No argument');
} else if (lenArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
