'use strict';

function initMap() {


////////////////////////////////////////////////////////////**DEMO TEST 1 */

    // const locations = [
    //   {
    //     name: 'Hackbright Academy',
    //     coords: {
    //       lat: 37.7887459,
    //       lng: -122.4115852,
    //     },
    //   },
    //   {
    //     name: 'Powell Street Station',
    //     coords: {
    //       lat: 37.7844605,
    //       lng: -122.4079702,
    //     },
    //   },
    //   {
    //     name: 'Montgomery Station',
    //     coords: {
    //       lat: 37.7894094,
    //       lng: -122.4013037,
    //     },
    //   },
    // ];
  
    // const markers = [];
    // for (const location of locations) {
    //   markers.push(
    //     new google.maps.Marker({
    //       position: location.coords,
    //       title: location.name,
    //       map: basicMap,
    //       icon: {
    //         // custom icon
    //         url: '/static/img/marker.svg',
    //         scaledSize: {
    //           width: 30,
    //           height: 30,
    //         },
    //       },
    //     }),
    //   );
    // }
  
    // for (const marker of markers) {
    //   const markerInfo = `
    //     <h1>${marker.title}</h1>
    //     <p>
    //       Located at: <code>${marker.position.lat()}</code>,
    //       <code>${marker.position.lng()}</code>
    //     </p>
    //   `;
  
    // const infoWindow = new google.maps.Map(document.querySelector('#map'), {
    //                     content: markerInfo,
    //                     maxWidth: 200,
    // });

    // marker.addListener('click', () => {
    // infoWindow.open(basicMap, marker);
    // });
    // }

    /////////////////////////////////////////////////////////**DEMO 2 TEST */


    const sfBayCoords = {
        lat: 37.601773,
        lng: -122.20287,
    };
      
    const basicMap = new google.maps.Map(document.querySelector('#inst-map'), {
        center: sfBayCoords,
        zoom: 11,
    });

    const sfMarker = new google.maps.Marker({
        position: sfBayCoords,
        title: 'SF Bay',
        map: basicMap,
    });

    sfMarker.addListener('click', () => {
        alert('Hi!');
    });

    const sfInfo = new google.maps.InfoWindow({
        content: '<h1>San Francisco Bay!</h1>',
    });

    sfInfo.open(basicMap, sfMarker);


///////////////////////////////////////////////////////////////// TEST WITH INST INFO

    // // Need to get the inst_id so I can acess the address
    // const inst_id = document.querySelector(".inst-container").id

    // //pass the inst_id to the db to get the location for that inst 
    // const queryString = new URLSearchParams({inst_id: inst_id})

    // fetch(`/geocoords.json?${queryString}`)
    //     .then(response => response.json())
    //     .then(jsonData => {

    //         const basicMap = new google.maps.Map(document.querySelector('#map'), {
    //             center:jsonData,
    //             zoom: 8,
    //         })

    //         const coordMarker = new google.maps.Marker({
    //             position: jsonData,
    //             title: 'Institution location',
    //             map: basicMap,
    //         });
    // })

}