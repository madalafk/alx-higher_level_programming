#!/usr/bin/node
/**
 *  class rectangle with width and height attributes
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
