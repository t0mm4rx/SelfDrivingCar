class Car {

  constructor(x, y) {
    this.position = createVector(x, y)
    this.speed = createVector(0, 0)
    this.acc = createVector(0, 0)
    this.direction = createVector(1, 0)

    this.SENSOR_LENGTH = 300
    this.s1 = this.SENSOR_LENGTH
    this.s2 = this.SENSOR_LENGTH
    this.s3 = this.SENSOR_LENGTH
    this.s4 = this.SENSOR_LENGTH
    this.s5 = this.SENSOR_LENGTH
    this.s6 = this.SENSOR_LENGTH
    this.s7 = this.SENSOR_LENGTH

    this.MAX_SPEED = 3
    this.ACC = .2
    this.DEC = .95
    this.BREAK = .8
    this.ROT = Math.PI / 40
  }

  draw() {
    fill(255)
    rectMode(CENTER, CENTER)
    push()
    translate(this.position.x, this.position.y)
    rotate(this.direction.heading())
    rect(0, 0, 30, 15)
    pop()

    let sensor1 = this.direction.copy().rotate(Math.PI / 4).normalize().mult(this.SENSOR_LENGTH)
    let sensor2 = this.direction.copy().normalize().mult(this.SENSOR_LENGTH)
    let sensor3 = this.direction.copy().rotate(-Math.PI / 4).normalize().mult(this.SENSOR_LENGTH)
    let sensor4 = this.direction.copy().rotate(Math.PI / 2).normalize().mult(this.SENSOR_LENGTH)
    let sensor5 = this.direction.copy().rotate(-Math.PI / 2).normalize().mult(this.SENSOR_LENGTH)
    let sensor6 = this.direction.copy().rotate(Math.PI / 8).normalize().mult(this.SENSOR_LENGTH)
    let sensor7 = this.direction.copy().rotate(-Math.PI / 8).normalize().mult(this.SENSOR_LENGTH)

    let sensor1_nor = this.direction.copy().rotate(Math.PI / 4).normalize()
    let sensor2_nor = this.direction.copy().normalize()
    let sensor3_nor = this.direction.copy().rotate(-Math.PI / 4).normalize()
    let sensor4_nor = this.direction.copy().rotate(Math.PI / 2).normalize()
    let sensor5_nor = this.direction.copy().rotate(-Math.PI / 2).normalize()
    let sensor6_nor = this.direction.copy().rotate(Math.PI / 8).normalize()
    let sensor7_nor = this.direction.copy().rotate(-Math.PI / 8).normalize()

    strokeWeight(.3)
    stroke(255)
    line(this.position.x, this.position.y, this.position.x + sensor1.x, this.position.y + sensor1.y)
    line(this.position.x, this.position.y, this.position.x + sensor2.x, this.position.y + sensor2.y)
    line(this.position.x, this.position.y, this.position.x + sensor3.x, this.position.y + sensor3.y)
    line(this.position.x, this.position.y, this.position.x + sensor4.x, this.position.y + sensor4.y)
    line(this.position.x, this.position.y, this.position.x + sensor5.x, this.position.y + sensor5.y)
    line(this.position.x, this.position.y, this.position.x + sensor6.x, this.position.y + sensor6.y)
    line(this.position.x, this.position.y, this.position.x + sensor7.x, this.position.y + sensor7.y)

    this.s1 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor1.x, this.position.y + sensor1.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor1.x, this.position.y + sensor1.y, inter[0], inter[1])
      ) {
        this.s1 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s1)
      }
    }

    this.s2 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor2.x, this.position.y + sensor2.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (inter == null) {
        this.s2 = 0
        break
      }
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor2.x, this.position.y + sensor2.y, inter[0], inter[1])
      ) {
        this.s2 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s2)
      }
    }

    this.s3 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor3.x, this.position.y + sensor3.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor3.x, this.position.y + sensor3.y, inter[0], inter[1])
      ) {
        this.s3 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s3)
      }
    }

    this.s4 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor4.x, this.position.y + sensor4.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor4.x, this.position.y + sensor4.y, inter[0], inter[1])
      ) {
        this.s4 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s4)
      }
    }
    this.s5 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor5.x, this.position.y + sensor5.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor5.x, this.position.y + sensor5.y, inter[0], inter[1])
      ) {
        this.s5 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s5)
      }
    }
    this.s6 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor6.x, this.position.y + sensor6.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor6.x, this.position.y + sensor6.y, inter[0], inter[1])
      ) {
        this.s6 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s6)
      }
    }
    this.s7 = this.SENSOR_LENGTH
    for (var i = 0; i < road.points.length; i++) {
      let p1 = road.points[i]
      let p2 = road.points[0]
      if (i < road.points.length - 1)
        p2 = road.points[i + 1]

      let inter = math.intersect(
          [this.position.x, this.position.y],
          [this.position.x + sensor7.x, this.position.y + sensor7.y],
          [p1[0], p1[1]],
          [p2[0], p2[1]]
      )
      if (
        this.pointInside(p1[0], p1[1], p2[0], p2[1], inter[0], inter[1])
        &&
        this.pointInside(this.position.x, this.position.y, this.position.x + sensor7.x, this.position.y + sensor7.y, inter[0], inter[1])
      ) {
        this.s7 = min(min(p5.Vector.dist(createVector(inter[0], inter[1]), this.position), this.SENSOR_LENGTH), this.s7)
      }
    }

    noStroke()
    fill(200, 100, 100)
    ellipseMode(CENTER, CENTER)
    ellipse(this.position.x + sensor1_nor.x * this.s1, this.position.y + sensor1_nor.y * this.s1, 10, 10)
    ellipse(this.position.x + sensor2_nor.x * this.s2, this.position.y + sensor2_nor.y * this.s2, 10, 10)
    ellipse(this.position.x + sensor3_nor.x * this.s3, this.position.y + sensor3_nor.y * this.s3, 10, 10)
    ellipse(this.position.x + sensor4_nor.x * this.s4, this.position.y + sensor4_nor.y * this.s4, 10, 10)
    ellipse(this.position.x + sensor5_nor.x * this.s5, this.position.y + sensor5_nor.y * this.s5, 10, 10)
    ellipse(this.position.x + sensor6_nor.x * this.s6, this.position.y + sensor6_nor.y * this.s6, 10, 10)
    ellipse(this.position.x + sensor7_nor.x * this.s7, this.position.y + sensor7_nor.y * this.s7, 10, 10)

    this.speed.add(this.acc)
    this.position.add(this.speed)

    if (up && this.speed.mag() < this.MAX_SPEED) {
      this.acc = this.direction.copy().mult(this.ACC)
    } else {
      this.acc = createVector(0, 0)
      this.speed.mult(this.DEC)
    }

    if (down) {
      this.speed.mult(this.BREAK)
    }

    if (left)
      this.direction.rotate(-this.ROT * this.speed.mag() / this.MAX_SPEED)
    if (right)
      this.direction.rotate(this.ROT * this.speed.mag() / this.MAX_SPEED)


    data.push(
      [this.s1,this.s2,this.s3,this.s4,this.s5,this.s6,this.s7,up,right,down,left]
    )


  }

  pointInside(p1x, p1y, p2x, p2y, px, py) {
    if ((p1x >= px - 1 && px + 1 >= p2x) || (p1x <= px + 1 && px - 1 <= p2x)) {
      if ((p1y >= py - 1 && py + 1 >= p2y) || (p1y <= py + 1 && py - 1 <= p2y)) {
        return true
      }
    }
    return false
  }

}
