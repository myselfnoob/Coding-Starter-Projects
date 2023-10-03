import Circle from './geometries/Circle';
import { loadImage } from './loaderAssets';

export default class Hero extends Circle {
  constructor(x, y, size, speed = 10, width, height, imgUrl, FRAMES) {
    super(x, y, size, speed);
    this.imgUrl = imgUrl;
    loadImage(this.imgUrl).then((img) => (this.img = img));

    this.cellWidth = 63;
    this.cellHeight = 58;
    this.cellX = 0;
    this.totalSprites = 4;
    this.spriteSpeed = 1;

    this.width = width;
    this.height = height;

    this.status = 'left';

    this.hit = new Circle(
      this.x + this.width / 2,
      this.y + this.height / 2,
      this.size,
      0,
      'transparent'
    );

    this.animeSprite(FRAMES);
    this.setControls();
  }

  draw(CTX) {
    this.setCellY();

    CTX.drawImage(
      this.img,
      this.cellX * this.cellWidth,
      this.cellY * this.cellHeight,
      this.cellWidth,
      this.cellHeight,
      this.x,
      this.y,
      this.width,
      this.height
    );

    this.hit.draw(CTX);
  }

  animeSprite = (FRAMES) => {
    //Controla a animacao do sprite
    setInterval(() => {
      this.cellX = this.cellX < this.totalSprites - 1 ? this.cellX + 1 : 0;
    }, 1000 / ((FRAMES * this.spriteSpeed) / 10));
  };

  setControls() {
    this.controls = {
      s: 'down',
      w: 'up',
      a: 'left',
      d: 'rigth'
    };
  }

  setCellY() {
    let sprites = {
      rigth: 0,
      left: 1,
      up: 2,
      down: 3
    };

    this.cellY = sprites[this.status];
  }

  move(limits, key) {
    let movements = {
      down: {
        x: this.x,
        y: this.y + this.speed
      },
      up: { x: this.x, y: this.y - this.speed },
      left: { x: this.x - this.speed, y: this.y },
      rigth: { x: this.x + this.speed, y: this.y }
    };

    this.status = this.controls[key] ? this.controls[key] : this.status;

    this.x = movements[this.status].x;
    this.y = movements[this.status].y;

    this.updateHit();
    this.limits(limits);
  }

  limits(limits) {
    this.x = this.x - this.size > limits.width ? -this.size : this.x;

    this.x = this.x + this.size < 0 ? limits.width - this.size : this.x;

    this.y =
      this.y - this.size > limits.height + this.size ? -this.size : this.y;
    this.y = this.y + this.size < 0 ? limits.height + this.size : this.y;
  }

  updateHit() {
    this.hit.x = this.x + this.width / 2;
    this.hit.y = this.y + this.height / 2;
  }

  colide(other) {
    return (
      this.hit.size + other.size >=
      Math.sqrt((this.hit.x - other.x) ** 2 + (this.hit.y - other.y) ** 2)
    );
  }
}
