// loader
var loader = document.getElementById('loader');
window.addEventListener('load', loaded);
function loaded() {
    loader.style.display = "none";
}
// theme
var theme = document.getElementById('theme');
var themeicon = document.getElementById('themeicon');
var iconvisible = 0;
var localtheme = localStorage.getItem("theme");
// checking for local storage files
window.localStorage;
function showthemebar() {
    if (iconvisible == 0) {
        theme.style.display = "block";
        iconvisible = 1;

    }
    else if (iconvisible == 1) {
        theme.style.display = "none";
        iconvisible = 0;
    }
}
