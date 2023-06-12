#!/usr/bin/node

const myVar = process.argv[2];

if (isNaN(myVar) || myVar === undefined) {
  console.log('Missig number of occurences');
} else {
  for (let index = 0; index < myVar; index++) {
    console.log('C is fun');
  }
}
