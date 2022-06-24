// // CREATE A NEW EVENT FORM

// const createEvt = document.querySelector('#create-event');

// createEvt.addEventListener('click', (evt) => {
//   /* When click the 'create new event' button */
//   evt.preventDefault();

//   const formInputs = { 
//     evt_title: document.querySelector('#evt_title').value,
//     evt_date: document.querySelector('#evt_date').value,
//     evt_start_time: document.querySelector('#evt_start_date').value,
//     evt_end_time: document.querySelector('#evt_end_time').value,
//     evt_address: document.querySelector('#evt_address').value,
//     evt_description: document.querySelector('evt_description').value,
//   }
    
//   fetch('/new-event', { //IS THAT RIGHT?
//     method: 'POST',
//     body: JSON.stringify(formInputs),
//     headers: {
//       'Content-Type': 'application/json',
//     },
//   })

//   .then((response) => response.json())
//   .then((responseJson) => {

//     console.log(responseJson)
//     document.querySelector('#new-event').innerHTML = responseJson;

//   });

// })

// CREATE A NEW EVENT BUTTON
// const createEvent = document.getElementById('createEvent')
// console.log(createEvent)

// createEvent.addEventListener('show.bs.modal', event => {
//   // Button that triggered the modal
//   const button = event.relatedTarget
//   // Extract info from data-bs-* attributes
//   const recipient = button.getAttribute('data-bs-whatever')
//   // If necessary, you could initiate an AJAX request here
//   // and then do the updating in a callback.
//   //
//   // Update the modal's content.
//   const modalTitle = createEvent.querySelector('.modal-title')
//   const modalBodyInput = createEvent.querySelector('.modal-body input')

//   modalTitle.textContent = `New message to ${recipient}`
//   modalBodyInput.value = recipient
// })



// Create an event handler to the causes button

// const animal_button = document.querySelector("#animals");

