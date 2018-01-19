function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function flyWhenClicked(){
  $("#pig").delay(1000).animate(
    {
        "margin-left": '1000px',
        opacity: '0',
        height: '500px',
        width: '500px',
       }
  );
  $("#pig2").delay(3000).animate(
    {
        "margin-left": '1000px',
        opacity: '0',
        height: '500px',
        width: '500px',
    }
  );
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#pig").click(flyWhenClicked);
    $("#pig2").click(flyWhenClicked);


}

$(document).ready(setup);
