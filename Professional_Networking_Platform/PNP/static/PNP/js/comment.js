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

    document.addEventListener('click', (e)=> {
        console.log(e.target);
        if (e.target.id === 'sendcomment') {
            addComment(e.target);
        }
    });

 // Send AJAX request to update the like count
 function addComment(likeButton) {
    var postId = likeButton.closest('.post').dataset.id;
    $.ajax({
        url: '/comment/' + postId + '/',
        type: 'POST',
        dataType: 'json',
        headers: { 'X-CSRFToken': '{{ csrf_token }}' },
        success: function (response) {
            if (response.success) {
                console.log(response.comments);
                document.querySelector('.comments[id=\"'+postId+'\"]').innerText = response.comments + ' comments';
            }
        }
    });
}
