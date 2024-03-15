// fisrtPage.html

// var fullName = document.getElementById('fullname');
// var imgOfUser = document.getElementById('userImg');
// var descOfUser = document.getElementById('descofuser');
// var descOfPost = document.getElementById('descofpost');
// var imgOfPost = document.getElementById('imgofpost');
// var sidebar = document.getElementById('sidebarActivity');

// var profileMenu = document.getElementById('profileMenu')
var popupcont = document.getElementById('popup')
var cont = document.getElementById('main');
function toggleMenu() {
    profileMenu.classList.toggle("open-menu");
}
function showSideBar() {
    sidebar.classList.toggle("open-activity")
    if (sidebar.classList.contains("open-activity")) {
        document.getElementById('showMoreLink').innerHTML = "Show Less <b>-</b>"
    }
    else {
        document.getElementById('showMoreLink').innerHTML = "Show More <b>+</b>"
    }
}




function popup() {
    popupcont.classList.toggle('open-popup')
}

// function add() {
// popupcont.classList.toggle('open-popup');

// const userImgFile = userImgInput.files[0];
// const imgOfPostFile = imgofpostInput.files[0];

// const userImgReader = new FileReader();
// const imgOfPostReader = new FileReader();

// userImgReader.onload = function (e) {
// const userImgDataUrl = e.target.result;
// document.getElementById('a').src = userImgDataUrl;
// };

// imgOfPostReader.onload = function (e) {
// const imgOfPostDataUrl = e.target.result;
// document.getElementById('b').src = imgOfPostDataUrl;
// };

// if (userImgFile) {
// userImgReader.readAsDataURL(userImgFile);
// }

// if (imgOfPostFile) {
// imgOfPostReader.readAsDataURL(imgOfPostFile);
// }
// alert("Your Post is Posted Scroll to The Bottom of the Page");
// cont.innerHTML += `
// <div class="post">
// <div class="post-author">
// <img id="a" src="" alt="User Image">
// <div>
//   <h1>${fullName.value}</h1>
//   <small>${descOfUser.value}</small>
//   <small>1 min ago</small>
// </div>
// </div>
// <p>${descOfPost.value}</p>
// <img id="b" src="" alt="Post Image" width="100%">
// <div class="post-stats">
// <div>
//   <img src="img/thumbsup.png">
//   <img src="img/love.png">
//   <img src="img/clap.png">
//   <span class="liked-users">AzaanUllah Khan and 5 others</span>
// </div>
// <div>
//   <span>0 comments &middot; 0 shares</span>
// </div>
// </div>
// <div class="post-activity">
// <div>
//   <img src="https://media.licdn.com/dms/image/D4D03AQHyJrtE6WbAfw/profile-displayphoto-shrink_100_100/0/1678030659122?e=1690416000&v=beta&t=9Vnws7rVjaREQebj3HeuNH3GQ_VS0XS4XFnkI5ttBpQ"
//     class="post-activity-user-icon">
//   <img src="img/down-arrow.png" class="post-activity-arrow-icon">
// </div>
// <div class="post-activity-link">
//   <img src="img/like.png" class="post-activity-user-icon">
//   <span>Like</span>
// </div>
// <div class="post-activity-link">
//   <img src="img/comment.png" class="post-activity-user-icon">
//   <span>Comment</span>
// </div>
// <div class="post-activity-link">
//   <img src="img/share.png" class="post-activity-user-icon">
//   <span>Share</span>
// </div>
// <div class="post-activity-link">
//   <img src="img/send.png" class="post-activity-user-icon">
//   <span>Send</span>
// </div>
// </div>
// </div>
// `;
// }

