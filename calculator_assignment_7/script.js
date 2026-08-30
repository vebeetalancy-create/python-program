/* ------------------------------
Calculator Variables
------------------------------ */

let firstNumber = "";
let operator = "";
let secondNumber = "";

/* ------------------------------
Get Display Element
------------------------------ */

const display = document.getElementById("display");

/* ------------------------------
Add Number to Display
------------------------------ */

function appendNumber(number) {


// If display currently shows 0, replace it
if (display.value === "0") {
    display.value = number;
}

// If an operator has already been selected,
// add the second number
else {
    display.value += number;
}


}

/* ------------------------------
Select Operator
------------------------------ */

function chooseOperator(selectedOperator) {


// Don't allow another operator without a number
if (display.value === "0" && firstNumber === "") {
    return;
}

// Store the first number
if (firstNumber === "") {

    firstNumber = parseFloat(display.value);

    operator = selectedOperator;

    // Show expression on display
    display.value = firstNumber + " " + getOperatorSymbol(selectedOperator) + " ";
}


}

/* ------------------------------
Convert Operator to Symbol
------------------------------ */

function getOperatorSymbol(operator) {


if (operator === "*") {
    return "×";
}

if (operator === "/") {
    return "÷";
}

if (operator === "-") {
    return "−";
}

return operator;


}

/* ------------------------------
Handle Number After Operator
------------------------------ */

display.addEventListener("input", function () {


// This function is not required for the calculator,
// but the display is kept readonly in HTML.


});

/* ------------------------------
Calculate Result
------------------------------ */

function calculate() {


if (firstNumber === "" || operator === "") {
    return;
}

// Get the number after the operator
let expression = display.value;

let parts = expression.trim().split(" ");

secondNumber = parseFloat(parts[2]);


// Make sure second number exists
if (isNaN(secondNumber)) {
    return;
}

let result;


/* Perform calculation */

switch (operator) {

    case "+":
        result = firstNumber + secondNumber;
        break;

    case "-":
        result = firstNumber - secondNumber;
        break;

    case "*":
        result = firstNumber * secondNumber;
        break;

    case "/":

        // Prevent division by zero
        if (secondNumber === 0) {

            display.value = "Cannot divide by 0";

            resetCalculator();

            return;
        }

        result = firstNumber / secondNumber;
        break;

    case "%":
        result = firstNumber % secondNumber;
        break;

    default:
        return;
}


// Show result
display.value = result;

// Reset calculator
firstNumber = "";
secondNumber = "";
operator = "";


}

/* ------------------------------
Clear Calculator
------------------------------ */

function clearDisplay() {


display.value = "0";

resetCalculator();


}

/* ------------------------------
Delete Last Character
------------------------------ */

function deleteLast() {


if (display.value.length > 1) {

    display.value = display.value.slice(0, -1);

} else {

    display.value = "0";
}


}

/* ------------------------------
Reset Calculator
------------------------------ */

function resetCalculator() {


firstNumber = "";

secondNumber = "";

operator = "";


}
