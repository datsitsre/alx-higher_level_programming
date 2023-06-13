#!/usr/bin/node
/*
 * Return a number of occurrence in a list
 *
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
