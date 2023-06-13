#!/usr/bin/node

/*
 *
 * 10. Number conversion
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
