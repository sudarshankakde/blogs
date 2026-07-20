var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/2m9gkwrp0pfon97n5wxy20rc5qxdwlg1a5adz1u2jr3bgowq/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
console.log('working');

script.onload = function () {
    // Remove HTML5 validation 'required' attribute to prevent browser focus errors on hidden elements
    const bodyEl = document.getElementById("id_body");
    if (bodyEl) bodyEl.removeAttribute("required");
    const caseStudyEl = document.getElementById("id_case_study");
    if (caseStudyEl) caseStudyEl.removeAttribute("required");

    tinymce.init({
        selector: "#id_body, #id_case_study",
        height: 500,
        width: '100%',
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'codesample table emoticons template paste help'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media codesample | ' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code codesample | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        codesample_languages: [
            { text: 'HTML/XML', value: 'markup' },
            { text: 'JavaScript', value: 'javascript' },
            { text: 'CSS', value: 'css' },
            { text: 'PHP', value: 'php' },
            { text: 'Ruby', value: 'ruby' },
            { text: 'Python', value: 'python' },
            { text: 'Bash', value: 'bash' },
            { text: 'Dart', value: 'dart' },
            { text: 'Java', value: 'java' },
            { text: 'C', value: 'c' },
            { text: 'C#', value: 'csharp' },
            { text: 'C++', value: 'cpp' },
        ],
        content_css: 'css/content.css'
    });
}