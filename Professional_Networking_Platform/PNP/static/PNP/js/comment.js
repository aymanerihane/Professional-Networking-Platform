var commet= document.getElementById('comment')
var section=document.getElementById('commentSection')
var overlay=document.getElementById('overlay')
commet.addEventListener('click', function () {
    section.classList.toggle('open-comment');
    overlay.classList.toggle('overlay-open');
});

function closeComment() {
    section.classList.remove('open-comment');
    overlay.classList.remove('overlay-open');
}

