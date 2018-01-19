function timesTwo (number){
  var value = number*2;
  return value;
}

function timesSix(number){
  var result = timesTwo(number)*3;
  return result;
}
function rollDice(){
  return Math.floor((Math.random()*6)+1);
}

function taxTip(billtotal,tax,tip){
  var subtotal = billtotal + (billtotal * (tax / 100));
  var total = subtotal + (subtotal * (tip / 100));
  return total;
}

function arrayDoubled() {
  var originalArray = [1,2,3,4];
  for(var i = 0; i < originalArray.length; i++){
    var number = originalArray[i]*2;
    alert(number);
  }
}

function arraysMovies() {
  var favmoviesArray = []
}

function reverse() {
  var nums = [1,2,3,4,5,6];
  var revnums = [];
  var len = nums.length
  for(i = 0; i < len; i++){
    revnums.push(nums.pop());
  }
  return revnums;

}

function merge() {
  var numbers = [1,2,3];
  var letters = ["a","b","c","d","e"];
  var combined = [];
  var len = numbers.length;
  for (var i = 0; i < len; i++){
    combined.push(numbers.shift());
    combined.push(letters.shift());
  }
  return combined.concat(letters);


}

function niceRegularBox(){
  var array = ["Grim", "visaged", "War", "hath", "smooth'd", "his", "wrinkled", "front"];
  var len = array.length;
  var maxlen = 0;

  for(var i = 0; i < len; i++){
    if(array[i].length > maxlen){
      maxlen = array[i].length
    }
  }
var dash = "-";
var spaces = " ";
console.log(dash.repeat(maxlen));
  for(var i = 0; i < len; i++){
    console.log( "|" + array[i] + spaces.repeat(maxlen - array[i].length) + "|");
  }
  console.log(dash.repeat(maxlen));
}

function stringToMorse(){
var string = 'SOS'
var alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
var morse =

}
