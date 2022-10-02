var checkbox = document.getElementById("nav-toggle"),
    heading = checkbox.parentElement,
    body = document.querySelector("body");

heading.addEventListener("click", function(e) {
    e.stopPropagation();
})

body.addEventListener("click", function() {
    checkbox.checked = false;
})