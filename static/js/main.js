var theme = document.getElementById('theme').value;
var ThemeIcon = document.getElementById('ThemeIcon');
console.log('theme =' + theme)
var DocStyle = document.documentElement.style;
var localStorageTheme = localStorage.getItem('theme');
// change theme
// set dark theme function
function setDark() {
    if(window.document.body.classList.contains('light-mode')){
        window.document.body.classList.replace('light-mode', 'dark-mode');
    }
    else{
        window.document.body.classList.add('dark-mode');
    }
    ThemeIcon.classList = 'bi bi-cloud-sun-fill';
    theme = 'dark';
    localStorage.setItem('theme', theme);
    console.log('theme:-' + theme);
}
// set light theme function
function setLight() {
    if(window.document.body.classList.contains('dark-mode')){
        window.document.body.classList.replace('dark-mode', 'light-mode');
    }
    else{
        window.document.body.classList.add('light-mode');
    }
    window.document.body.classList.replace('dark-mode', 'light-mode');
    ThemeIcon.classList = 'bi bi-moon-stars-fill';
    theme = 'light';
    localStorage.setItem('theme', theme);
    console.log('theme:-' + theme);
}
// changetheme conditions
function changeTheme() {
    DocStyle.transition = 'all 1s';

    if (theme == 'dark') {
        setLight();
    }
    else if (theme == 'light') {
        setDark();
    }
    else {
        setDark();
    }
}


// local theme set

if (localStorageTheme == 'dark') {
    setDark();
}
else if (localStorageTheme == 'light') {
    setLight();
}
else {
    if (window.matchMedia) {
        // Check if the dark-mode Media-Query matches
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            window.document.body.classList.add('dark-mode');
            console.log('set dark mode by system');
            ThemeIcon.classList = 'bi bi-cloud-sun-fill';
            theme = 'dark';

            // Dark
        } else {
            window.document.body.classList.add('light-mode');
            console.log('set light mode by system');
            ThemeIcon.classList = 'bi bi-moon-stars-fill';
            theme = 'light';


            // Light
            // console.log('system light')
        }
    } else {
        // Default (when Media-Queries are not supported)
    }
}



