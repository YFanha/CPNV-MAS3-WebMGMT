// function addRow() {
//     const tableBody = document.querySelector("table tbody"); // Select the table body
//     const newRow = document.createElement("tr"); // Create a new row element

//     // Set the HTML content of the new row
//     newRow.innerHTML = `
//         <th class="text-center">
//             <input type="text" class="form-control border-0 bg-transparent text-center p-0 text-center fw-bold" name="name" value="">
//         </th>
//         <td class="text-center">
//             <input type="number" class="form-control border-0 bg-transparent text-center p-0 transparent-input text-center" name="nbr" value="">
//         </td>
//     `;

//     // Append the new row to the table body
//     tableBody.appendChild(newRow);
// }


function removeRow(button) {
    // Get the row (tr) element of the button
    var row = button.closest("tr");

    // Remove the row from the table
    row.remove();
}

function addRow() {
    const tableBody = document.querySelector("table tbody");
    const rows = tableBody.querySelectorAll("tr"); 
    
    let newId = 1; // Default to 1 if no rows exist

    if (rows.length > 0) {
        const lastRow = rows[rows.length - 1];
        const lastId = lastRow.querySelector('input[name="id"]')?.value || 0;
        newId = parseInt(lastId) + 1; 
    }

    let idExists = false;
    do {
        idExists = false;
        for (let row of rows) {
            const existingId = row.querySelector('input[name="id"]')?.value;
            if (existingId == newId) {
                idExists = true; 
                break;
            }
        }
        if (idExists) {
            newId++; 
        }
    } while (idExists); 

    const newRow = document.createElement("tr");
    newRow.classList.add("table-success")

    newRow.innerHTML = `
        <input type="hidden" name="id" value="${newId}">  <!-- Set the ID of the new row -->
        <th class="text-center">
            <input type="text" class="form-control border-0 bg-transparent text-center p-0 fw-bold" name="name" value="" placeholder="Enterprise name">
        </th>
        <td class="text-center">
            <input type="number" class="form-control border-0 bg-transparent text-center p-0" name="nbr" value="" placeholder="1">
        </td>
        <td class="text-center">
            <button type="button" class="btn btn-danger btn-sm w-100 h-100 p-2" onclick="removeRow(this)">
                <i class="bi bi-x-circle"></i> Remove
            </button>
        </td>
    `;

    // Append the new row to the table body
    tableBody.appendChild(newRow);
}
