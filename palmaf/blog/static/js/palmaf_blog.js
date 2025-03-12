function changeLang(lang) {
    document.cookie = "lang=" + lang + ";path=/";
    location.reload(); // refresh the page
}