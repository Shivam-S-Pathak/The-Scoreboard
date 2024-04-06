let count = 5;
document.getElementById('add-subject').addEventListener('click', () => {
    if (count <=10) {
        let table = document.getElementById('subjects-table');
        let lastRow = table.rows.length - 1;
        let newRow = table.insertRow(lastRow);
        newRow.style.opacity = 0;
        setTimeout(() => {
            newRow.style.opacity = 1;
        }, 100);

        let headerCell1 = document.createElement("th");
        headerCell1.innerHTML = '<label for="subject_name">Subject Name:</label>';
        newRow.appendChild(headerCell1);
        newRow.insertCell(1).innerHTML = '<td><input type="text" name="sub' + count + '" class="input-box" autocomplete="off"></td>';

        let headerCell2 = document.createElement("th");
        headerCell2.innerHTML = '<label for="subject_name">Marks:</label>';
        newRow.appendChild(headerCell2);
        newRow.insertCell(3).innerHTML = '<td><input type="text" name="m' + count + '" class="input-box" autocomplete="off"></td>';

        let headerCell3 = document.createElement("th");
        headerCell3.innerHTML = '<label for="subject_name">PDF:</label>';
        newRow.appendChild(headerCell3);
        newRow.insertCell(5).innerHTML = '<td><input id="file-upload" type="file" name="pdf_file' + count + '" class="input-box" autocomplete="off"></td>';
        newRow.insertCell(6).innerHTML = '<td><button type="button" class="remove-subject" id="second" title="Remove this subject">✕</button></td>';
        count++;
    } else {
        alert("maximum number of subjects exceeded");
    }
});

let inputElements = document.getElementById('subjects-table');

inputElements.addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-subject")) {
        event.target.parentNode.parentNode.remove();
        count--;
    }
});


inputElements.addEventListener("input", (event) => {
    if (event.target.matches(".input-box")) {
        if (event.target.value.trim() !== "") {
            event.target.style.backgroundColor = "white";
        } else {
            event.target.style.backgroundColor = "rgba(255, 255, 255, 0.363)";
        }
    }
});

inputElements.addEventListener("input", (event) => {
    if (event.target.matches("select")) {
        if (event.target.value.trim() !== "") {
            event.target.style.backgroundColor = "white";
        } else {
            event.target.style.backgroundColor = "rgba(255, 255, 255, 0.363)";
        }
    }
});

