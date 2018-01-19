function greeting(){
  var userName = $('#name').val();
  var header = $("h2");
  header.text("Hello, " + userName + "!");
}

function setup() {
  $("#ok_button").click(greeting);
}

function hobbies() {
  var hobby = $("#hobby").val();
  $("ul").append("<li>" + hobby + "</li>");
}

function list() {
  $("#enter_button").click(hobbies);
}

function setup2() {
  $("body").append("<div></div>");
  $("div").mouseenter(changeColorToBlue);
  $("div").mouseleave(changeColorToRed);
}

function changeColorToBlue() {
  $(this).removeClass("red");
  $(this).addClass("blue");
}

$(document).ready(setup);
$(document).ready(list);
