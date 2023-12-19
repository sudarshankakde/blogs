var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
console.log('working');

script.onload = function () {
    tinymce.init({
        selector: "#id_body",
        height: 400,
        width:'100%',
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak ',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            ' code codesample table emoticons template paste help'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media fullpage | ' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css'
    });
    tinymce.init({
        selector: 'textarea',
        plugins: 'codesample',
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
        force_br_newlines: true,
        force_p_newlines: false,
        forced_root_block: '' // Needed for 3.x
    });
}