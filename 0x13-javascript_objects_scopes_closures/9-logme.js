#!/usr/bin/node

/*
 * 9. Log me
 */
let logme = 0;

exports.logMe = function (item) {
  console.log(logme + ': ' + item);
  logme++;
};
