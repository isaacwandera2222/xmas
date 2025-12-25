const c = document.getElementById("stars");
const ctx = c.getContext("2d");

c.width = window.innerWidth;
c.height = window.innerHeight;

let stars = [];
for(let i=0;i<200;i++){
    stars.push({
        x: Math.random()*c.width,
        y: Math.random()*c.height,
        size: Math.random()*2,
        speed: Math.random()*2+0.5
    });
}

function draw(){
    ctx.fillStyle = "black";
    ctx.fillRect(0,0,c.width,c.height);

    ctx.fillStyle = "white";
    stars.forEach(s=>{
        ctx.fillRect(s.x,s.y,s.size,s.size);
        s.y += s.speed;
        if(s.y > c.height) s.y = 0;
    });

    requestAnimationFrame(draw);
}

draw();
