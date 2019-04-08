var timelineNew = new TimelineMax();
// TweenMax.from(".welcome", 0.7, { x: 1000 });
// TweenMax.to(".welcome", 0.5, { x: -1000, delay: 1.2 });
// setTimeout(function() {
//   document.querySelector(".welcome").style.display = "none";
// }, 1500);
TweenMax.from(".title", 1, { x: 1000, delay: 1.0 });
TweenMax.from(".subtitle", 1, { x: -1000, delay: 1.5 });

var timeline = new TimelineMax();
timeline.from(".terminal-container", 1, {
  // scale: 0,
  x: 1000,
  ease: Back.easeOut.config(2)
});
function sidebar_trans() {
  TweenMax.from(".sidebar", 1, {
    x: -1000,
    ease: Back.easeOut.config(1.7)
  });
  TweenMax.staggerFrom(
    ".sidebar a",
    0.7,
    { scale: 0, opacity: 0, x: 500 },
    0.3
  );
}
function sidebar_trans_back() {
  TweenMax.to(".sidebar", 1, {
    x: -1000,
    ease: Back.easeOut.config(1.7)
  });
  document.getElementById("sidebarId").style.display = "none";
  TweenMax.to(".sidebar", 1, {
    x: 0
  });
}
function changeToDark() {
  document.querySelector(".home-content").style.color = "white";
  document.querySelector("#world").style.backgroundColor = "black";
  document.querySelector(".openSidebar-btn").style.color = "white";
  document.querySelector(".chgv-btn1").style.display = "none";
  document.querySelector(".chgv-btn2").style.display = "block";
}
function changeToLight() {
  document.querySelector(".home-content").style.color = "black";
  document.querySelector("#world").style.backgroundColor = "white";
  document.querySelector(".openSidebar-btn").style.color = "black";
  document.querySelector(".chgv-btn1").style.display = "block";
  document.querySelector(".chgv-btn2").style.display = "none";
}
