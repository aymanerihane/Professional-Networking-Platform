
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







