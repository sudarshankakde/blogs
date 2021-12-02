
//  theme
window.localStorage
var theme = document.getElementById('theme');
var body = document.getElementById('body');
var currentTheme = 0;
var localtheme = localStorage.getItem("theme");
var btnColor = localStorage.getItem("btnColor");
var TextColor = localStorage.getItem("TextColor");
if (localtheme == 0) {
    theme.classList = 'bi bi-cloud-sun-fill';
    document.documentElement.style.setProperty('--primary-text', TextColor);
    document.documentElement.style.setProperty('--secondary-text', 'rgb(20, 20, 20)');
    document.documentElement.style.setProperty('--primary-theme', btnColor);
    document.documentElement.style.setProperty('--secondary-theme', '#4285f4');
    body.classList = 'bg-dark';
    currentTheme = 1;
    localStorage.setItem("theme", 0);
}

else if (currentTheme == 1) {
    document.documentElement.style.setProperty('--primary-text', TextColor);
    document.documentElement.style.setProperty('--secondary-text', '#ffffff');
    document.documentElement.style.setProperty('--primary-theme', btnColor);
    document.documentElement.style.setProperty('--secondary-theme', '#a6c');
    theme.classList = 'bi bi-moon-stars-fill';
    body.classList = 'bg-light';
    currentTheme = 0;
    localStorage.setItem("theme", 1);

}


// changing on click
function changeTheme() {
    body.style.transitionDelay = '0.2s';
    if (currentTheme == 0) {
        theme.classList = 'bi bi-cloud-sun-fill';
        document.documentElement.style.setProperty('--primary-text', '#ffffff');
        document.documentElement.style.setProperty('--secondary-text', 'rgb(20, 20, 20)');
        document.documentElement.style.setProperty('--primary-theme', '#a6c');
        document.documentElement.style.setProperty('--secondary-theme', '#4285f4');
        body.classList = 'bg-dark';
        currentTheme = 1;
        localStorage.setItem("theme", 0);
        localStorage.setItem("btnColor","#a6c")
        localStorage.setItem("TextColor","#ffffff")
    }
    else if (currentTheme == 1) {
        document.documentElement.style.setProperty('--primary-text', 'rgb(20, 20, 20)');
        document.documentElement.style.setProperty('--secondary-text', '#ffffff');
        document.documentElement.style.setProperty('--primary-theme', '#4285f4');
        document.documentElement.style.setProperty('--secondary-theme', '#a6c');
        theme.classList = 'bi bi-moon-stars-fill';
        body.classList = 'bg-light';
        currentTheme = 0;
        localStorage.setItem("theme", 1);
        localStorage.setItem("btnColor","#4285f4")
        localStorage.setItem("TextColor","rgb(20, 20, 20)")

    }
    else {
        document.documentElement.style.setProperty('--primary-text', 'rgb(20, 20, 20)');
        document.documentElement.style.setProperty('--secondary-text', '#ffffff');
        document.documentElement.style.setProperty('--primary-theme', '#4285f4');
        document.documentElement.style.setProperty('--secondary-theme', '#a6c');
        theme.classList = 'bi bi-moon-stars-fill';
        body.classList = 'bg-light';
        currentTheme = 0;
        localStorage.setItem("theme", 1);
        localStorage.setItem("btnColor","#4285f4")
        localStorage.setItem("TextColor","rgb(20, 20, 20)")
    }
}

