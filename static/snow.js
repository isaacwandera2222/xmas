const snowCanvas = document.createElement("canvas");
snowCanvas.style.position = "fixed";
snowCanvas.style.top = 0;
snowCanvas.style.left = 0;
snowCanvas.style.pointerEvents = "none";
document.body.appendChild(snowCanvas);

const ctx2 = snowCanvas.getContext("2d");

function resize() {
    snowCanvas.width = window.innerWidth;
    snowCanvas.height = window.innerHeight;
}
resize();
window.onresize = resize;

let flakes = [];
for (let i = 0; i < 150; i++) {
    flakes.push({
        x: Math.random() * snowCanvas.width,
        y: Math.random() * snowCanvas.height,
        r: Math.random() * 4 + 1,
        d: Math.random() + 1
    });
}

function snow() {
    ctx2.clearRect(0, 0, snowCanvas.width, snowCanvas.height);
    ctx2.fillStyle = "white";

    flakes.forEach(f => {
        ctx2.beginPath();
        ctx2.arc(f.x, f.y, f.r, 0, Math.PI * 2);
        ctx2.fill();

        f.y += f.d;
        if (f.y > snowCanvas.height) {
            f.y = 0;
            f.x = Math.random() * snowCanvas.width;
        }
    });

    requestAnimationFrame(snow);
}
snow();
