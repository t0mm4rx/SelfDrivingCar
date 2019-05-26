class Road {

  constructor() {

    this.points =[
      [100, 100],
      [300, 100],
      [400, 500],
      [500, 500],
      [600, 100],
      [700, 100],
      [700, 700],
      [250, 700],
      [250, 400],
      [50, 400]
    ]

    this.vertices =[
      [50, 50],
      [350, 50],
      [450, 450],
      [550, 50],
      [750, 50],
      [750, 750],
      [200, 750],
      [200, 450],
      [0, 450],
      [50, 50],

      [150, 50],
      [120, 350],
      [300, 350],
      [300, 650],
      [650, 650],
      [650, 150],
      [550, 550],
      [350, 550],
      [250, 150],
      [50, 150]
    ]

  }

  draw() {

    noStroke()
    fill(100, 100, 140)
    beginShape()
    for (var i = 0; i < this.vertices.length; i++) {
      vertex(this.vertices[i][0], this.vertices[i][1])
    }
    endShape(CLOSE)

    noFill()
    stroke(255)
    strokeWeight(1)
    for (var i = 1; i < this.points.length; i++) {
      line(this.points[i - 1][0], this.points[i - 1][1], this.points[i][0], this.points[i][1])
    }
    line(this.points[this.points.length - 1][0], this.points[this.points.length - 1][1], this.points[0][0], this.points[0][1])

  }

}
