let timer;
let totalTime = 60; // 60 seconds
let timeLeft = totalTime;

function startTimer() {
 timer = setInterval(function() {
   timeLeft--;
   updateTimeDisplay();
   if(timeLeft <= 0) {
     clearInterval(timer);
     alert('Time is up!');
   }
 }, 1000);
}

function stopTimer() {
 clearInterval(timer);
}

function resetTimer() {
 clearInterval(timer);
 timeLeft = totalTime;
 updateTimeDisplay();
}

function updateTimeDisplay() {
 let minutes = Math.floor(timeLeft / 60);
 let seconds = timeLeft % 60;
 document.getElementById('time-left').textContent = `${minutes}:${seconds < 10 ? '0' + seconds : seconds}`;
}
 
 window.onload = function () {
    var time = 60 * 30, // your time in seconds here
        display = document.querySelector('#timer');
    startTimer(time, display);
 };