/*

  Adaptation of a PS2 yabasic demo
  http://members.iinet.net.au/~jimshaw/Yabasic/yabres/demos/balroq/cavefly.txt
	REM *** CAVE-FLY *** (c) balroq 2002
	JS ge1doot Sept 2015
	
*/

~ function() {

		'use strict';

		var RESOLUTION_X = 719,
				RESOLUTION_Y = 719,
				q = 120,
				s = 800,
				points = [],
				ang = 0,
				mx = q,
				mmx;

		// Vertex object constructor

		var Point = function(x, y, z) {

				this.px = x;
				this.py = y;
				this.pz = z;
				this.tx = 0;
				this.ty = 0;
				this.tz = 0;

		}

		// 3D to 2D projection

		Point.prototype.project = function(cmx) {

				this.px += 6;
				if (this.px > s) {
						this.px = this.px - s * 2 - 50;
						this.pz = 200 + Math.random() * 800;
						if (cmx) {
								cmx = false;
								mmx = mx;
								mx--;
								if (mx < 110) mx = 120;
						}
				}

				var z = -this.px + s;
				this.tx = RESOLUTION_X / 2 + this.py * 300 / z;
				this.ty = RESOLUTION_Y / 2 - this.pz * 300 / z;
				this.tz = z;
				return cmx;

		}

		// build cave

		for (var y = -s; y <= s; y += s / 5) {
				for (var x = -s; x <= s; x += s / 5) {
						points.push(
								new Point(
										x,
										y * 2,
										200 + Math.random() * 800
								)
						);
				}
		}

		// draw 2 x poly

		function draw(p0, p1, p2, p3) {

				var light = (100 - p0.tz / (s * 2 / 100)) / 1;
				var offsetX = RESOLUTION_X / 2;
				var offsetY = RESOLUTION_Y / 2;

				ctx.beginPath();
				ctx.fillStyle = 'hsl(47, 30%, ' + light + '%)';
				ctx.moveTo(-offsetX + p0.tx, -offsetY + p0.ty);
				ctx.lineTo(-offsetX + p1.tx, -offsetY + p1.ty);
				ctx.lineTo(-offsetX + p2.tx, -offsetY + p2.ty);
				ctx.lineTo(-offsetX + p3.tx, -offsetY + p3.ty);
				ctx.fill();

				ctx.beginPath();
				ctx.fillStyle = 'hsl(227, 30%, ' + light + '%)';
				ctx.moveTo(offsetX - p0.tx, offsetY - p0.ty);
				ctx.lineTo(offsetX - p1.tx, offsetY - p1.ty);
				ctx.lineTo(offsetX - p2.tx, offsetY - p2.ty);
				ctx.lineTo(offsetX - p3.tx, offsetY - p3.ty);
				ctx.fill();

		}

		//  main loop 

		function run() {

				requestAnimationFrame(run);

				ctx.clearRect(0, 0, RESOLUTION_X, RESOLUTION_Y);

				var x = pointer.x / 100;
				ang += (x - ang) / 10;

				// project

				var cmx = true;
				for (var i = 0; i <= q; i++) {
						cmx = points[i].project(cmx);
				}

				// draw

				ctx.save();
				ctx.translate(RESOLUTION_X / 2, RESOLUTION_Y / 2);
				ctx.rotate(ang);

				for (var y = 0; y < 10; y++) {
						for (var x = 0; x < 10; x++) {
								var i = mmx + y;
								if (i > 120) i -= 11;
								var j = i + 1;
								if (j > 120) j -= 11;
								draw(
										points[i - x * 11],
										points[i - (x + 1) * 11],
										points[j - (x + 1) * 11],
										points[j - x * 11]
								);

						}
				}

				ctx.restore();

				// vignette
				ctx.fillStyle = grd;
				ctx.fillRect(0, 0, RESOLUTION_X, RESOLUTION_Y);

		};

		// set canvas

		var canvas = {
				width: 0,
				height: 0,
				elem: document.createElement('canvas'),
				init: function() {
						var ctx = this.elem.getContext('2d');
						document.body.appendChild(this.elem);
						this.elem.width = RESOLUTION_X;
						this.elem.height = RESOLUTION_Y;
						return ctx;
				}
		};

		var ctx = canvas.init();

		// vignette
		var outerRadius = RESOLUTION_X * 0.7;
		var innerRadius = RESOLUTION_X * 0.3;
		var grd = ctx.createRadialGradient(RESOLUTION_X / 2, RESOLUTION_Y / 2, innerRadius, RESOLUTION_X / 2, RESOLUTION_Y / 2, outerRadius);
		grd.addColorStop(0, 'rgba(0,0,0,0)');
		grd.addColorStop(1, 'rgba(0,0,0,0.8)');

		// pointer

		var pointer = (function(canvas) {
				var pointer = {
						x: 0,
						y: 0,
						canvas: canvas,
						pointer: function(e) {
								var touchMode = e.targetTouches,
										pointer;
								if (touchMode) {
										e.preventDefault();
										pointer = touchMode[0];
								} else pointer = e;
								this.x = pointer.clientX;
								this.y = pointer.clientY;
						},
				};
				window.addEventListener('mousemove', function(e) {
						this.pointer(e);
				}.bind(pointer), false);
				canvas.elem.addEventListener('touchmove', function(e) {
						this.pointer(e);
				}.bind(pointer), false);
				return pointer;
		}(canvas));

		// start

		ang = pointer.x;
		run();

}();icks/11/