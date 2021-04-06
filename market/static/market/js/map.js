function initMap(myPlace) {
            var ures = {lat: 29.427, lng: -110.393};
            // The map, centered 
            var map = new google.maps.Map(
            document.getElementById('map'), {zoom: 6, center: ures});
            if(myPlace){
                var marker = new google.maps.Marker({position: myPlace, map: map, draggable: true,})
                google.maps.event.addListener(marker, 'dragend', function (evt) {
                    map.setCenter(marker.position);
                    marker.setMap(map);
                    const lat = document.getElementById('id_lat').value = evt.latLng.lat().toFixed(6)
                    const lng = document.getElementById('id_long').value = evt.latLng.lng().toFixed(6)
                    console.log(document.getElementById('id_long').value, document.getElementById('id_lat').value)
                })
            }
            
            
        }