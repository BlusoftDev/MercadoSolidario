

        
      
        const extNumberInput = document.getElementById('extNumber');
        const streetInput = document.getElementById('street');
        const colonyInput = document.getElementById('colony');
        const cpInput = document.getElementById('id_postal_code');
        const cityInput = document.getElementById('city');
        const localityInput = document.getElementById('locality');
        const phoneInput = document.getElementById('id_cellphone');
        const paymentInput = document.getElementById('id_payment_method');
        
        const submitBtn = document.getElementById('submitBtn');
        submitBtn.setAttribute('disabled', 'true');


        cityInput.addEventListener('change', () =>{
          setMarket()
          disableSubmitBtn()
        })
       
        cpInput.addEventListener('change', () =>{
          setMarket()
          disableSubmitBtn()
        })
        colonyInput.addEventListener('change', () =>{
          setMarket()
          disableSubmitBtn()
        })
        phoneInput.addEventListener('change', () =>{
          disableSubmitBtn()
        })
        paymentInput.addEventListener('change', () =>{
          disableSubmitBtn()
        })
        extNumberInput.addEventListener('change', () =>{
            setMarket()
        })
        streetInput.addEventListener('change', () =>{
            setMarket()
        })
        colonyInput.addEventListener('change', () =>{
            setMarket()
        })
        
        

        function disableSubmitBtn(){
          console.log(phoneInput.value ==='')
          if(cityInput.value === 2 || 
            
            cpInput.value ==='' ||
            colonyInput.value === '' ||
            phoneInput.value ===''
          ){
            submitBtn.setAttribute('disabled', 'true');
          }else{
            submitBtn.removeAttribute('disabled')
          }
        }
        

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



        function setMarket(){
            const city = document.getElementById('city')
            const cityValue = (city.options[city.selectedIndex].text)
            
            const extNumber = document.getElementById('extNumber').value
            const street = document.getElementById('street').value
            const colony = document.getElementById('colony')
            const colonyValue = colony.value
            const cp = document.getElementById('id_postal_code').value
            
            const address = extNumber+' '+street+' '+colonyValue+' '+cityValue
            const splitAddress = address.split(' ')
            const urlAddress = splitAddress.join('+')

            console.log(urlAddress)

            const url='https://maps.googleapis.com/maps/api/geocode/json?address='+urlAddress+'&key=AIzaSyC9YTgCN-8vKj4OKnRzEWihyNiaXnBDGsk'
                console.log(url)
            fetch(url).then(response => response.json()).then(data => {
            console.log(data)
            const location=data.results[0].geometry.location
            const myPlace = {lat:Number(location.lat), lng:Number(location.lng)}
            const lat = document.getElementById('id_lat').value = location.lat
            const lng = document.getElementById('id_long').value = location.lng
            console.log(document.getElementById('id_long').value, document.getElementById('id_lat').value)
            initMap(myPlace)
        })
        }
    