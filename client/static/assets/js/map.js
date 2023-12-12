var map;
var res = { prev: null };
var marker;
async function initMap() {


  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    center: { lat: 11.01613, lng: 76.936108 },
    zoom: 16,
    mapId: "4504f8b37365c3d0",
    styles: [
      {
        featureType: "all",
        elementType: "labels",
        stylers: [{ visibility: "off" }],
      },
      {
        featureType: "road.local",
        elementType: "labels",
        stylers: [{ visibility: "on" }],
      },
      {
        featureType: "transit.station.bus",
        elementType: "labels",
        stylers: [{ visibility: "on" }],
      },
    ],
    // mapTypeId: google.maps.MapTypeId.SATELLITE
  });
  var prev = new AdvancedMarkerElement({
    position: { lat: 0, lng: 0 },
    map: null
  });


  setInterval(async () => {
    let response = await fetch("http://127.0.0.1:8080/dgnss", {
      method: "GET",
    });
    let response2 = await fetch("http://127.0.0.1:8080/getLoc", {
      method: "GET",
    });
    prev.map = null
    let data = await response.text();
    let data2 = await response2.text();
    console.log(JSON.parse(data));
    console.log(JSON.parse(data2));
    const x = JSON.parse(data);
    const y = JSON.parse(data2);
    const marker = new AdvancedMarkerElement({
      position: { lat: y.lat + x.dlat, lng: y.long + x.dlong },
      map: map
    });
    prev = marker
  }, 2000);
}

initMap();
