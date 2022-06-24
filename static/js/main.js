// const findByLocation = () => {

//     const status = document.querySelector('.status');

//     const successCallback = (position) => {
//         console.log(position);
//         const lat = position.coords.latitude;
//         const long = position.coords.longitude;
        
//         const geoApiUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${lat}&longitude=${long}&localityLanguage=en`

//         fetch(geoApiUrl)
//         .then(res => res.json())
//         .then(data => {
//             console.log(data.postcode)
//         })

//     };
    
//     const errorCallback = () => {
//         status.textContent = "Unable to retrieve your location.";
//     };

//     navigator.geolocation.getCurrentPosition(successCallback, errorCallback, {
//         enableHighAccuracy: true
//     });
// }

// document.querySelector('.btn-find').addEventListener('click', findByLocation);