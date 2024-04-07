const increaseBtn = document.querySelector(".increase-btn");
increaseBtn.addEventListener('click', (event) => {
    let currSize = parseInt(window.getComputedStyle(document.querySelector("#textarea")).fontSize);
    const maxSize = 48; // Adjust this value as needed (e.g., 36, 72)
    if (currSize + 2 > maxSize) {
        currSize = maxSize;
    } else {
        currSize += 2;
    }
    textarea.style.fontSize = `${currSize}px`;
    textarea.style.transition = 'font-size 0.2s ease-in-out';
    event.preventDefault();
    
    
});

const decreaseBtn = document.querySelector(".decrease-btn");
decreaseBtn.addEventListener('click', (e) => {
    let curtSize = parseInt(window.getComputedStyle(document.querySelector("textarea")).fontSize);
    const minSize = 13.3; // Adjust this value as needed (e.g., 36, 72)
    if (curtSize - 2 < minSize) {
        curtSize = minSize;
    } else {
        curtSize -= 2;
    }
    textarea.style.fontSize = `${curtSize}px`;
    textarea.style.transition = 'font-size 0.2s ease-in-out';
    e.preventDefault();
    
});