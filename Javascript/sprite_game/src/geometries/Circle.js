export default class Circle {
	constructor(x, y, size, speed = 10, color = "#00f") {
		this.x = x;
		this.y = y;
		this.size = size;
		this.speed = speed;
		this.color = color;
		this.line = 3
	}

	draw(ctx) {
		this.circ(ctx,
			this.x,
			this.y,
			this.size,
			this.line,
			this.color,
			this.color)
	}

	circ(ctx, pos_x, pos_y, radius, line, color, fill = false) {
		ctx.lineWidth = line;
		ctx.strokeStyle = color
		ctx.beginPath();
		ctx.arc(pos_x, pos_y, radius, 0, Math.PI*2);
		ctx.stroke();
		if (fill) {
			ctx.fillStyle = fill
			ctx.fill()
		}
	}
	
	anda(limits, key) {

		switch (key) {
			case 's':
				this.status = 'down'
				break
			case 'w':
				this.status = 'up'
				break
			case 'a':
				this.status = 'left'
				break
			case 'd':
				this.status = 'right'
				break
		}

		switch (this.status) {
			case 'down':
				this.y += this.speed
				break
			case 'up':
				this.y -= this.speed
				break
			case 'left':
				this.x -= this.speed
				break
			case 'right':
				this.x += this.speed
				break
		}

		if (this.x > limits.width)
			this.x = -this.size
		else if (this.x + this.size < 0)
			this.x = limits.width - this.size

		if (this.y > limits.height)
			this.y = -this.size
		else if (this.y + this.size < 0)
			this.y = limits.height - this.size
	}

	colide(circ) {
		return Math.abs(this.x-circ.x) < (this.size+circ.size)*0.9
			   && Math.abs(this.y-circ.y) < (this.size+circ.size)*0.9
	}
}