

function setup() {
  $("body").append("<div></div>");
  $("div").mouseenter(changeColorToBlue);
  $("div").mouseleave(changeColorToRed);
}

function changeColorToBlue() {
  $(this).removeClass("red");
  $(this).addClass("blue");
}

function changeColorToRed() {
  $(this).removeClass("blue");
  $(this).addClass("red");
}

$(document).ready(setup);
