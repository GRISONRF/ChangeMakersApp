'use strict';

function initMap() {
    
    // Need to get the inst_id from div in html
    const inst_id = document.querySelector(".map").id;

    //pass the inst_id to the db to get the location for that inst 
    const queryString = new URLSearchParams({inst_id: inst_id});

    fetch(`/instgeocoords.json?${queryString}`)
        .then(response => response.json())
        .then(jsonData => {

            const basicMap = new google.maps.Map(document.querySelector('#inst-map'), {
                center: jsonData,
                zoom: 15,
            });

            const coordMarker = new google.maps.Marker({
                position: jsonData,
                title: 'Institution location',
                map: basicMap,
            });
    });
}


function eventMap() {
    
    // Need to get the event_id from div in html
    const event_id = document.querySelector(".maps").id;

    //pass the event_id to the db to get the location for that event 
    const queryString = new URLSearchParams({event_id: event_id});

    fetch(`/eventgeocoords.json?${queryString}`)
        .then(response => response.json())
        .then(jsonData => {

            const basicMap = new google.maps.Map(document.querySelector('#event-map'), {
                center: jsonData,
                zoom: 15,
            });

            const coordMarker = new google.maps.Marker({
                position: jsonData,
                title: 'Event location',
                map: basicMap,
            });
    });
}











/////////////////////////////////////////////////////////**DEMO 2 TEST */

// // Need to get the inst_id so I can acess the address?
// const inst_id = document.querySelector(".map").id
// const instCoords = {
//     lat: 37.601773,
//     lng: -122.20287,
// };
  
// const basicMap = new google.maps.Map(document.querySelector('#inst-map'), {
//     center: sfBayCoords,
//     zoom: 11,
// });

// const sfMarker = new google.maps.Marker({
//     position: sfBayCoords,
//     title: 'SF Bay',
//     map: basicMap,
// });

// sfMarker.addListener('click', () => {
//     alert('Hi!');
// });

// const sfInfo = new google.maps.InfoWindow({
//     content: '<h1>San Francisco Bay!</h1>',
// });

// sfInfo.open(basicMap, sfMarker);