import Quad from "./Quad";

export default class Rect extends Quad{

	draw(ctx){
		ctx.lineWidth = 5;
		ctx.fillStyle = this.color;
		ctx.fillRect(this.x, this.y, this.size, this.size*2);
	}
}