// 1669 멍멍이 쓰다듬기
const fs = require("fs");
const [x, y] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);

const target = y-x;

if (target in [0, 1, 2, 3]) {
    console.log(target);
} else {
    const day = parseInt(Math.sqrt(target));
    if (target === day*day) {
        console.log(day*2-1);
    } else if (target <= day*(day+1)){
        console.log(day*2);
    } else {
        console.log(day*2+1);
    }
}