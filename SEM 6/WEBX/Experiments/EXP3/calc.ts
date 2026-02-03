import * as readlineSync from "readline-sync";

const num1Str = readlineSync.question("pehla number daalo bhai: ");
const num1 = parseFloat(num1Str);

const num2Str = readlineSync.question("doosra number daalo pleej: ");
const num2 = parseFloat(num2Str);

const operator = readlineSync.question("kya karna hai in dono number ka (+, -, *, /, %, **): ", {
    limit: ["+", "-", "*", "/", "%", "**"],
    limitMessage: "sahi operator daalo pleej (+, -, *, /, %, **)",
});

if (isNaN(num1) || isNaN(num2)) {
    console.error("Error: number daalona pleej");
}

let result: number;
try {
    switch (operator) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            if (num2 === 0) {
                throw new Error("zero se divide nahi hota hai bro");
            }
            result = num1 / num2;
            break;
        case "%":
            result = num1 % num2;
            break;
        case "**":
            result = Math.pow(num1, num2);
            break;
        default:
            throw new Error(`galat operator: ${operator}`);
    }

    console.log(`\n${num1} ${operator} ${num2} = ${result}`);
} catch (error) {
    if (error instanceof Error) {
        console.error(`Error: ${error.message}`);
    }
}
