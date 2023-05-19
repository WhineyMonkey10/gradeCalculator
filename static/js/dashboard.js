document.getElementById('theme-toggle').addEventListener('click', function() {
    var theme = document.getElementById('theme');
    if (theme.getAttribute('class') == 'dark-theme') {
        theme.setAttribute('class', 'light-theme');
    } else {
        theme.setAttribute('class', 'dark-theme');
    }
});
