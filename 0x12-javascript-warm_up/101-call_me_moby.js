#!/usr/bin/node

exports.callMeMoby = function (times, callback) {
  for (let i = 0; i < times; i++) {
    callback();
  }
};

