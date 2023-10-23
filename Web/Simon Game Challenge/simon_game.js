// creating array
var buttonColours = ["red", "blue", "green", "yellow"];

var gamePattern = [];

var userClickedPattern = [];

var started = false;
var level = 0;

// keypress function
$(document).keypress(function() {
  if (!started) {
    $(".head").text("level " + level);
    nextSequence();
    started = true;
  }
})

// handler function
$(".btn").click(function() {
  var userChosenColor = $(this).attr("id");
  userClickedPattern.push(userChosenColor);

  playsound(userChosenColor);
  animatePress(userChosenColor);

  checkanswer(userClickedPattern.length - 1);
});


// creating random number
function nextSequence() {
  userClickedPattern = [];
  level++;
  $(".head").text("level " + level);
  var randomNumber = Math.floor(Math.random() * 4);
  var randomChosenColour = buttonColours[randomNumber];
  gamePattern.push(randomChosenColour);

  $("#" + randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);
  playSound(randomChosenColour);
}

function playsound(name) {
  var audio = new Audio("sounds/" + name + ".mp3");
  audio.play();
}

function animatePress(currentColor) {
  $("#" + currentColor).addClass("pressed");
  setTimeout(function() {
    $("#" + currentColor).removeClass("pressed");
  }, 100);
}

function checkanswer(currentLevel) {
  if (gamePattern[currentLevel] === userClickedPattern[currentLevel]) {
    if (userClickedPattern.length === gamePattern.length) {
      setTimeout(function() {
        nextSequence();
      }, 1000);
    }

  } else {
    playsound("wrong");
    $("body").addClass("game-over");
    $(".head").text("Game Over, Press Any Key to Restart");

    setTimeout(function(){
      $("body").removeClass("game-over");
    },200);

    startOver();
  }
}

function startOver(){
  level = 0;
  gamePattern = [];
  started = false;
}
