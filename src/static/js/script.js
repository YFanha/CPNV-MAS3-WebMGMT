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
    const tableBody = document.querySelector("table tbody"); // Select the table body
    const rows = tableBody.querySelectorAll("tr"); // Get all rows in the table body
    
    // Determine the new row's ID by checking the last row's ID
    let newId = 1; // Default to 1 if no rows exist

    if (rows.length > 0) {
        // Get the ID of the last row
        const lastRow = rows[rows.length - 1];
        const lastId = lastRow.querySelector('input[name="id"]')?.value || 0;
        newId = parseInt(lastId) + 1; // Increment the last ID by 1 for the new row
    }

    // Check if the newId already exists in any of the rows
    let idExists = false;
    do {
        idExists = false;
        // Iterate over each row to check if the newId already exists
        for (let row of rows) {
            const existingId = row.querySelector('input[name="id"]')?.value;
            if (existingId == newId) {
                idExists = true; // If the ID exists, flag it
                break;
            }
        }
        if (idExists) {
            newId++; // Increment the ID if it already exists
        }
    } while (idExists); // Continue checking until a unique ID is found

    // Create a new row element
    const newRow = document.createElement("tr");
    newRow.classList.add("table-primary")

    // Set the HTML content of the new row
    newRow.innerHTML = `
        <input type="hidden" name="id" value="${newId}">  <!-- Set the ID of the new row -->
        <th class="text-center">
            <input type="text" class="form-control border-0 bg-transparent text-center p-0 text-center fw-bold" name="name" value="">
        </th>
        <td class="text-center">
            <input type="number" class="form-control border-0 bg-transparent text-center p-0 transparent-input text-center" name="nbr" value="">
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
