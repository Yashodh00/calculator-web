const display = document.getElementById("display");
const buttons = document.querySelectorAll("[data-value]");
const clearButton = document.getElementById("clear");
const calculateButton = document.getElementById("calculate");

buttons.forEach(button => {
    button.addEventListener("click", () => {
        display.value += button.dataset.value;
    });
});

clearButton.addEventListener("click", () => {
    display.value = "";
});

calculateButton.addEventListener("click", async () => {
    const expression = display.value;

    if (expression === "") {
        return;
    }

    const response = await fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            expression: expression
        })
    });

    const data = await response.json();

    display.value = data.result;
});