/**
 * Created by mingyu.zhang on 2019/9/17.
 */
    "use strict";
var a='abc';
var i=a.indexOf('b');
window.alert(i);
var c=[1,2,3];
var d = c.push('5');
window.alert(d);
var numbers1 = [45, 4, 9, 16, 25];
var sum = numbers1.reduce(myFunction);

function myFunction(total, value, index, array) {
  return total + value;
}window.alert(sum);
var f = new Date();
document.getElementById("sss").innerHTML = f.toDateString();