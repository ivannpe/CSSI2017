function greeting(){
  var userName = $('#username').val();
  alert("You are awesome \n" + userName);
  var header = $("h2");
  header.text("Hey " + userName + ", I knew I remembered you")
}

function setup() {
  $("#ok_button").click(greeting);
}

$(document).ready(setup);
