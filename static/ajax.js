// VOLUNTEER REGISTER PAGE

const createEvt = document.querySelector('#create-button');

createEvt.addEventListener('click', () => {
  /* When click the 'create new event' button */
  

  const queryString = new URLSearchParams({}).toString();
  const url = `/inst_profile?${queryString}`;



  fetch(url)
  .then((response) => response.json())
  .then((status) => {

    document.querySelector('create-volunteer').innerHTML = status;

  });

}
