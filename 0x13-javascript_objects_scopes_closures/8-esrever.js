#!/usr/bin/node
/**
 * this function  returns the reversed version of a list
 */

exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
