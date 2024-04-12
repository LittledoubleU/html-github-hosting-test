//JavaScript to update data for Modal A

// Variable to store data for Modal A
var dataModalA = {};

// Function to update data for Modal A
function updateDataModalA() {
    // Update data for Modal A as needed
    dataModalA.field1 = document.getElementById('input_field_modal_a').value;
    // Add more fields as needed
}

// Event listener for input changes in Modal A
document.getElementById('input_field_modal_a').addEventListener('input', updateDataModalA);


//JavaScript to update data for Modal B

// Variable to store data for Modal B
var dataModalB = {};

// Function to update data for Modal B
function updateDataModalB() {
    // Update data for Modal B as needed
    dataModalB.field1 = document.getElementById('input_field_modal_b').value;
    // Add more fields as needed
}

// Event listener for input changes in Modal B
document.getElementById('input_field_modal_b').addEventListener('input', updateDataModalB);


//JavaScript to gather data for Modal C
function gatherDataForModalC() {
    // Gather data from Modals A and B
    var dataForModalC = {
        modalA: dataModalA,
        modalB: dataModalB
        // Add more data as needed
    };

    // Send data to backend
    fetch('/submit_modal_c', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
    },
        body: JSON.stringify(dataForModalC)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        // Handle response from backend if needed
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

