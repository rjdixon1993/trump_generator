'use strict';

//Lecture 1
// document.querySelector('.message'); //done in the same way as we select classes using css

// console.log(document.querySelector('.message').textContent);
// //returns solely the text content of the .message class elements

// document.querySelector('.message').textContent = 'Correct Number!!';
// document.querySelector('.number').textContent = 13;
// document.querySelector('.score').textContent = 100;

// document.querySelector('.guess').value = 23;
// console.log(document.querySelector('.guess').value);

//Lecture 73

const solution = Math.trunc(Math.random() * 20) + 1;
//putting it on the page to aid debugging
document.querySelector('.number').textContent = solution;

//Setting up the "lives left" variable
let lives = 20;
document.querySelector('.score').textContent = lives;

document.querySelector('.check').addEventListener('click', function () {
  let guess = Number(document.querySelector('.guess').value);
  console.log(guess);

  //Changingthe message to the user if no number is entered...
  //If guess is false ie if it's notavalue
  if (!guess) {
    document.querySelector('.message').textContent = 'No number entered... 👍 ';
  }
  //If we have entered a number, enter into this loop (but only if we still have lives)
  else if (guess == solution && lives > 1) {
    document.querySelector('.message').textContent = 'Correct 👍 ';
  }
  //If the guess is the wrong solution
  else if (guess !== solution) {
    //Only doing this bit if we have lives left
    if (lives > 1) {
      document.querySelector('.message').textContent = 'Try again nerd 👍 ';
      //Updating the lives variable on the page
      lives--;
      document.querySelector('.score').textContent = lives;
    }
    //If we have no lives left:
    else {
      document.querySelector('.message').textContent = 'You lost the game 🤣 ';
      lives = 0;
      document.querySelector('.score').textContent = lives;
    }
  }
});

//Limitations here:
// If we go down to 0,
