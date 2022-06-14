// VOLUNTEER REGISTER PAGE


function showVolunteerForm(evt) {
    /* When click to register as volunteer */

    evt.preventDefault();

    const url = '/register'

    fetch(url)
    .then((response) => response.text())
    .then((status) => {
      document.querySelector('create-volunteer').innerHTML = status;
    });

} 