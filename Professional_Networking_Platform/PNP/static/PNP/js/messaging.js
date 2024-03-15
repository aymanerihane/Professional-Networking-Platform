var dusc = document.querySelectorAll('.contacts ul li');

dusc.forEach((dus) => {
    dus.addEventListener('click', () => {
        dusc.forEach((dus) => {
            dus.classList.remove('active');
        });
        var id= this.dataset.id;
        var url = '/messaging/' + id;
        chnagerManupulation(url);
        dus.classList.add('active');
    });
});

// ajax function
function chnagerManupulation(url){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            document.getElementById('content').innerHTML = xhr.responseText;
            // setTimeout(function () {
            //     center.style.opacity = 1; // Set opacity to 1 to fade in the content
            // }, 30);
        }
    };
    xhr.open('GET', url, true);
    xhr.send();
}