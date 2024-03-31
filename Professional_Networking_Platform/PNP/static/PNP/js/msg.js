
    
function previewFiles() {
    var preview = document.querySelector('#preview');
    var files   = document.querySelector('input[type=file]').files;

    function readAndPreview(file) {
        var removeButton = document.createElement('p');
        removeButton.textContent = 'x';
        removeButton.style.cursor = 'pointer';
        removeButton.style.color = 'red';
        removeButton.style.position = 'absolute';
        removeButton.style.top = '0';
        removeButton.style.right = '0';
        var container = document.createElement('div');
        container.style.position = 'relative';

        if ( /\.(jpe?g|png|gif)$/i.test(file.name) ) {
            var reader = new FileReader();

            reader.addEventListener("load", function () {
                var image = new Image();
                image.height = 100;
                image.style.position= 'relative';
                image.title = file.name;
                image.src = this.result;

                
                container.appendChild(image);
                container.appendChild(removeButton);
                preview.appendChild(container);
            }, false);

            reader.readAsDataURL(file);

        } else if( /\.(mp4|avi)$/i.test(file.name) ) {
            var video = document.createElement('video');
            video.src = URL.createObjectURL(file);
            video.height = 100;
            video.controls = true;

            container.appendChild(video);
            container.appendChild(removeButton);
            preview.appendChild(container);

        } else if( /\.(mp3)$/i.test(file.name) ) {
            var audio = document.createElement('audio');
            audio.src = URL.createObjectURL(file);
            audio.height = 100;
            audio.controls = true;

            container.appendChild(audio);
            container.appendChild(removeButton);
            preview.appendChild(container);

        } else if( /\.(pdf)$/i.test(file.name) ) {
            var pdf = document.createElement('iframe');
            pdf.src = URL.createObjectURL(file);
            pdf.height = 500;
            pdf.controls = true;

            container.appendChild(pdf);
            container.appendChild(removeButton);
            preview.appendChild(container);

        } else {
            var doc = document.createElement('p');
            doc.innerHTML = file.name;

            container.appendChild(doc);
            container.appendChild(removeButton);
            preview.appendChild(container);
        }

        removeButton.addEventListener('click', (event)=> {
        preview.removeChild(container);

        // Create a new DataTransfer object
        var dt = new DataTransfer();

        // Loop over the files in the file input
        for (var i = 0; i < inputElement.files.length; i++) {
            // If the file at the current index is not the file to be removed, add it to the DataTransfer object
            if (inputElement.files[i] !== file) {
                dt.items.add(inputElement.files[i]);
            }
        }

        // Set the files property of the file input to the files property of the DataTransfer object
        inputElement.files = dt.files;
    });
    }
    var inputElement = document.querySelector('input[type=file]');
    if (files) {
        [].forEach.call(files, readAndPreview);
    }
}

function quitterRoom(id){ // quitter room
        var url = '/quitterRoom/'+id+'/';
        var messagediv= document.getElementById('messagediv');
        $.ajax({
            type: 'GET',
            url: url,
            success: function(data){
                refresh_dusc();
                messagediv.innerHTML = `<div id="messageCont" style="height: 70vh;">
                <div class="content" style="position:relative; display: flex; justify-content: center; align-items: center; height: 100vh;">
                    <img style="width: 100px;" src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="">
                    <p style="text-align: center;">You should choose a room</p>
                </div>
            </div>
            <div id="messageForm">
            </div>`;
            }
        })
    }
function refresh_dusc(){ // refresh rooms
    $.ajax({
        url: '/searchRoom/x212x/',
        type: 'GET',
        success: function (response) {
            var dusc = document.getElementById('disc');
            dusc.innerHTML = response;
        }
    });
}
function getTypeFile(file){
    var type=file.type.split('/')[0];
    if ( type = /\.(jpe?g|png|gif|)$/i.test(file.name) ) {
        return 1;
    }else if( /\.(mp4|avi|)$/i.test(file.name) ){
        return 2;
    }else if( /\.(mp3|)$/i.test(file.name) ){
        return 3;
    }else if( /\.(pdf|)$/i.test(file.name) ){
        return 4;
    }else{
        return 5;
    }

     
}
document.addEventListener('click', async (e) => { 
    if( e.target.id == "MenbersShow"){
    document.getElementById('modifie').style.display = 'block';
    var form = document.getElementById('form-container');
    $.ajax({
        url: '/members/'+ e.target.dataset.id +'/',
        type: 'GET',
        success: function (response) {
            form.innerHTML = response;
        }
    });
    }else if(e.target.id == 'createRoom'){ // create room
        type=e.target.dataset.type;
        document.getElementById('modifie').style.display = 'block';
        if(type == 3){
            var id = e.target.dataset.id;
            console.log(id);
            getForm(type,id);
        }else{
            getForm(type,0);
        }

    }else if (e.target.classList.contains('overlay')) { // close form
        document.getElementById('modifie').style.display = 'none';
    }else if(e.target.id == "quitterDusc"){ // quitter room
        let id = e.target.dataset.id;
        quitterRoom(id);
    }else if(e.target.classList.contains('sendmessage')){ // send message
        let id = e.target.dataset.id;
        let input = document.querySelector('.message-form input[name=message]');
        let message = input.value;
        var files = document.querySelector('input[name=media]').files;
        var formData = new FormData();
        
        formData.append('message', message );
        formData.append('id', id );
        for (var i = 0; i < files.length; i++) {
            var type = await getTypeFile(files[i]); // await the result of getTypeFile
            formData.append('files', files[i]);
            formData.append('type', type);
        }
        if(message.trim() == '' && files.length == 0){
            return;
        }
        
        $.ajax({
            url:'/messageForm/'+id+'/',
            type:'POST',
            data:formData,
            processData: false, // add this line to prevent jQuery from converting the FormData into a string
            contentType: false, // add this line to prevent jQuery from setting a default content type
            beforeSend: function(xhr, settings) {
                function getCookie(name) {
                    var cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                            var cookie = jQuery.trim(cookies[i]);
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            success: function(response){
                getMessages(id);
                var input = document.querySelector('input[type="file"]');
                var preview = document.querySelector('#preview');
                var message = document.querySelector('.message-form input[name=message]');
                preview.innerHTML = '';
                message.value = '';
                input.value = '';
            }
        })
    }
});


document.addEventListener('click', (e) => { // get room messages and toogle active class
    if(e.target.classList.contains('roomdusc')){
        var dusc = document.querySelectorAll('.contacts ul li:not(#createRoom)');
        var room_ID = e.target.dataset.id;
        getMessages(room_ID);
        getFormMessage(room_ID);
        dusc.forEach((dus) => {
            dus.classList.remove('active');
        });
        e.target.classList.add('active');
    }
});



function getFormMessage(room_ID){ // get form message
    $.ajax({
        url: '/messageForm/'+ room_ID +'/',
        type: 'GET',
        success: function (response) {
            var form = document.getElementById('messageForm');
            form.innerHTML = response;
        }
    });
}

function getMessages(room_ID){ // get messages
    $.ajax({
        url: '/getMessages/'+ room_ID +'/',
        type: 'GET',
        success: function (response) {
            var messages = document.getElementById('messageCont');
            messages.innerHTML = response;
        }
    });
}


function getForm(type,id){ // get form of create dusc or group
    $.ajax({
        url: '/roomCreateForm/'+ type+'/'+ id +'/',
        type: 'GET',
        success: function (response) {
            var form = document.getElementById('form-container');
            form.innerHTML = response;
        }
    });
}

