window.addEventListener('load', function () {
    const inputs = document.getElementsByTagName('input');
    let submitBtns = []
    let images = []

    Array.from(inputs).forEach(input => {
        if (input.type === 'submit') {
            submitBtns.push(input);
        } else if (input.type === 'file') {
            images.push(input)
        }
    })

    submitBtns.forEach(submitBtn => {
        submitBtn.addEventListener('click', function (e) {
            if (window.File && window.FileReader && window.FileList && window.Blob) {
                images.forEach(image => {
                    if (image.files.length > 0 && image.files[0].size > 1 * 1024 * 1024) {
                        // $('errorliste').text("El archivo no puede ser mayor a 1 MB. El archivo subido es de " + (imageInput.files[0].size / 1024 / 1024).toFixed(2))
                        alert("El archivo no puede ser mayor a 1 MB. El archivo subido es de " + (image.files[0].size / 1024 / 1024).toFixed(2) + 'MB');
                        e.preventDefault();
                    }
                });
            }
        });
    });

});


