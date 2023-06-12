#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myVar = process.argv.slice(2).map(Number);
  const myVar2 = myVar.sort(function (n, b) { return b - n; })[1];
  console.log(myVar2);
}
