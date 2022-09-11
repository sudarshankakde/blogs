// loader
var loader = document.getElementById('loader');
window.addEventListener('load', loaded);
function loaded() {
    setTimeout(() => {
        
        loader.style.display = "none";
        document.body.style.overflow="visible";
    }, 500);
}