const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((e) => +e);

solution(input);
function solution(input) {
  let large_num = Math.max(...input);
  const check_prime = [];

  // Find all prime numbers up to n
  for (let i = 3; i <= large_num; i += 2) {
    check_prime[i] = true;
  }

  check_prime[2] = true;

  const limit = Math.sqrt(large_num);
  for (let m = 3; m <= limit; m += 2) {
    if (check_prime[m]) {
      for (let k = m * m; k <= large_num; k += m) {
        check_prime[k] = false;
      }
    }
  }

  let p = 3;
  for (let i = 0; i < input.length; i++) {
    let value = input[i];

    for (; p <= value / 2; p += 2) {
      if (check_prime[value - p] && check_prime[p]) {
        console.log(`${value} = ${p} + ${value - p}`);
        break;
      }
    }
    if (p > value / 2) p = 3;
  }
}
