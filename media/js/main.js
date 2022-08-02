


var theme = document.getElementById('theme').value;
var ThemeIcon = document.getElementById('ThemeIcon');
console.log('theme =' + theme)
var DocStyle = document.documentElement.style;
var localStorageTheme = localStorage.getItem('theme');
// change theme
// set dark theme function
function setDark() {
    DocStyle.setProperty('--primary-text', 'white');
    DocStyle.setProperty('--primary-bg', '#1c2331');
    DocStyle.setProperty('--card-bg', '#37474f');
    DocStyle.setProperty('--primary-theme', '#a6c');
    ThemeIcon.classList='bi bi-cloud-sun-fill';
    theme = 'dark';
    localStorage.setItem('theme',theme);
    console.log('theme:-' + theme);
}
// set light theme function
function setLight() {
    DocStyle.setProperty('--primary-text', 'black');
    DocStyle.setProperty('--primary-bg', 'white');
    DocStyle.setProperty('--card-bg', 'white');
    DocStyle.setProperty('--primary-theme', '#4285f4');
    ThemeIcon.classList='bi bi-moon-stars-fill'
    theme = 'light';
    localStorage.setItem('theme',theme);
    console.log('theme:-' + theme);
}
// changetheme conditions
function changeTheme() {
    DocStyle.transition='all 1s';
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
    setLight();
}



