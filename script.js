var car = null
var road = null

var up = false
var down = false
var left = false
var right = false

var data = []

function setup() {

  createCanvas(800, 800)
  road = new Road()
  car = new Car(100, 100)

}

function draw() {

  background(50, 50, 70)
  road.draw()
  console.log(data.length)
  car.draw()

  if (data.length >= 10000) {
    var tab = window.open('about:blank', '_blank');
    tab.document.write(JSON.stringify(data));
    tab.document.close();
  }

}

function keyPressed() {
  if (keyCode == 38)
    up = true
  if (keyCode == 40)
    down = true
  if (keyCode == 39)
    right = true
  if (keyCode == 37)
    left = true
}

function keyReleased() {
  if (keyCode == 38)
    up = false
  if (keyCode == 40)
    down = false
  if (keyCode == 39)
    right = false
  if (keyCode == 37)
    left = false
}
