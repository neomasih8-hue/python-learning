const display = document.getElementById('display');
const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.innerText;

    if (value === 'C') {
      display.value = ''; // Clears the screen
    } else if (value === '=') {
      try {
        display.value = eval(display.value); // Computes the answer
      } catch {
        display.value = 'Error';
      }
    } else {
      display.value += value; // Appends the clicked number/operator
    }
  });
});